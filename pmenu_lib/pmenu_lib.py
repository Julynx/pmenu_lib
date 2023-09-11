"""
@file     pmenu_lib.py
@brief    Sleek dmenu alternative written in Python and powered by curses.
@date     02/08/2023
@author   Julio Cabria
"""


import curses
from contextlib import suppress

MAX_QUERY_LENGTH = 60
PRINTABLE_CHARS = range(32, 127)
ESC = 27


def pmenu(lines):
    """
    Display a menu with the given lines and return the selected option.

    Args:
        lines (list): The lines to display in the menu.

    Returns:
        str: The selected option or None if the user quit the menu.
    """
    try:
        return curses.wrapper(_display_menu, lines)
    except KeyboardInterrupt:
        return None


def _display_menu(stdscr, lines):
    """
    Display a menu with the given lines and return the selected option.
    Don't call this function directly, use curses.wrapper(_display_menu, ...)
    instead.

    Args:
        stdscr (screen): The curses screen.
        lines (list): The lines to display in the menu.

    Returns:
        str: The selected option or None if the user quit the menu.
    """
    curses.curs_set(1)
    curses.use_default_colors()
    curses.set_escdelay(20)

    current_row = 0
    query = ""

    while True:
        stdscr.clear()
        filtered_lines = _filter_lines(lines, query)
        start_row, max_display_rows = _populate_screen(screen=stdscr,
                                                       lines=filtered_lines,
                                                       row=current_row,
                                                       query=query)
        stdscr.refresh()
        key = stdscr.getch()

        if key == ord('\n'):
            with suppress(IndexError):
                return filtered_lines[current_row]

        elif key == curses.KEY_UP:
            if current_row > 0:
                current_row -= 1
            elif start_row > 0:
                start_row -= 1

        elif key == curses.KEY_DOWN:
            if current_row >= len(filtered_lines) - 1:
                continue
            current_row += 1
            if current_row == max_display_rows - 1:
                start_row += 1

        elif key == curses.KEY_BACKSPACE:
            current_row = 0
            query = query[:-1]

        elif key in PRINTABLE_CHARS:
            current_row = 0
            if len(query) < MAX_QUERY_LENGTH:
                query += chr(key)

        elif key == ESC:
            return None


def _filter_lines(lines, query):
    """
    Filter the given lines by the given query.

    Args:
        lines (list): The lines to filter.
        query (str): The query to filter the lines by.

    Returns:
        list: The filtered lines.
    """
    return [line
            for line in lines
            if query.lower() in line.lower()]


def _populate_screen(*, screen, lines, row, query):
    """
    Populate the given screen with the given lines.

    Args:
        screen (screen): The screen to populate.
        lines (list): The lines to populate the screen with.
        row (int): The index of the row to highlight.
        query (str): The query to display.

    Returns:
        tuple: The start row and the max display rows.
    """
    max_rows, _ = screen.getmaxyx()
    max_display_rows = min(max_rows - 1, len(lines))

    start_row = max(0, row - max_display_rows + 1)
    end_row = min(start_row + max_display_rows, len(lines))

    for i, line in enumerate(lines[start_row:end_row], start=start_row):
        with suppress(curses.error):
            if i == row:
                screen.addstr(i - start_row + 1, 0, line, curses.A_REVERSE)
                continue
            screen.addstr(i - start_row + 1, 0, line)

    screen.addstr(0, 0, "[Search]: " + query, curses.A_BOLD)

    return start_row, max_display_rows
