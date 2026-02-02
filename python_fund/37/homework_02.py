""" 02 Устройства

Создайте два класса:
MediaPlayer — поддерживает только аудио. Принимает список треков.
Laptop — поддерживает аудио и видео. Принимает списки треков и видео.
Проверьте работу классов, вызвав методы воспроизведения.

!!! Не забудьте проверить наличие атрибутов в КАЖДОМ объекте
"""

from homework_01 import AudioFileMixin, VideoFileMixin


# Класс MediaPlayer — поддерживает только аудио
class MediaPlayer(AudioFileMixin):
    def __init__(self, audio_tracks):
        self.audio_tracks = audio_tracks


# Класс Laptop — поддерживает и аудио, и видео
class Laptop(AudioFileMixin, VideoFileMixin):
    def __init__(self, audio_tracks, video_files):
        self.audio_tracks = audio_tracks
        self.video_files = video_files


# Примеры использования
player = MediaPlayer(["Песня 1", "Песня 2"])
laptop = Laptop(["Песня A", "Песня B"], ["Видео X", "Видео Y"])


player.play_audio()

try:
    player.play_video()
except AttributeError as e:
    print(f'{e.__class__.__name__}: {e}')

print()
laptop.play_audio()
laptop.play_video()

# Воспроизведение аудио для MediaPlayer:
# 	Песня 1
# 	Песня 2
# AttributeError: 'MediaPlayer' object has no attribute 'play_video'
#
# Воспроизведение аудио для Laptop:
# 	Песня A
# 	Песня B
# Воспроизведение видео для Laptop:
# 	Видео X
# 	Видео Y