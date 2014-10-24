import term, sys

log = open('/Users/Akshay/Desktop/log.log', 'w')

__windows = []

def add_window(window):
    __windows.append(window)
    __windows.sort(key=lambda x: x._z if not x._on_top else 99999)

def update():
    for window in __windows:
        window.draw()

class Window(object):

    def __init__(self, position, size, draw, z = 0, foreground = 'green', background = 'black', foreground_bright = True, background_bright = False):
        self._position = position
        self._size = size
        self._draw = draw
        self._z = z
        self._on_top = False
        self._foreground = foreground
        self._background = background
        self._foreground_bright = foreground_bright
        self._background_bright = background_bright
        self._buffer = ['#'*size[1]]*size[0]

    def __repr__(self):
        return "Window {position=" + str(self._position) + ", size=" + str(self._size) + ", z-index=" + str(self._z) + "}"

    def draw(self):
        term.set_cursor_position(*self._position)
        term.set_foreground(self._foreground, self._foreground_bright)
        term.set_background(self._background, self._background_bright)
        x,y = self._position
        while y < 25 and y - self._position[1] < self._size[1]:
            while x < 80 and x - self._position[0] < self._size[0]:
                sys.stdout.write(self._buffer[y - self._position[1]][x - self._position[0]])
                x += 1
            x = self._position[0]
            y += 1
            term.set_cursor_position(x,y)

        term.set_cursor_position(*map(lambda x: x+1, self._position))
        if (self._draw is not None):
            self._draw()
        term.set_foreground('default')
        term.set_background('default')


buf = [
    ['*','*','*','*','*','*','*','*','*','*'],
    ['*','A','A','A','A','A','A','A','A','*'],
    ['*','A','A','A','A','A','A','A','A','*'],
    ['*','A','A','A','A','A','A','A','A','*'],
    ['*','*','*','*','*','*','*','*','*','*']
]
win = Window((1,1), (10, 5), None, -5)
win._buffer = buf
add_window(win)
# add_window(Window((10,10), (10, 10), None, 100))

term.clear()

update()

raw_input()

log.write('\n'*25)
