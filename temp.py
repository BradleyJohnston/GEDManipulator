# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

f = open(file_path, "r")

isWriting = True
writedata = []
for line in f.readlines():
    buffer = ""
    if line[:6] == "1 EVEN":
        isWriting = False
    if line[:6] == "1 CHAN":
        isWriting = True
    
    if isWriting:
        writedata.append(line)

f.close()
f = open(file_path, "w")

for line in writedata:
    f.write(line)