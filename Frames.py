# this python code is to illustrate about frames in python using customtkinter.
import customtkinter
import tkinter
app=customtkinter.CTk()

# initials
app.geometry('720x360')
app.title("Frames")
app._set_appearance_mode("light")

# main code

#function defination
def click(txt):
    txt=str(e.get())
    l.configure(master=frame,text=txt)
    #l.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER,x=20,y=60)
    l.pack(padx=30,pady=30)
    l._set_appearance_mode('light')
    print("text is configured!")

def clear(label):
    label.configure(master=frame,text="")
    print("Text is cleared")
# frame defination
frame = customtkinter.CTkFrame(master=app,
                               width=500,
                               height=300,
                               corner_radius=40)
#frame.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER)
frame.pack(padx=10,pady=10)
frame._set_appearance_mode("light")

# elements in the frames
e=customtkinter.CTkEntry(master=frame,width=200,height=25,corner_radius=10,placeholder_text="Enter text")
#e.place(relx=0.4, rely=0.5,anchor=tkinter.CENTER,x=20,y=20)
e.pack(padx=10,pady=10)
e._set_appearance_mode('light')

# button defination
# submit button
subbtn=customtkinter.CTkButton(master=app,text="Submit",command=lambda:click(e.get()))
#btn.place(relx=0.5, rely=0.5,anchor=tkinter.CENTER,x=20,y=40)
subbtn._set_appearance_mode('light')
subbtn.pack(padx=20,pady=20)

# clear button
clrbtn=customtkinter.CTkButton(master=app,text="Clear",command=lambda:clear(l))
clrbtn._set_appearance_mode('light')
clrbtn.pack(padx=40,pady=20)

l=customtkinter.CTkLabel(master=frame,text="")
l.pack(padx=30,pady=30)
l._set_appearance_mode('light')
# mainloop
app.mainloop()