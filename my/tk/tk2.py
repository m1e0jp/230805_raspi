# coding= utf-8

import sys
#sys.setdefaultencoding('utf-8')

import tkinter as tk



root = tk.Tk()
root.title("実験")
root.geometry("640x480")
text_widget = tk.Text(root)
text_widget.grid()
get_start = tk.Entry(root)
get_start.grid()



def paint():
	
	s = open('./1.html', 'r')
	f = s.read()
	s.close()

	start = get_start.get()
	judge = start in f
	if judge == False:
		alert = tk.Message(root, text="タグが見つかりません")
		alert.grid()
		return
	startN = f.find(start)
	N = len(start) + 1
	end = f.find('</header>') + N
	moto = text_widget.get('1.0','end-1c')
	change = f[startN:end]
	res = f.replace(change,moto)
	year = open('1.html','w')
	year.write(res)
	year.close()
	

go_button = tk.Button(root,text = 'go', command = paint)
go_button.grid()


root.mainloop()
