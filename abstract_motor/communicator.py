from abc import ABC, abstractmethod


class Protocol(ABC):

    def __init__(self, *args, **kwargs):
        """
        Initialize communication protocol for individual device
        """
        pass

    @abstractmethod
    def generate_bindings(self, *args, **kwargs):
        """
        Generate bindings
        """
        pass

    @abstractmethod
    def push(self, *args, **kwargs):
        pass

    @abstractmethod
    def pull(self, *args, **kwargs):
        pass


class lcm(Protocol):

    def __init__(self, topic, freq, generate_bindings=False):
        """
        Initialize LCM protocol for individual device
        """

        self.topic = topic

        if generate_bindings:
            self.generate_bindings()

    def generate_bindings(self, *args, **kwargs):
        """
        Generate bindings
        """
        print("Generated LCM bindings")

    def push(self, content):
        print(f"Pushed to LCM topic:   {self.topic}")

    def pull(self, content):
        print(f"Pulled from LCM topic: {self.topic}")
