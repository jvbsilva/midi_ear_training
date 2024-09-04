import pygame
import random
import os

if __name__ == "__main__":
    folder_name = "chord_progressions"

    file_list = [f for f in os.listdir(folder_name) if f.endswith('.mid')]

    file_name = random.choice(file_list)
    progression_name = file_name.split('.')[0]
    file_path = os.path.join(folder_name,file_name)
    
    pygame.init()
    pygame.mixer.music.load(file_path)
    
    user_input = "R"
    print("*************************************")
    print("* Welcome to the ear training game! *")
    print("*************************************")
    print("Press 'Q' to exit the game.")
    print("Press 'R' to listen again.")
    while user_input.upper() == "R":  
        pygame.mixer.music.play()
        user_input = input("Enter your answer: ")
        if user_input == progression_name:
            print("RIGHT ANSWER!!")
            break
    print(f"Anwser: {progression_name}")