from module.game import Game, load
from module.interface import clear, query, wait, generate_text_box
from module.interface import HOME
from module.backend import Prompt

class MainMenu(Prompt):
    def build(self):
        self.options = [self.start, self.load, self.end]
        self.stops = [self.end]

    def ask(self):
        return query(header=HOME, num=len(self.options))

    def start(self):
        game = Game()
        game.new()

    def load(self):
        game = load()
        game.start()

    def end(self):
        tbox = generate_text_box(
            'Thanks for playing!',
            h_margin=9)
        print(tbox)
        wait()
        clear()

def main():
    menu = MainMenu()
    menu.run()

if __name__ == '__main__':
    main()
