import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from pathlib import Path
import sys

def show_transition(janela, callback):
    if getattr(sys, 'frozen', False):
        Rota = Path(sys._MEIPASS)
    else:
        Rota = Path(__file__).parent.parent

    gif_path = Rota / 'assets' / 'transicao.gif'

    # Garante tamanho correto
    janela.update_idletasks()
    width = janela.winfo_width()
    height = janela.winfo_height()

    img = Image.open(gif_path)

    frames = []
    for frame in ImageSequence.Iterator(img):
        frame = frame.convert("RGBA")
        frame = frame.resize((width, height), Image.Resampling.LANCZOS)
        frames.append(ImageTk.PhotoImage(frame))

    lbl = tk.Label(janela, bd=0)
    lbl.place(x=0, y=0, relwidth=1, relheight=1)

    def animate(counter=0):
        lbl.config(image=frames[counter])
        counter += 1
        if counter < len(frames):
            janela.after(50, animate, counter)
        else:
            lbl.destroy()
            callback()

    animate()