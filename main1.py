import curses
from curses import wrapper
import time

def start(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the typing speed test!")
    stdscr.addstr(1,0,"Choose your song:")
    stdscr.addstr(2,0,"1. Shape of you")
    stdscr.addstr(3,0,"2. Dynamite")
    stdscr.addstr(4,0,"3. Senorita")
    stdscr.addstr(5,0,"4. Believer")
    stdscr.addstr(6,0,"5. Love me like you do")
    stdscr.addstr(7,0,"6. Kadhaippoma")
    stdscr.addstr(8,0,"Enter Your choice: ")
    stdscr.refresh()
    key= stdscr.getkey()
    return key


def display(stdscr,curr, target, wpm=0):
    lines= target.split("\n")
    for i, line in enumerate(lines):
        stdscr.addstr(i,0,line)

    rows, cols = 0, 0
    for i, ch in enumerate(curr):
        if target[i] == "\n":
            rows += 1
            cols = 0
            continue

        stdscr.addstr(rows,cols, ch, curses.color_pair(1) if ch==target[i] else curses.color_pair(2))
        cols += 1
    stdscr.addstr(len(lines)+2,0,f"WPM: {wpm}")


def load_song(choice):
    file_path = f"songs/song{choice}.txt"
    with open(file_path) as f:
        return f.read()


def func(stdscr, choice):
    standard_text= load_song(choice)
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
        if "".join(user_text).rstrip() == standard_text.rstrip():
            stdscr.addstr(len(standard_text.split("\n"))+5,0,"Congratulations! Press any key to try again or ESC to exit.")
            stdscr.nodelay(False) #so it wont wait for any key press and just exit
            break

        try:
            key= stdscr.getkey()
        except:
            continue

        if ord(key) == 27: #if the user presses the escape key, exit the loop
            break

        if key in ("KEY_BACKSPACE",'\b', '\x7f'):
            if len(user_text) > 0:
                user_text.pop()

        elif key in ("\n", "\r", "KEY_ENTER"):
            user_text.append("\n") 

        elif len(user_text) < len(standard_text):
            user_text.append(key)
       

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    while True:
        choice = start(stdscr)
        while choice not in ("1","2","3","4","5","6"):
            choice = start(stdscr)
        func(stdscr,choice)
        key= stdscr.getkey()

        if ord(key) == 27: #if the user presses the escape key, exit the loop
            break

wrapper(main)