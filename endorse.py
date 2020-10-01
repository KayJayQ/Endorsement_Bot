#!/usr/bin/python
# -*- coding: UTF-8 -*-

import win32con
import win32clipboard as w
import time

def readtxt():
    w.OpenClipboard()
    b=w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return b

def inputtxt(string):
    w.OpenClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,string)
    w.CloseClipboard()

if __name__ == '__main__':
    with open("db.txt",'r',encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()
            while True:
                time.sleep(0.1)
                word = readtxt()
                if word == 'n':
                    break
            time.sleep(0.1)
            inputtxt(line)
