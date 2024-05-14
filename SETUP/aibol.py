from tkinter import *
import pyttsx3
from tkinter import ttk
from PIL import ImageTk,Image
import webbrowser
import tkinter.scrolledtext as ScrolledText

root = Tk()
root.title("AiBol")
root.geometry("1134x455")
root.configure(bg="white")
root.iconbitmap("mic.ico")


menu1 = Menu(root)
root.config(menu=menu1)

   

Details_menu = Menu(menu1)
menu1.add_command(label="Exit", command=root.quit)

my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

frame1 = Frame(my_notebook, width=1134, height=455, bg="white")
frame2 = Frame(my_notebook, width=1134, height=455, bg="white")
frame3 = Frame(my_notebook, width=1134, height=455, bg="white")
frame4 = Frame(my_notebook, width=1134, height=455, bg="white")


frame1.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)

my_notebook.add(frame1, text="Program")
my_notebook.add(frame2, text="App Details")
my_notebook.add(frame3, text="About")
my_notebook.add(frame4, text="Developer Contact")


label8 = Label(frame3, text="AiBol is a Text-to-Speech program created by Pankaj Prajapati", fg="black", bg="white", font=("Arial", 20))
label8.pack()
label9 = Label(frame3, text="It is coded in Python Tkinter", fg="black", bg="white", font=("Arial", 20))
label9.pack()
label10 = Label(frame3, text="By using this program you can convert the text written into speech by the programmed voice.", fg="black", bg="white", font=("Arial", 20))
label10.pack()


label1 = Label(frame1, text="Welcome to AiBol", fg="black", bg="white", font=("Arial", 30) )
label1.pack()

label2 = Label(frame1, text="Write anything below", fg="black", bg="white", font=("Arial", 10))
label2.pack()

def talk():
        engine = pyttsx3.init()
        engine.setProperty('rate', 100)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text1.get())
        engine.runAndWait()
        text1.delete(0,END)
        
    



text1 = Entry(frame1, font=("Arial", 20))
text1.pack()
button1 = Button(frame1, text="Speak", bg="white", fg="black", padx=10, pady=10, font=('Arial', 10), command=talk)
button1.pack(pady=20)
    

button2 = Button(frame1, text="Exit", bg="white", fg="black", padx=10, pady=10, font=('Arial', 10), command=root.quit)
button2.pack(pady=20)
   
label3 = Label(frame2, text="App Details", bg="white", fg="black", font=("Arial", 30))
label3.pack()

label4 = Label(frame2, text="Version - 1.1.0", bg="white", fg="black", font=("Arial", 20))
label4.pack()

label5 = Label(frame2, text="Python Version - Python 3", bg="white", fg="black", font=("Arial", 20))
label5.pack()




label7 = Label(frame2, text="Python Modules", bg="white", fg="black", font=("Arial", 20))
label7.pack()

label11 = Label(frame4, text="Developer : Pankaj Prajapati", bg="white", fg="black", font=("Arial", 20))
label11.pack()

label12 = Label(frame4, text="Email : prfsr04@gmail.com", bg="white", fg="black", font=("Arial", 20))
label12.pack()

def github():
    webbrowser.open("https://github.com/profe5sor")


button5 = Button(frame4, text="Github", bg="white",padx=10, pady=10, fg="black", font=("Arial", 10), command=github)
button5.pack()


my_listbox = Listbox(frame2, font=("Arial", 10))
my_listbox.pack()

my_listbox.insert(END, "Tkinter")
my_listbox.insert(END, "pyttsx3")
my_listbox.insert(END, "webbrowser")
my_listbox.insert(END, "ttk")




root.mainloop()
