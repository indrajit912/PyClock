# A script to print the current time on the terminal screen.
# Author: Indrajit Ghosh
# Created On: Jun 29, 2024
# 

import os
import shutil
import time

def get_terminal_size():
    # Get the size of the terminal window
    terminal_size = shutil.get_terminal_size()
    return terminal_size.columns, terminal_size.lines

def get_current_time():
    return time.strftime("%I:%M:%S %p")

def print_centered_text(text):
    terminal_width, terminal_height = get_terminal_size()
    text_length = len(text)
    # Calculate the starting position for centering the text horizontally
    start_position_x = (terminal_width - text_length) // 2
    # Calculate the starting position for centering the text vertically
    start_position_y = terminal_height // 2
    # ANSI escape sequences for bold and color (change color as desired)
    styled_text = "\033[1;33m{}\033[0m".format(text)  # Bold yellow text
    # ANSI escape sequences to move cursor to a specific position and print styled text
    print("\033[{};{}H{}".format(start_position_y, start_position_x, styled_text), end="\r")

def main():
    try:
        while True:
            os.system('clear')
            current_time = get_current_time()
            print_centered_text(current_time)
            time.sleep(1)  # Update every second
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
