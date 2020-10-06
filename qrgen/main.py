import os
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Progressbar

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

#The main root class
class Root(tk.Tk):
    global THIS_FOLDER
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("QR - Code Generator")
        self.geometry("644x644")
        self.minsize(644,644)
        self.maxsize(644,1200)
        
        self.wm_iconbitmap(os.path.join(THIS_FOLDER,'static','images','logo.ico'))


#The Title frame
class Title(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(
            self,
            text = "QR CODE GENERATOR",
            justify = "center",
            font = ("Times New Roman",24,"bold"),
            bg = 'white',
            width = 30,
            relief = 'groove'
        )                
        self.title['pady'] = self.title['pady'] = 34
        
        self.title.pack(
            side='top',
            anchor='n', 
            fill='x',
            expand=True
        )


#Input area frame
class EntryInput(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.logofilepath = ""
    
    #Choosing the image
    def logoupload(self):
        global THIS_FOLDER
        self.logofilepath = askopenfilename(
            initialdir = os.path.join(os.path.dirname(THIS_FOLDER),'logo'),
            title = "choose your image file",
            filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
        )

    def create_widgets(self):
        #Label the dataentry
        self.data = tk.Label(
            self, 
            text="Data to be Encoded :",
            justify="left",
            font = ("Arial",18),
        )

        #Progressbar to track the progress
        self.progress = Progressbar(
            self, 
            orient = 'horizontal', 
            length = 500, 
            mode = 'determinate'
        )

        #Submit button
        self.submit = tk.Button(
            self,
            text="Generate QR-Code",
            font=("Arial",15,"bold"),
            bg='#ebab34',
            command=self.gen_qr_code,
            width=40,
        )

        #Initialisation of Tkinter Variables
        self.datavalue = tk.StringVar()
        self.logo = tk.IntVar()
        
        #Entry widget of the tkinter
        self.datarentry = tk.Entry(
            self, 
            textvariable = self.datavalue,
            font = ("Times New Roman",18),
        )
        self.data['height'] = 4

        #Checkbox for the center logo
        self.logocheckbox = tk.Checkbutton(
            self,
            text="Want to put the logo at center?", 
            variable = self.logo,
            highlightcolor='#ebab34',
            font=("Arial",15,"bold"),
            command=self.logoupload
        )

        #Packing the elements in a grid
        self.data.grid(row=0,column = 1, padx=2)
        self.datarentry.grid(row=0,column = 2,padx=2)
        self.logocheckbox.grid(row=1,column = 1,pady = 2,columnspan=2)        
        self.progress.grid(row=2,column=1,columnspan=2)
        self.submit.grid(row=3,column=1,columnspan=2,pady=25,padx=2)

    #Qrcode generation function
    def gen_qr_code(self):
        import pyqrcode
        print(self.logofilepath)

        #Getting the data
        title = self.datavalue.get()
        files_logo = os.listdir(os.path.join(os.path.dirname(THIS_FOLDER), 'logo'))
        
        #Error generation
        if title in ('',None): 
            messagebox.showerror('No Data Found!!!',"No data was given in order to get encoded, so please try again!!!")
            return False
        
        self.progress['value'] = 20
        self.update_idletasks()


#the Image display frame
class QRCodeImageShow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


#__main__
if __name__ == '__main__':
    root = Root()
    if not os.path.isdir(os.path.join('qrcode_images')): os.mkdir(os.path.join(THIS_FOLDER,'qrcode_images'))

    title = Title(master=root)
    app = EntryInput(master=root)
    
    root.mainloop()
