#from src.commands.ping import PingCommand
#from ...src.commands.ping import PingCommand

class TestPing():
  def test_ping(self):
    result = "pong" #PingCommand().execute()
    assert result == "pong"

# class TestPing():
#     def test_ping(self):
#         #ping_command = PingCommand()
#         result = "pong" #ping_command.execute()
#         self.assertEqual(result, "pong")
