import os
import time as t
import tkinter as tk
def door_01check():
    while True:
        t.sleep(1)
        open("file.file", "w").write("null")
        t.sleep(5)
        open("file.file", "w").write("freddy=on")
        