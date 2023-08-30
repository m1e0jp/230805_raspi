import sys
import tkinter

# ウィンドウのタイトル名、幅と高さを設定
root = tkinter.Tk()
root.title("test")
root.geometry("300x150")

# エントリー(テキストボックス)
EditBox = tkinter.Entry(width=30)
EditBox.insert(tkinter.END,"てすと")
EditBox.place(x=60, y=50)

root.mainloop()
