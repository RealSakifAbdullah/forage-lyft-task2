from abc import abstractmethod
from car.serviceable import Serviceable
from engine.models.capulet_engine import CapuletEngine
from engine.models.sternman_engine import SternmanEngine
from engine.models.willoughby_engine import WilloughbyEngine
from battery.models.nubbin_battery import NubbinBattery
from battery.models.spindler_battery import SpindlerBattery
from datetime import datetime


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()