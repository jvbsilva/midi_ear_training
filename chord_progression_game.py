import pygame
import random
import os
from create_chord_progressions import is_valid_progression,create_mid_from_progression

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
    pygame.mixer.music.play()

    print("***************************************************")
    print("* Welcome to the chord progression guessing game! *")
    print("***************************************************")
    print("Press 'Q' to exit the game.")
    print("Press 'R' to listen again.")
    
    right_answer = False
    user_input = ""

    while True:
        
        user_input = input("Enter your answer: ")

        if user_input.upper() == "Q":
            pygame.quit()
            break

        if user_input.upper() == "R":
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            continue
        
        if user_input == progression_name:
            right_answer = True
            print("RIGHT ANSWER!!")
            user_input = input("Keep playing? [Y/N]: ")
            
            if user_input.upper() == "Y":
                file_name, file_path, progression_name = get_song()
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                continue
            pygame.quit()
            break
        
        user_progression = user_input.split(" ") 
        if is_valid_progression(user_progression):
            user_progression_mid = create_mid_from_progression(user_progression)
            user_progression_mid.save("user_progression.mid")
            pygame.mixer.music.load("user_progression.mid")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.wait(1000)
 
        print("WRONG ANSWER!!")
        user_input = input("Keep trying? [Y/N]: ")
        if user_input.upper() == "Y":
            user_input = "R"
    
    if not right_answer:
        print(f"Right answer was: {progression_name}")

    pygame.quit()
    if os.path.exists("user_progression.mid"):
        os.remove("user_progression.mid")
