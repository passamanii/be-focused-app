import pygame
from .utils import resource_path

class AudioManager:
    def __init__(self, sound_files_info):
        """ Carrega a playlist de sons """
        pygame.mixer.init()
        self.sounds = [pygame.mixer.Sound(resource_path(f[1])) for f in sound_files_info]
        self.sound_labels = [f[0] for f in sound_files_info]

    def play(self, index, volume):
        """ Toca um som se o mixer não estiver ocupado """
        if not pygame.mixer.get_busy():
            self.sounds[index].set_volume(volume)
            self.sounds[index].play()

    def get_busy(self):
        """ Retorna se o mixer está tocando algo """
        return pygame.mixer.get_busy()

    def stop_all(self):
        """ Para todos os sons """
        pygame.mixer.stop()

    def fadeout(self, index, ms=500):
        """ Aplica fadeout em um som específico """
        self.sounds[index].fadeout(ms)
