from abc import ABC, abstractmethod
class Object(ABC):
    def __init__(self, position):
        self.position = position

    @abstractmethod
    def draw(self):
        pass

