from kivy.app import App
from kivy.graphics import BorderImage, Color
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex

spacing = 15


def all_cells():
    for x in xrange(4):
        for y in xrange(4):
            yield (x, y)


class GameApp(App):
    # def on_start(self):
    #     board = self.root.ids.board
    #     board.reset()

    def build(self):
        return Board()


class Board(Widget):
    cell_size = None
    b = None

    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)
        self.resize()

    def resize(self, *args):
        self.cell_size = (0.25 * (min(self.width, self.height) - 5 * spacing),) * 2
        self.canvas.before.clear()
        with self.canvas.before:
            BorderImage(pos=self.pos, size=self.size, source='board.png')
            Color(*get_color_from_hex('CCC0B4'))
            for board_x, board_y in all_cells():
                BorderImage(pos=self.cell_pos(board_x, board_y), size=self.cell_size, source='cell.png')

    on_pos = resize
    on_size = resize

    def cell_pos(self, board_x, board_y):
        delta_x = (self.width - (self.cell_size[0] + spacing) * 4 - spacing) / 2
        delta_y = (self.height - (self.cell_size[1] + spacing) * 4 - spacing) / 2
        return (self.x + board_x * (self.cell_size[0] + spacing) + spacing + delta_x,
                self.y + board_y * (self.cell_size[1] + spacing) + spacing + delta_y)

    def reset(self):
        self.b = [[None for i in xrange(4)] for j in xrange(4)]

    def valid_cell(self, board_x, board_y):
        return 0 <= board_x <= 3 and 0 <= board_y <= 3

    def can_move(self, board_x, board_y):
        return self.valid_cell(board_x, board_y) and self.b[board_x][board_y]


if __name__ == '__main__':
    from kivy.config import Config

    Config.set('graphics', 'height', 1280 / 2)
    Config.set('graphics', 'width', 720 / 2)
    Config.write()
    GameApp().run()
