from tkinter import *
import tkinter

# -------------- GLOBALS ---------------------#
AFTER_ID = None
FONT = "Times 16 bold"

window = Tk()
window.title("Disappearing Text")
window.geometry("800x600")
window.grid_columnconfigure(1, weight=2)


# GUI
canvas = Canvas(window, width=700, height=200, border=2, relief=RIDGE)

label = Label(window, text="Start typing!\n If you STOP writing for more than 5 seconds the text will disappear!",
              font=FONT)
label.grid(column=1, row=0, pady=(50, 0))
text_box = Text(window, width=80)
text_box.grid(column=1, row=1)
result = Label(window, text='')
result.grid(column=1, row=2)


# -------------- Functions -------------------#
def handle_keypress(event):
    result.config(text='')
    global AFTER_ID
    window.after_cancel(AFTER_ID)
    AFTER_ID = window.after(5000, save_words)


def save_words():
    num_words = len(text_box.get("1.0", tkinter.END).split())
    text_box.delete("1.0", END)
    result.config(text=f'You got wrote {num_words} words before your work was wiped out.', fg='green', font=FONT)


# Bind keypress event to handle_keypress()
window.bind("<KeyRelease>", handle_keypress)

# First After Method so the ID gets created
AFTER_ID = window.after(5000, save_words)

# Main Loop
window.mainloop()
