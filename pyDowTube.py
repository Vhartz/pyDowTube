#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''pyDowTube is a program written in Pyhton that helps you download your favorite YouTube videos,
created with a simple and functional code with an interdisciplinary intention.'''

from tkinter import *
from pytube import YouTube
import os
import time
import subprocess

__title__ = 'pyDowTube'
__version__ = '1.0'
__author__ = 'Vitor Amorim'
__license__ = 'GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007'
__copyright__ = 'Copyright 2019 Vitor Amorim'

root =Tk()
root.geometry("250x130")
root.title('pyDowTube')
root.resizable(False, False)
root.update_idletasks()
root.overrideredirect(FALSE)
#root.update()

label_entry = Label(root, text='Insert the youtube video url', font='Times 11 bold').place(x=30,y=5)
entry_var = StringVar()
entry = Entry(root, width=30, textvariable=entry_var).place(x=35, y=40)

def download():
    url = entry_var.get()
    YouTube('%s' %(url)).streams.first().download()
    print('ok')    
	    
button_download = Button(root, text='Download', font='Arial 10 bold', command= download).place(x=90,y=70)

root.mainloop()
