# Desenvola um código que abra e reproduza um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('csgo.mp3')
pygame.mixer.music.play()
pygame.event.wait()