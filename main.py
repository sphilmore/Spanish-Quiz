from tkinter import *

import pandas
import pandas as pd
from PIL import ImageTk, Image
import random
BACKGROUND_COLOR = "#B1DDC6"
rand ={}
words={}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/spanish_words..csv")
    words = original_data.to_dict(orient="records")
else:
    words=data.to_dict(orient="records")
#-----Random Number Generator--------------------------------------------------------------------
def random_card():
    global rand, flip_timer
    window.after_cancel(flip_timer)
    rand = random.choice(words)
    canvas.itemconfig(language_text, text="Spanish", fill="black")
    canvas.itemconfig(word_text, text=f"{rand['Spanish']}", fill="black")
    canvas.itemconfig(back_ground, image=card_front_img)
    flip_timer=window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{rand['English']}", fill="white")
    canvas.itemconfig(back_ground, image=card_back_img)

def is_known():
    words.remove(rand)
    data= pandas.DataFrame(words)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_card()
#-------------------UI DESIGN----------------------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=110, pady=50)
flip_timer= window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = ImageTk.PhotoImage(Image.open("images/card_front.png"))
back_ground=canvas.create_image(400, 270, image=card_front_img)
canvas.grid(column=0, columnspan=3)
language_text = canvas.create_text(400,150, text="",font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400,263, text="",  font=("Ariel", 60, "bold"), )
#------------Back Image-----------------------------------------------------------------------------
card_back_img = ImageTk.PhotoImage(Image.open("images/card_back.png"))
#-----------Buttons---------------------------------------------------------------------------------
wrong_img =ImageTk.PhotoImage(Image.open("images/wrong.png"))
wrong_button = Button(image=wrong_img, highlightthickness=0,command=random_card)
wrong_button.grid(column=0)
wrong_button.config(padx=50, bd=0)
right_img = ImageTk.PhotoImage(Image.open("images/right.png"))
right_button = Button(image=right_img,highlightthickness=0, command=is_known)
right_button.grid(column=2, row=1)
right_button.config(bd=0, padx=50)
random_card()















window.mainloop()