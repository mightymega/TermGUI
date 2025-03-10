import curses

class TermGUI:
    def __init__(self):
        self.stdscr = None

    def start(self, draw_func):
        curses.wrapper(draw_func)

    def create_window(self, stdscr, y, x, height, width, title="Window"):
        """Creates a bordered window with a title."""
        win = curses.newwin(height, width, y, x)
        win.box()
        win.addstr(0, 2, f" {title} ")
        win.refresh()
        return win
