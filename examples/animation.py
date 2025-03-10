import curses
from termgui.graphics import animate_text

if __name__ == "__main__":
    curses.wrapper(animate_text)
