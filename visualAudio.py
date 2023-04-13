import Audio
import tkinter as tk
import sys

myWindow = tk.Tk()
numEn = tk.Entry(myWindow, width=10)
numEn.grid(column=1, row=1)
nameEn = tk.Entry(myWindow, width=10)
nameEn.grid(column=2, row=1)


def getNum() -> int:
    if not numEn.get().isdigit():
        from tkinter import messagebox
        messagebox.showinfo('这不是一个数字')

        return 0
    return int(numEn.get())


def getName() -> str:
    return nameEn.get()


myAudio = None


def start():
    myAudio = Audio.Audio(time=getNum(), savePath=getName() + '.wav')
    result = myAudio.startRecord()
    from tkinter import messagebox
    messagebox.showinfo(title='结果',message=result)


numEn.bind('<Return>', getNum)
nameEn.bind('<Return>', getName)
buttonStart = tk.Button(myWindow, text='点击开始录音', command=start)
buttonStart.grid(column=3, row=1)
myWindow.mainloop()
