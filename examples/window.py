import curses
from termgui.core import TermGUI

def main(stdscr):
    gui = TermGUI()
    gui.create_window(stdscr, 5, 10, 10, 40, title="Demo Window")
    stdscr.getch()

if __name__ == "__main__":
    gui = TermGUI()
    gui.start(main)
