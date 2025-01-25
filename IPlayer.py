from abc import ABC, abstractmethod

class IPlayer(ABC):
    @property
    @abstractmethod
    def player(self):
        pass

    @player.setter
    @abstractmethod
    def player(self, value):
        pass

    @property
    @abstractmethod
    def state(self):
        pass

    @state.setter
    @abstractmethod
    def state(self, value):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @abstractmethod
    def play(self):
        pass
