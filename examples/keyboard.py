import curses
from termgui.input import handle_keyboard

if __name__ == "__main__":
    curses.wrapper(handle_keyboard)
