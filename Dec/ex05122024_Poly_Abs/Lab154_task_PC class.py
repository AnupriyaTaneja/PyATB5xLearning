# Create a Program
# Class - PC
# Class - MotherBoard
# ab → start MotherBoard
# Class - RAM
# abstractMethod → start ram
# Class - Processor
# abstractMethod → start processor
# Class - Storage
# abstractMethod → storage data,
# static method
# loadOS
# non static
# startMouse
# UseHeadPhone


from abc import ABC, abstractmethod

class PC:
    def __init__(self):
        print("PC initialized")

class MotherBoard:
    def start(self):
        print("MotherBoard started")

class RAM(ABC):
    @abstractmethod
    def start_ram(self):
        pass

class Processor(ABC):
    @abstractmethod
    def start_processor(self):
        pass

class Storage(ABC):
    @abstractmethod
    def storage_data(self):
        pass

    @staticmethod
    def loadOS():
        print("Operating System loaded")

    def startMouse(self):
        print("Mouse started")

    def useHeadPhone(self):
        print("Headphones connected")