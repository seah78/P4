import os


class Clear:
    """
    Efface l'écran
    """
    @staticmethod
    def screen():
        os.system('cls' if os.name == 'nt' else 'clear')