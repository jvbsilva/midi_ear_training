import os
from mido import Message, MidiFile, MidiTrack

# Mapping of chords intervals in the key of C major
CHORDS = {
    "i": [60, 63, 67],  # C minor chord: C4, Eb4, G4
    "I": [60, 64, 67],  # C major chord: C4, E4, G4
    "ii": [62, 65, 69],  # D minor chord: D4, F4, A4
    "II": [62, 66, 69],  # D major chord: D4, F#4, A4
    "iii": [64, 67, 71],  # E minor chord: E4, G4, B4
    "III": [64, 68, 71],  # E major chord: E4, G#4, B4
    "iv": [65, 68, 72],  # F minor chord: F4, Ab4, C5
    "IV": [65, 69, 72],  # F major chord: F4, A4, C5
    "v": [67, 70, 74],  # G minor chord: G4, Bb4, D5
    "V": [67, 71, 74],  # G major chord: G4, B4, D5
    "vi": [69, 72, 76],  # A minor chord: A4, C5, E5
    "VI": [69, 73, 76],  # A major chord: A4, C#5, E5
    "vii": [71, 74, 78],  # B minor chord: B4, D5, F#5
    "VII": [71, 75, 78],  # B major chord: B4, D#5, F#5
}

PROGRESSIONS = [
    # Minor key
    ["i", "VI", "VII"],
    ["i", "iv", "VII"],
    ["i", "iv", "v"],
    ["i", "VI", "III", "VII"],
    ["ii", "v", "i"],
    ["i", "iv", "v", "i"],
    ["i", "VII", "VI", "VII"],
    ["i", "iv", "i"],
    # Major key
    ["I", "IV", "V"],
    ["I", "vi", "IV", "V"],
    ["II", "V", "I"],
    ["I", "vi", "ii", "V"],
    ["I", "V", "vi", "IV"],
    ["I", "IV", "vi", "V"],
    ["I", "iii", "IV", "V"],
    ["I", "IV", "I", "V"],
    ["I", "IV", "ii", "V"],
]

# PROGRESSIONS = [
#     # valid progression
#      ["I", "IV", "ii", "V"],
#     # wrong progression
#     ["I", "ii", "x"]
# ]

def is_valid_progression(progression:list[str], debug = True) -> bool:
    for chord_symbol in progression:
        chord = CHORDS.get(chord_symbol)
        if not chord:
            if debug:
                raise ValueError(f"Invalid chord symbol '{chord_symbol}' in progression: {progression}")
            return False
    return True

def create_mid_from_progression(progression:list[str], velocity=64, duration=960) -> MidiFile:
    
    if is_valid_progression(progression):    
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
    
        for chord_symbol in progression:
            chord = CHORDS.get(chord_symbol)

            # Notes on
            for note in chord:
                track.append(Message("note_on", note=note, velocity=velocity, time=0))

            # Notes off
            track.append(
                Message("note_off", note=chord[0], velocity=velocity, time=duration)
            )
            for note in chord[1:]:
                track.append(Message("note_off", note=note, velocity=velocity, time=0))
    return mid

def save_chord_progression(progression: list[str],folder_name:str = "chord_progressions") -> None:

    if progression[0].isupper():
        filename = f"major_{'-'.join(progression)}.mid"
    else:
        filename = f"minor_{'-'.join(progression)}.mid"

    file_path = os.path.join(folder_name, filename)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    mid = create_mid_from_progression(progression)
    mid.save(file_path)
    
if __name__ == "__main__":
    for progression in PROGRESSIONS:
        save_chord_progression(progression)
