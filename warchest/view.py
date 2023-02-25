from warchest.config import Config

class GameTerminalView:
    '''This class contains interactions with players'''

    @classmethod
    def select_action(cls) -> str:
        play: str = input("Make an action (moverecruit/place/attack/control/initiative/forfeit): ")

        while play.lower() not in Config.ACTIONS:
            print('Invalid action.')
            play = input("Make an action (moverecruit/place/attack/control/initiative/forfeit): ")
        return play.lower()

    @classmethod
    def start_game(cls) -> bool:
        play = input("Start game? (y/n): ")

        if play.lower() == 'y':
            return True
        else:
            if play.lower() == 'n':
                print("Ok, maybe next time. Bye.")
            else:
                print("Incorrect option. Bye.")
            return False    

    @classmethod
    def select_discard_coin(cls, message: str, options: list) -> str:
        coin: str = input(message+': ')
        while coin not in options:
            print('Invalid value.')
            coin = input(message+': ')
        return coin

    @classmethod
    def show(cls, message: str) -> None:
        print(message)