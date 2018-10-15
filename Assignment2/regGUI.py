#!/usr/bin/env python

#-----------------------------------------------------------------------
# regGUI.py
# Author: Quinn Donohue
#-----------------------------------------------------------------------

from Tkinter import Tk, Frame, Label, N, S, E, W, Entry
from Tkinter import Listbox, Scrollbar, StringVar, END, HORIZONTAL, SINGLE
from queryClass import Query
from networkHandler import NetworkHandler
from tkMessageBox import showerror, showinfo, ERROR, INFO
import re

def runGUI(networkHandler):

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

	# Set up our string variables
	deptString = StringVar()
	coursenumString = StringVar()
	areaString = StringVar()
	titleString = StringVar()

	# Attach the string variables
	deptEntry['textvariable'] = deptString
	coursenumEntry['textvariable'] = coursenumString
	areaEntry['textvariable'] = areaString
	titleEntry['textvariable'] = titleString

	# Helper function to construct an appropriate string out of
	# our dictionary
	def detailBuilder(dictionary):
		finString = "Course ID: " + dictionary["courseid"][0] + "\n"
		finString += "\n"
		finString += "Days: " + dictionary["days"][0] + "\n"
		finString += "Start time: " + dictionary["starttime"][0] + "\n"
		finString += "End time: " + dictionary["endtime"][0] + "\n"
		finString += "Building: " + dictionary["bldg"][0] + "\n"
		finString += "Room: " + dictionary["roomnum"][0] + "\n"
		finString += "\n"

		for cur in dictionary["deptcoursenum"]:
			finString += "Dept and Number: " + cur + "\n"

		finString += "\n"

		finString += "Area: " + dictionary["area"][0] + "\n"

		finString += "\n"

		finString += "Title: " + dictionary["title"][0] + "\n"

		finString += "\n"

		finString += "Description: " + dictionary["descrip"][0] + "\n"

		finString += "\n"

		finString += "Prerequisites: " + dictionary["prereqs"][0] + "\n"

		finString += "\n"

		for cur in dictionary["profname"]:
			finString += "Professor: " + cur + "\n"

		return finString

	# add in our scrolling listbox
	def updateListBox(vals, listbox):
		listbox.delete(0, END)
		for x in vals:
			listbox.insert(END, x)

	# Handle getting focus in
	def handle_focus(event):
		selection = scrollingListbox.curselection()
		if selection:
			return
		scrollingListbox.selection_set(0)

	def listboxListener(event):
		selection = scrollingListbox.curselection()

		try:
			selected = scrollingListbox.get(selection[0])
		except IndexError:
			# This will only happen if the list box is empty
			return

		classid = int(re.search(r'\d+', selected).group())

		try:
			returndict = networkHandler.searchHandle(classid)
			title = returndict["title"][0]
		except Exception, e:
			showerror(title='Reg Error', message= e, icon=ERROR)
			return

		details = detailBuilder(returndict)
		showinfo(title=title, detail = details, icon=INFO)

	listboxFrame = Frame(root)
	listboxFrame.grid_columnconfigure(0, weight = 1)
	listboxFrame.grid_columnconfigure(1, weight =0)
	listboxFrame.grid_rowconfigure(0, weight = 1)
	listboxFrame.grid_rowconfigure(1, weight = 0)
	scrollingListbox = Listbox(listboxFrame, font = 'TkFixedFont')
	scrollbarV = Scrollbar(listboxFrame, command = scrollingListbox.yview)
	scrollbarH = Scrollbar(listboxFrame, command = scrollingListbox.xview,
		orient = HORIZONTAL)
	scrollingListbox['yscrollcommand'] = scrollbarV.set
	scrollingListbox['xscrollcommand'] = scrollbarH.set
	scrollingListbox.grid(row = 0, column = 0, sticky = N+S+E+W)
	scrollbarH.grid(row=1, column = 0, sticky = E+W)
	scrollbarV.grid(row=0, column=1, sticky =N+S)

	scrollingListbox.bind('<Double-ButtonRelease-1>', listboxListener)
	scrollingListbox.bind('<Key-Return>', listboxListener)
	scrollingListbox.bind('<FocusIn>', handle_focus)

	listboxFrame.grid(row=1, column = 0, sticky = N+S+E+W)


	# Handle generating each entry row:
	# NOTE: B/c our printng out function adds to the end first, we
	# build up our list backwards
	def listGenerator(d):
		formatted = []

		max_len = len(d[d.keys()[0]])

		for i in range(0, max_len):

			formatstr = "{0:6}   {1:5}   {2:5}   {3:4}   {4:}"

			temp = formatstr.format(d["classid"][i], d["dept"][i], 
			d["coursenum"][i], d["area"][i], d["title"][i])

			formatted.append(temp)

		return formatted


	# Handle events for entrys
	def entryListener(event):
		dept = deptString.get()
		coursenum = coursenumString.get()
		area = areaString.get()
		title = titleString.get()

		# create a query
		query = Query(dept, coursenum, area, title)

		try:
			returndict = networkHandler.queryHandle(query)
		except Exception, e:
			showerror(title='Error', message= e, icon=ERROR)
			return

		formatted = listGenerator(returndict)

		updateListBox(formatted, scrollingListbox)


	# bind up our events
	deptEntry.bind('<KeyRelease>', entryListener)
	coursenumEntry.bind('<KeyRelease>', entryListener)
	areaEntry.bind('<KeyRelease>', entryListener)
	titleEntry.bind('<KeyRelease>', entryListener)

	# Fill in the box initially
	query = Query("","","","")

	try:
		returndict = networkHandler.queryHandle(query)
	except Exception, e:
		showerror(title='Error', message= e, icon=ERROR)
		return

	formatted = listGenerator(returndict)

	updateListBox(formatted, scrollingListbox)

	root.mainloop()

if __name__ == '__main__':
	main()