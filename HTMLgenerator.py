'''
Copyright Lucas Percereau -> lucas.percereau@gmail.com
'''

'''Imports'''
from functools import partial
from tkinter import *
from PIL import Image, ImageTk

'''Variables'''
index = 2

element = []
type = []
''''''

'''FONCTIONS'''
def generateHTML():
    str = ""
    for i in range(len(element)):
        if type[i] == "P":
            str += "<p>"+element[i].get("1.0",'end-1c')+"</p>"+'\n'
        if type[i] == "S":
            str += "<p class=\"link\">Sitographie  : <a target=\"_blank\" href=\""+element[i].get("1.0",'end-1c')+"\">test</a></p>"+'\n'
        if type[i] == "H2":
            str += "<h2>" + element[i].get("1.0", 'end-1c') + "</h2>"+'\n'
        if type[i] == "H4":
            str += "<h4>" + element[i].get("1.0", 'end-1c') + "</h4>"+'\n'
        if type[i] == "H6":
            str += "<h6>" + element[i].get("1.0", 'end-1c') + "</h6>"+'\n'
        if type[i] == "Sign":
            str += "<br /><div class=\"signature\">-- "+element[i].get("1.0", 'end-1c')+"</div>"+'\n'
        if type[i] == "image":
            strFull = element[i].get("1.0", 'end-1c').split("%")
            str += "<img class=\"img_article\" src=\"../ressources/images/pop/"+numeroEdition.get("1.0", 'end-1c')+"/"+strFull[0]+"\""+" alt=\""+strFull[1]+"\">"+'\n'
        if type[i] == "legende":
            str += "<div class=\"legende\">"+element[i].get("1.0", 'end-1c')+"</div>"+'\n'
        if type[i] == "hrow":
            str += "<br /><hr style=\"background:#004875;\"><br />"+'\n'

    f = open("articleGenerated.html", "w")
    f.write(str)
    f.close()

def addParagraphe():
    global index
    text = Text(frame, height=10, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    element.append(text)
    type.append("P")
    label = Label(frame, text='Paragraphe : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addSitographie():
    global index
    text = Text(frame, height=5, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    element.append(text)
    type.append("S")
    label = Label(frame, text='Sitographie : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addH2():
    global index
    text = Text(frame, height=1, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    element.append(text)
    type.append("H2")
    label = Label(frame, text='Titre H2 : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addH4():
    global index
    text = Text(frame, height=1, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    element.append(text)
    type.append("H4")
    label = Label(frame, text='Titre H4 : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addH6():
    global index
    text = Text(frame, height=1, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    element.append(text)
    type.append("H6")
    label = Label(frame, text='Titre H6 : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addSignature():
    global index
    text = Text(frame, height=1, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    element.append(text)
    type.append("Sign")
    label = Label(frame, text='Signature : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addHrow():
    global index
    text = Text(frame, height=1, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    text.insert(1.0, "NOTHING TO WRITE HERE, JUST AN HORIZONTAL ROW :D !")
    element.append(text)
    type.append("Sign")
    label = Label(frame, text='H row : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addImageSimple():
    global index
    text = Text(frame, height=1, width=150,padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    text.insert(1.0, "nom_image%description_image")
    element.append(text)
    type.append("image")
    label = Label(frame, text='Image path : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index,rowspan =3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def addLegende():
    global index
    text = Text(frame, height=1, width=150, padx="5", pady="5")
    text.configure(bg="#FDF5E6")
    element.append(text)
    type.append("legende")
    label = Label(frame, text='Legende : ')
    label.configure(bg='#E8927C')
    text.grid(column=1, row=index, rowspan=3)
    label.grid(column=0, row=index)

    index += 3
    replaceButton()

def replaceButton():
    global index
    buttonH2.grid(column=2, row=index)
    buttonH4.grid(column=2, row=index + 1)
    buttonSitographie.grid(column=2, row=index + 2)
    buttonH6.grid(column=3, row=index)
    buttonParagraphe.grid(column=3, row=index + 1)
    buttonSignature.grid(column=3, row=index + 2)
    buttonGenerate.grid(column=1, row=index + 1)
    buttonImage.grid(column=2, row=index+3)
    buttonLegende.grid(column=3, row=index+3)
    buttonHrow.grid(column=2, row=index+4)
    updateScrollRegion()

def updateScrollRegion():
    canvas.update_idletasks()
    canvas.config(scrollregion=frame.bbox())
    canvas.yview_moveto(1)

def mouse_wheel(event):
    direction = 0
    if event.num == 5 or event.delta == -120:
        direction = 1
    if event.num == 4 or event.delta == 120:
        direction = -1
    canvas.yview_scroll(direction, UNITS)

def clearTextBox(event):
    numeroEdition.delete('1.0', END)
    numeroEdition.unbind("<Button-1>")

'''CREATION FENETRE'''
root = Tk()
root.title("HTML GENERATOR")
root.geometry("1600x900")
root.bind("<MouseWheel>", mouse_wheel)
root.bind('<Button-4>', mouse_wheel)
root.bind('<Button-5>', mouse_wheel)
''''''

'''FRAME AND CANVAS FOR SCROLLING'''
canvas = Canvas(root)
frame = Frame(canvas)
canvas.configure(bg='#004875')
frame.configure(bg='#004875')
scrollbar = Scrollbar(root)

canvas.config(yscrollcommand=scrollbar.set, highlightthickness=0)
canvas.configure(yscrollincrement='30')
scrollbar.config(orient=VERTICAL, command=canvas.yview)
scrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
canvas.pack(fill=BOTH, side=LEFT, expand=TRUE)
canvas.create_window(0, 0, window=frame, anchor=NW)
''''''

'''WIDGET'''
labelTitle = Label(frame, text='HTML GENERATOR',pady=10,padx=30)
labelTitle.configure(bg='#E8927C')

numeroEdition = Text(frame, height=1, width=10,padx="5", pady="5")
numeroEdition.insert(1.0,"Edition N°")
numeroEdition.bind("<Button-1>", clearTextBox)


load = Image.open("logoMedium.png")
render = ImageTk.PhotoImage(load)
img = Label(frame, image=render)
img.configure(bg='#004875')
img.image = render

load2 = Image.open("logoPolytechMedium.png")
render2 = ImageTk.PhotoImage(load2)
img2 = Label(frame, image=render2)
img2.configure(bg='#004875')
img2.image = render2

buttonH2 = Button(frame, text='+Titre H2', command=partial(addH2))
buttonH2.configure(bg='#E8927C')
buttonH4 = Button(frame, text='+Titre H4', command=partial(addH4))
buttonH4.configure(bg='#E8927C')
buttonH6 = Button(frame, text='+Titre H6', command=partial(addH6))
buttonH6.configure(bg='#E8927C')
buttonParagraphe = Button(frame, text='+Paragraphe', command=partial(addParagraphe))
buttonParagraphe.configure(bg='#E8927C')
buttonSitographie = Button(frame, text='+Sitographie', command=partial(addSitographie))
buttonSitographie.configure(bg='#E8927C')
buttonSignature = Button(frame, text='+Signature',command=partial(addSignature))
buttonSignature.configure(bg='#E8927C')
buttonImage = Button(frame, text='+Image simple',command=partial(addImageSimple))
buttonImage.configure(bg='#E8927C')
buttonLegende = Button(frame, text='+Legende',command=partial(addLegende))
buttonLegende.configure(bg='#E8927C')
buttonHrow= Button(frame, text='+H row',command=partial(addHrow))
buttonHrow.configure(bg='#E8927C')

buttonGenerate = Button(frame, text='Generate', command=partial(generateHTML),padx=50)
buttonGenerate.configure(bg='#E8927C')
''''''

'''Grid'''
labelTitle.grid(column=1, row=0)

numeroEdition.grid(column=1, row=1)

img.grid(column=0, row=0,rowspan =2)
img2.grid(column=2, row=0,columnspan =2,rowspan =2)

buttonH2.grid(column=1, row=2)
buttonH4.grid(column=1, row=3)
buttonH6.grid(column=1, row=4)
buttonParagraphe.grid(column=1, row=5)
buttonSitographie.grid(column=1, row=6)
buttonSignature.grid(column=1, row=7)
buttonImage.grid(column=1, row=8)
buttonLegende.grid(column=1, row=9)
buttonHrow.grid(column=1, row=10)

buttonGenerate.grid(column=1, row=11)

root.mainloop()
''''''
