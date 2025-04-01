import pygame
import os

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

music_folder = "music" 
songs = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]
current_song_index = 0
paused_position = 0

def play_song(index, start_pos=0):
    pygame.mixer.music.load(os.path.join(music_folder, songs[index]))
    pygame.mixer.music.play(start=start_pos)

if songs:
    play_song(current_song_index)

running = True
while running:
    screen.fill((30, 30, 30))  
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play / Resume
                if not pygame.mixer.music.get_busy():
                    play_song(current_song_index, paused_position)
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_s:  # Stop
                paused_position = pygame.mixer.music.get_pos() / 1000.0
                pygame.mixer.music.stop()
            elif event.key == pygame.K_n:  # Next song
                current_song_index = (current_song_index + 1) % len(songs)
                play_song(current_song_index)
                paused_position = 0
            elif event.key == pygame.K_b:  # Previous song
                current_song_index = (current_song_index - 1) % len(songs)
                play_song(current_song_index)
                paused_position = 0

pygame.quit()
