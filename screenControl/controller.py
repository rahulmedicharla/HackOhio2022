from pynput.mouse import Button, Controller
import time

mouse = Controller()

scroll_constant = 100

#scrolling function
def scroll_up():
    mouse.scroll(0, scroll_constant)

def scroll_down():
    mouse.scroll(0, -scroll_constant)

def change_mouse_pos(mx, my):
    mouse.position = (mx, my)



