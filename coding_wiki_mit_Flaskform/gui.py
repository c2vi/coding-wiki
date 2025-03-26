

from tkinter import *

window = Tk(baseName = "Test")
window.geometry("900x500+200+200")
window.title("Inserting Items")

menu_frame = Frame(window , bg="green" , height=100 , width=100)
menu_frame.place(relheight=1 , width=200 , anchor=NW)

content_frame = Frame(window , bg="red")
content_frame.place(x=200 , relheight=1 , relwidth=1)

test = Entry(content_frame)

mb_frame = Frame(menu_frame , pady=10 , width=180 , height=44)
mb_frame.place(y=15)

#Menu
types = ["garbige","random - text","random - number"]

l = Label(menu_frame , text="Hey!!")
tb = Button(menu_frame , text="Klick!!" , command=lambda:l.pack(side=BOTTOM , fill=X))
tb.pack(side=BOTTOM , fill=X)


#Quit-Button
qbframe = Frame(menu_frame , height=10)
qbframe.pack(side=BOTTOM, fill=X)
qbutton = Button(menu_frame , bg="blue" , text="Quit" , command=window.quit , width=10)
qbutton.pack(side=BOTTOM , fill=X)

#menu in menubar
menu = Menu(window)
window.config(menu=menu)

sub_menu = Menu(menu)
menu.add_cascade(label="first menu" , menu=sub_menu)

sub_menu.add_command(label="first option" , command=lambda:print("first option"))
sub_menu.add_separator()

window.mainloop()