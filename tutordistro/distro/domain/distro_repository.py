from abc import ABC, abstractmethod

class DistroRepository(ABC):
    @abstractmethod
    def clone(self):
        """
        Method to clone themes
        """
