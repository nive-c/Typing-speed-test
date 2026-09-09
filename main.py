import curses
from curses import wrapper
import time
import random

def start(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing speed test!")
    stdscr.addstr(1,0,"Press any key to start...")
    stdscr.refresh()
    stdscr.getkey()

def display(stdscr,curr, target, wpm=0):
    stdscr.addstr(target)

    for i, ch in enumerate(curr):
        stdscr.addstr(0,i, ch, curses.color_pair(1) if ch==target[i] else curses.color_pair(2))
    stdscr.addstr(2,0,f"WPM: {wpm}")

def load_text():
    with open("text.txt", "r") as f:
        lines= f.readlines()
    return random.choice(lines).strip()


def func(stdscr):
    standard_text= load_text()
    user_text=[]
    curr_time= time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed= max(time.time() - curr_time, 1)
        wpm= round((len(user_text)/ (time_elapsed/60)) / 5)

        stdscr.clear()
        display(stdscr,user_text,standard_text, wpm)
        stdscr.refresh()

        #.join() is used to convert the list of characters into a single string
        if "".join(user_text) == standard_text:
            stdscr.nodelay(False) #so it wont wait for any key press and just exit
            break

        try:
            key= stdscr.getkey()
        except:
            continue

        if ord(key) == 27: #if the user presses the escape key, exit the loop
            break

        if key in ("BACKSPACE",'\b', '\x7f'):
            if len(user_text) > 0:
                user_text.pop() 
        elif len(user_text) < len(standard_text):
            user_text.append(key)
       

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    start(stdscr)
    while True:
        func(stdscr)
        stdscr.addstr(4,0,"Congratulations! Press any key to try again or ESC to exit.")
        key= stdscr.getkey()

        if ord(key) == 27: #if the user presses the escape key, exit the loop
            break

wrapper(main)