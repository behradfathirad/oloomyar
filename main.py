#درست شده توسط بهراد فتحی راد و امین بزرگ زاده
#در مدرسه ی شاهد امام رضا

from cProfile import label
from cgitb import text
from tkinter import *
from tkinter import messagebox
import tkinter
from tkinter import ttk
#-----------------------#
def ghalat():
    tkinter.messagebox.showerror(title="ghalat!", message="جواب شما نادرست است")
#-----------------------#
def dorost():
    tkinter.messagebox.showinfo(title="doroste!", message="افرین درست بود")
#-----------------------#
root = Tk()
root.title("oloomyar")
root.geometry("400x300")
# Add image file
bg = PhotoImage(file = "oloom.png")

# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 50, y = 100)

label2 = Label( root, text = r"به بازی علوم یار خوش امیدید نسخه ی 1 علوم هفتم")
label2.pack(pady = 50)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )
#---------------------------#
def level_1_test_1(): 
    root.destroy()
    root_2 = Tk()
    root_2.title("oloomyar")
    root_2.geometry("800x600")
    Label( root_2, text = r"غار های آهکی چگونه تشکیل میشوند؟").pack(pady=20)
    #---------------------------------#
    def level_1_test_2():

        root_2.destroy()     
        root_3 = Tk()
        root_3.geometry("800x600")
        root_3.title("oolomyar")
        
        dorost()

        Label(root_3, text="آب های زیر زمینی چگونه تشکیل میشوند؟").pack(pady=20)
        Label(root_3, text="وقتی باران میبارد ")   



        root_3.mainloop()
    #----------------------------------#
    bg2 = PhotoImage(file = "غار های اهکی.png")
    
    label3 = Label( root_2, image = bg2)
    label3.place(x = 50, y = 200)
    
    Label( root_2, text = r"الف: غار های طبیعی بر اثر گرمای زیاد به وجود می آید ").pack(pady=20)
    Label( root_2, text = r"وقتی آب اهی زیر زمینی به سنگ های آهکی میرسند فضای خالی ایجاد میشود و غار های اهکی ایجاد میشوند").pack(pady=20)
    Label( root_2, text = r"پ: هیچ کدام").pack(pady=20)

    ttk.Button(root_2, text= "الف", command= ghalat).pack(pady=20)
    ttk.Button(root_2, text= "ب", command= level_1_test_2).pack(pady=20)
    ttk.Button(root_2, text="پ", command=ghalat).pack(pady=20)


    root_2.mainloop()

#---------------------------#
# Add buttons
button1 = Button(frame1,text="شروع", command= level_1_test_1)
button1.pack(pady=20)
#-----bastan ba docmeh-----#
def des():
    root.destroy()
#--------------------------#
button2 = Button( frame1, text = "خروج", command= des)
button2.pack(pady = 20)
#---------------------------#
root.mainloop()
