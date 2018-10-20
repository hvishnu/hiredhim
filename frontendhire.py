from tkinter import *

root = Tk()
frame = Frame(root, width=500,height=500,background='darkslategray')
frame.pack()



name = Label(root,text = 'Name',background='darkslategray',font='40',fg='white')
percent = Label(root,text = 'Percentage',background='darkslategray',font='40',fg='white')
back = Label(root,text = 'Backlog',background='darkslategray',font='40',fg='white')
intern = Label(root,text = 'Internship',background='darkslategray',font='40',fg='white')
firstround = Label(root,text = 'First Round',background='darkslategray',font='40',fg='white')
commskill = Label(root,text = 'Communication Skill',background='darkslategray',font='40',fg='white')


ename = Entry(root,font=1)
epercent = Entry(root,font=1)
eback = Entry(root,font=1)
eintern = Entry(root,font=1)
efirstround = Entry(root,font=1)
ecommskill = Entry(root,font=1)

b1 = Button(root,text='decision tree',height=2,width=20,bg='palegoldenrod')
b2 = Button(root,text='random forest',height=2,width=20,bg='palegoldenrod')

name.place(x=100,y=100)
percent.place(x=100,y=125)
back.place(x=100,y=150)
intern.place(x=100,y=175)
firstround.place(x=100,y=200)
commskill.place(x=100,y=225)

ename.place(x=300,y=100,height=23,width=150)
epercent.place(x=300,y=125,height=23,width=150)
eback.place(x=300,y=150,height=23,width=150)
eintern.place(x=300,y=175,height=23,width=150)
efirstround.place(x=300,y=200,height=23,width=150)
ecommskill.place(x=300,y=225,height=23,width=150)

b1.place(x=200,y=280)
b2.place(x=200,y=325)


root.mainloop()