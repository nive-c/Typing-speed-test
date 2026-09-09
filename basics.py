import curses
from curses import wrapper

def main(stdscr): #standard screen
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)#initialize color pair 1 with green text and black background
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear() #clear the screen before  wrriting or there maybe some junk
    stdscr.addstr("Hello world!", curses.color_pair(2)) #use the initialized color here
    stdscr.addstr(1,4,"Hello") # 1-row, 4-col so it will be on the next line with indentation
    stdscr.refresh()
    key=stdscr.getkey() #wait for user input and store it in the variable key

wrapper(main)#this will call the main function and pass the standard screen to it, allowing us to use curses functions within main.