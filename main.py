import itertools
import datetime
import sys
import logging

logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)

from spirecomm.communication.coordinator import Coordinator
from spirecomm.ai.agent import SimpleAgent
from spirecomm.spire.character import PlayerClass

### https://stackoverflow.com/a/21919644/6022781
import signal
import logging

class DelayedKeyboardInterrupt:

    def __enter__(self):
        self.signal_received = False
        self.old_handler = signal.signal(signal.SIGINT, self.handler)
                
    def handler(self, sig, frame):
        self.signal_received = (sig, frame)
        logging.debug('SIGINT received. Delaying KeyboardInterrupt.')
    
    def __exit__(self, type, value, traceback):
        signal.signal(signal.SIGINT, self.old_handler)
        if self.signal_received:
            self.old_handler(*self.signal_received)



if __name__ == "__main__":
    with DelayedKeyboardInterrupt():
        logging.info("initializing agent")
        agent = SimpleAgent()
        coordinator = Coordinator()
        coordinator.signal_ready()
        coordinator.register_command_error_callback(agent.handle_error)
        coordinator.register_state_change_callback(agent.get_next_action_in_game)
        coordinator.register_out_of_game_callback(agent.get_next_action_out_of_game)

        # Play games forever, cycling through the various classes
        for chosen_class in itertools.cycle(PlayerClass):
            agent.change_class(chosen_class)
            result = coordinator.play_one_game(chosen_class)
