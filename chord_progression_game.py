import pygame
import random
import os
from create_chord_progressions import is_valid_progression, create_mid_from_progression, save_chord_progression
from create_chord_progressions import CHORDS, PROGRESSIONS

TARGET_PROG_FILE = "target_progression.mid"
USER_PROG_FILE = "user_progression.mid"


def select_target_progression():
    target_progresison = random.choice(PROGRESSIONS)
    mid = create_mid_from_progression(target_progresison)
    mid.save(TARGET_PROG_FILE)
    target_progression_name = " ".join(target_progresison)
    return target_progression_name


def play_mid(mid_file:str):
    pygame.mixer.music.load(mid_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(1000)


if __name__ == "__main__":

    print("***************************************************")
    print("* Welcome to the chord progression guessing game! *")
    print("***************************************************")
    print("Press 'Q' to exit the game.")
    print("Press 'R' to listen again.")

    pygame.init()

    target_progression_name = select_target_progression()
    play_mid(TARGET_PROG_FILE)

    right_answer = False
    user_input = ""

    while True:

        user_input = input("Enter your answer: ")

        if user_input.upper() == "Q":
            print(f"Right answer was: {target_progression_name}")
            pygame.quit()
            break

        if user_input.upper() == "R":
            
            pygame.mixer.music.load(TARGET_PROG_FILE)
            pygame.mixer.music.play()
            continue

        if user_input == target_progression_name:
            right_answer = True
            print("RIGHT ANSWER!!")
            user_input = input("Keep playing? [Y/N]: ")

            if user_input.upper() == "Y":
                target_progression_name = select_target_progression()
                play_mid(TARGET_PROG_FILE)
                continue
            pygame.quit()
            break

        user_progression = user_input.strip().split()
        if is_valid_progression(user_progression, debug=False):
            user_progression_mid = create_mid_from_progression(user_progression)
            user_progression_mid.save(USER_PROG_FILE)
            play_mid(USER_PROG_FILE)

        print("WRONG ANSWER!!")

    pygame.quit()
    if os.path.exists(USER_PROG_FILE):
        os.remove(USER_PROG_FILE)
    if os.path.exists(TARGET_PROG_FILE):
        os.remove(TARGET_PROG_FILE)
