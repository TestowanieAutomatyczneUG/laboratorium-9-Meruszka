from src.main import Env

class Checker:
    def __init__(self) -> None:
        self._env = Env()
        self._was_played = False

    def was_played(self):
        return self._was_played

    def wavePlay(self):
        self._was_played = True
    
    def resetWave(self):
        self._was_played = False
    
    def reminder(self):
        cur = self._env.getTime().hour
        if cur >= 17:
            self._env.playWaveFile("place holder")
            self.wavePlay()
