import vlc, time
from time import sleep


class InternetRadio(object):
    def __init__(self, valume=60):
        self.volume = int(valume)
        self.stations = dict([
            ("test", "test.mp3"),
            ("Monte Carlo", "http://icecast.unitedradio.it/RMC.mp3"),
            ("Jazz", "http://nashe1.hostingradio.ru:80/jazz-256"),
            ("Книга", "http://bookradio.hostingradio.ru:8069/fm")])
        self.player = vlc.MediaPlayer()
        self.set_volume(self.volume)

    def play(self, station):
        self.player.set_mrl(self.stations[station])
        self.player.play()

    def set_volume(self, volume):
        if isinstance(volume, int) and 0 <= volume <= 100:
            self.player.audio_set_volume(volume)
            self.volume = volume
            return True
        else:
            return False
    def set_station(self, stationNumber):
        if isinstance(stationNumber, int) and 1 <= stationNumber <= len(self.stations):
            stations = list(self.stations)
            self.play(stations[stationNumber-1])
            return True
        else:
            return False

    def stop(self):
        self.set_volume(0)


p = InternetRadio()
#p.play("test")

# Adjust volume
#while True:
    #newVolume = int(input())
    #p.set_volume(newVolume)

# Change station
while True:
    newStation = int(input())
    p.set_station(newStation)
