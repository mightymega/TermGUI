# termgui/__init__.py

from .core import TermGUI
from .graphics import animate_text
from .input import handle_keyboard

__version__ = "0.1.0"

__all__ = ["TermGUI", "animate_text", "handle_keyboard"]
