from .base_command import BaseCommand
class PingCommand(BaseCommand):
    def execute(self):
        return "pong"