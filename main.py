import vlc
from time import sleep

class InternetRadio(object):
    def __init__(self, volume=70):
        self.volume = int(volume)
        self.stations = dict([
            ("test", "1.mp3"),
            ("Monte Carlo", "http://icecast.unitedradio.it/RMC.mp3"),
            ("Jazz", "http://nashe1.hostingradio.ru:80/jazz-256"),
            ("Книга", "http://bookradio.hostingradio.ru:8069/fm")])

    def play(self, station):
        player = vlc.MediaPlayer(self.stations[station])
        player.audio_set_volume(self.volume)
        player.play()
        sleep(5)  # Or however long you expect it to take to open vlc
        while player.is_playing():
            sleep(1)

    def set_volume(self, volume):
        if isinstance(volume, int) and 0 <= volume <= 100:
            self.volume = int(volume)
            return True
        else:
            return False


r = InternetRadio()
r.play("Monte Carlo")
