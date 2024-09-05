import pygame
import random
import os

FORLDER_NAME = "chord_progressions"
FILE_LIST = [f for f in os.listdir(FORLDER_NAME) if f.endswith(".mid")]


def get_song():
    file_name = random.choice(FILE_LIST)
    file_path = os.path.join(FORLDER_NAME, file_name)
    progression_name = file_name.split(".")[0].split("_")[1].replace("-", " ")
    return file_name, file_path, progression_name


if __name__ == "__main__":
    pygame.init()
    file_name, file_path, progression_name = get_song()
    pygame.mixer.music.load(file_path)

    right_answer = False
    user_input = "R"
    print("***************************************************")
    print("* Welcome to the chord progression guessing game! *")
    print("***************************************************")
    print("Press 'Q' to exit the game.")
    print("Press 'R' to listen again.")
    while user_input.upper() == "R":
        print(progression_name)
        pygame.mixer.music.play()
        user_input = input("Enter your answer: ")
        if user_input.upper() == "Q":
            pygame.quit()
            break
        if user_input == progression_name:
            right_answer = True
            print("RIGHT ANSWER!!")
            user_input = input("Keep playing? [Y/N]: ")
            if user_input.upper() == "Y":
                user_input = "R"
                file_name, file_path, progression_name = get_song()
                print(progression_name)
                pygame.mixer.music.load(file_path)
                continue
            pygame.quit()
            break
        elif user_input.upper() != "R":
            print("WRONG ANSWER!!")
            user_input = input("Keep trying? [Y/N]: ")
            if user_input.upper() == "Y":
                user_input = "R"
    if not right_answer:
        print(f"Right answer was: {progression_name}")

    pygame.quit()
