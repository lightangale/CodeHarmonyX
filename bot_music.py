import os
import pygame

current_song = None

def play_music(song_name):
    global current_song
    try:
        current_song = song_name
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing {song_name}: {e}")

def pause_resume_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def show_menu(songs):
    print("Choose a song to play:")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song}")

def music():
    pygame.init()
    pygame.mixer.init()

    while True:
        songs = [file for file in os.listdir() if file.endswith(".mp3")]
        show_menu(songs)
        choice = input("Enter the number of the song you want to play (0 to exit, p to pause/resume): ")
        
        if choice == '0':
            break
        elif choice.lower() == 'p':
            pause_resume_music()
        else:
            try:
                choice = int(choice)
                if 1 <= choice <= len(songs):
                    song_name = songs[choice - 1]
                    play_music(song_name)
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    pygame.mixer.quit()
    pygame.quit()

if __name__ == "__main__":
    music()
