import openai
import bot_music
import bot_timer
import bot_voice
import bot_quiz
from bot_music import music

openai.api_key = "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"

def chat_with_gpt(username, user_command=None):
    while True:
        if user_command and user_command.lower() == "yes":
            prompt = bot_voice.voice()
            print(f"You said: {prompt}")
            if prompt is None:
                continue
        else:
            prompt = input(f"{username}: ")

        if user_command and user_command.lower() == "stop" or prompt.lower() == "stop":
            menu()
            break

        if user_command and user_command.lower() == "bye" or prompt.lower() == "bye":
            print("Goodbye!")
            break

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        print("Botsy:", response.choices[0].message['content'].strip())

    return response.choices[0].message['content'].strip()

def quit():
    print("Quitting now....")

def menu():
    option = {
        1: chat_with_gpt,
        2: music,
        3: bot_timer.timer,
        4: bot_quiz.quiz,
        5: quit
    }
    
    print("MENU\t")
    print("Choose from the following numbers(1-5) according to what you want")
    print("\n1)Doubt Bot\n2)Music\n3)Timer\n4)Quiz\n5)Quit")

    while True:
        option_num = input("\nEnter Your Choice: ")
        if option_num.isdigit():
            option_num = int(option_num)
            if 1 <= option_num <= 5:
                if option_num == 5:
                    quit()  
                    break
                elif option_num==1:
                    user_command = input("Would you like voice typing? 1)Yes or No\n")
                    option[option_num](username, user_command=user_command)
                else:
                    option[option_num]() 
                break
            else:
                print("Please enter a valid range between 1-5")
        else:
            print("Please enter a digit between 1-5!")

if __name__ == "__main__":
    username = input("Enter your username:")
    menu()
