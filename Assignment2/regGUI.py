#!/usr/bin/env python

#-----------------------------------------------------------------------
# regGUI.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from Tkinter import Tk, Frame, Label, N, S, E, W, Entry
from Tkinter import Listbox, Scrollbar, StringVar, END, HORIZONTAL, SINGLE

def main():

	root = Tk()
	root.title('Reg')

	screenWidth = root.winfo_screenwidth()
	screenHeight = root.winfo_screenheight()
	root.geometry('%sx%s' % (screenWidth//2, screenHeight//2))

	
	root.grid_rowconfigure(0, weight = 0)
	root.grid_rowconfigure(1, weight = 1)
	root.grid_columnconfigure(0, weight=1)

	# set up titles for entry values
	labelFrame = Frame(root)

	labelFrame.grid_columnconfigure(0, weight = 0)
	labelFrame.grid_columnconfigure(1, weight = 0)
	labelFrame.grid_columnconfigure(2, weight = 0)
	labelFrame.grid_columnconfigure(3, weight = 1)
	labelFrame.grid_rowconfigure(0, weight = 0)
	labelFrame.grid_rowconfigure(1, weight = 0)

	labelFrame.grid(row = 0, column = 0, sticky = W+E)


	# build up our labels
	deptLabel = Label(labelFrame, text='Department')
	coursenumLabel = Label(labelFrame, text='Course Number')
	areaLabel = Label(labelFrame,text = 'Area')
	titleLabel = Label(labelFrame, anchor = 'w', text = 'Title')

	deptLabel.grid(row = 0, column = 0, sticky=W+E)
	coursenumLabel.grid(row = 0, column = 1, sticky=W+E)
	areaLabel.grid(row = 0, column =2, sticky=W+E)
	titleLabel.grid(row = 0, column = 3, sticky=W+E)

	# build up our input locations
	deptEntry = Entry(labelFrame, width = 4)
	coursenumEntry = Entry(labelFrame, width = 4)
	areaEntry = Entry(labelFrame, width = 4)
	titleEntry = Entry(labelFrame, width = 20)

	# pack em in
	deptEntry.grid(row = 1, column = 0, sticky=W+E)
	coursenumEntry.grid(row = 1, column = 1, sticky = W+E)
	areaEntry.grid(row = 1, column = 2, sticky=W+E)
	titleEntry.grid(row = 1, column = 3, sticky=E+W)

	# add in our scrolling listbox


	def updateListBox(vals, listbox):
		listbox.delete(0, END)
		for x in vals:
			listbox.insert(END, x)

	def genValues(n):
		xyz = []
		for x in range(0, n):
			xyz.append(x)
		return xyz

	listboxFrame = Frame(root)
	listboxFrame.grid_columnconfigure(0, weight = 1)
	listboxFrame.grid_columnconfigure(1, weight =0)
	listboxFrame.grid_rowconfigure(0, weight = 1)
	listboxFrame.grid_rowconfigure(1, weight = 0)
	scrollingListbox = Listbox(listboxFrame, selectmode=SINGLE)
	updateListBox(genValues(1000), scrollingListbox)
	scrollbarV = Scrollbar(listboxFrame, command = scrollingListbox.yview)
	scrollbarH = Scrollbar(listboxFrame, command = scrollingListbox.xview,
		orient = HORIZONTAL)
	scrollingListbox['yscrollcommand'] = scrollbarV.set
	scrollingListbox['xscrollcommand'] = scrollbarH.set
	scrollingListbox.grid(row = 0, column = 0, sticky = N+S+E+W)
	scrollbarH.grid(row=1, column = 0, sticky = E+W)
	scrollbarV.grid(row=0, column=1, sticky =N+S)
	listboxFrame.grid(row=1, column = 0, sticky = N+S+E+W)




	root.mainloop()

if __name__ == '__main__':
	main()