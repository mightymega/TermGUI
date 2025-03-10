import curses

def handle_keyboard(stdscr):
    """Detects keyboard inputs and displays them."""
    stdscr.addstr(2, 2, "Press any key. Press 'q' to quit.")
    stdscr.refresh()
    
    while True:
        key = stdscr.getch()
        stdscr.clear()
        stdscr.addstr(2, 2, f"Key Pressed: {chr(key)}")
        stdscr.refresh()
        if key == ord('q'):
            break
