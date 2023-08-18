from .base_command import BaseCommand
from ..errors.errors import InvalidParams

class Sumar(BaseCommand):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def execute(self):
        if (not isinstance(self.x , (int, float))) or (not isinstance(self.y , (int, float))):
            raise  InvalidParams
        return self.x + self.y