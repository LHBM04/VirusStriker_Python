from Utilities.AudioManager import AudioManager
import turtle as turtle
import pygame
import time

pygame.init()

size = [200, 200]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("연습")

audioManager = AudioManager()
testBGM = audioManager.CreateAudio('Resources/Audio/BGM/BGM_MainMenu0.flac')
audioManager.PlayPrimaryBGM(testBGM)

input()
audioManager.StopPrimaryBGM()
time.sleep(2)
pygame.quit()