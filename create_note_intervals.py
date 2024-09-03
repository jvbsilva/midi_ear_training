from mido import Message, MidiFile, MidiTrack
import os
# Mapping of interval names to semitones
intervals = {
    'minor_second': 1,
    'major_second': 2,
    'minor_third': 3,
    'major_third': 4,
    'perfect_fourth': 5,
    'tritone': 6,
    'perfect_fifth': 7,
    'minor_sixth': 8,
    'major_sixth': 9,
    'minor_seventh': 10,
    'major_seventh': 11,
    'octave': 12
}

def generate_midi(note: int, interval_name: str):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # Start with the root note
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=480))

    # Calculate the next note based on the interval
    interval = intervals.get(interval_name.lower())
    if interval is None:
        raise ValueError(f"Invalid interval name: {interval_name}")

    next_note = note + interval

    # Add the next note
    track.append(Message('note_on', note=next_note, velocity=64, time=480))
    track.append(Message('note_off', note=next_note, velocity=64, time=480))

    # Save the MIDI file
    folder_name = "note_intervals"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = f"{note}_{interval_name}.mid"
    file_path = os.path.join(folder_name, filename)
    mid.save(file_path)

def main():
    for interval in intervals:
        for note in range(60,72,1):
            generate_midi(note, interval)
            
if __name__ == "__main__":
    main()
