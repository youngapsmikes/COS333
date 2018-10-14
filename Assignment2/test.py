#!/usr/bin/env python

#-----------------------------------------------------------------------
# messageboxtest.py
# Author: Bob Dondero
#-----------------------------------------------------------------------

from Tkinter import Tk, Button, Text, END
from tkMessageBox import showinfo, INFO

def main():
    
    root = Tk()
    root.title('Message Box Test')

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    root.geometry('%sx%s' % (screenWidth//2, screenHeight//2))
    
    def buttonListener():
        x = "CourseID: aoiaoaid" + "\n" + "Title: adioajdfoiasdj\n \n \n \nfoaidsj\n \n \n \noifjsaodaj\n \n \n \n faoisdjfoiasjdofiasdoifjasiodf jao\n \n \n \n \n \n \n \n \nsdjfioadsjdoiafjsdoifajoidjf"
        showinfo(title='My title', message=x, icon=INFO)        
        
        # For a smaller font, use "detail=" instead of "message="
        
        # Other functions:
        # askokcancel(), askquestion(), askretrycancel(), askyesno(),
        # askyesnocancel(), showerror(), showinfo(), showwarning()
    
        # Other icons: INFO, QUESTION, WARNING
            
    button = Button(root, text='Show Dialog', command=buttonListener)
    button.pack()
    
    text = Text(root, height=10, bg='gray')
    text.pack()

    root.mainloop()
 
if __name__ == '__main__':
    main()