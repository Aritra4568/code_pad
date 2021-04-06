from tkinter import *
from tkinter import filedialog
from plyer import *
root=Tk()

if __name__ == '__main__':
 	notification.notify(
 	title = "WELCOME TO OMEGA",
 	message ="This a  code editor for beginners.\nWe hope you like it.\nThank you for donloading this editor.",
 	app_icon = "/home/aritra/completed py projects/ico.ico",
 	timeout= 13
 	)

root.geometry("490x635")
root.title("CODE-{PAD}")
p1 = PhotoImage(file = 'icon.png')
root.iconphoto(False, p1)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if open_file is None:
        return
    text=str(entry1.get(1.0,END))
    open_file.write(text)
    open_file.close()

def clear_all():
    entry1.delete(1.0,END)

def open_file():
    file = filedialog.askopenfile(mode='r',defaultextension=[".txt"])
    if file is not None:
        content=file.read()
    entry1.insert(INSERT,content)

def c_a_scr():
    ne = Toplevel()
    ne.title("{note}")
    ne.geometry("300x300")
    entry2=Text(ne,height=16,width=34,wrap=WORD)
    entry2.place(x=10,y=10)
    
b1=Button(root,text="save",command=save_file)
b1.place(x=10,y=10)

b2=Button(root,text="clear",command=clear_all)
b2.place(x=70,y=10)

b3=Button(root, text="open file", command=open_file)
b3.place(x=130,y=10)

b4=Button(root, text="notes", command=c_a_scr)
b4.place(x=417,y=10)

entry1=Text(root,height=33,width=58,wrap=WORD)
entry1.place(x=10,y=50)

root.mainloop()