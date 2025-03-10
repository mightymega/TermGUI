import curses
import time

def animate_text(stdscr, text="🚀 TermGUI Animation 🚀"):
    """Moves text across the screen."""
    curses.curs_set(0)
    height, width = stdscr.getmaxyx()
    
    x = 0
    while x < width - len(text):
        stdscr.clear()
        stdscr.addstr(height // 2, x, text)
        stdscr.refresh()
        time.sleep(0.05)
        x += 1
