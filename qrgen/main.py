import os
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Progressbar

import pyqrcode
from PIL import Image, ImageTk

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(THIS_FOLDER)
qrcodefilename = ""

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
            initialdir = os.path.join(BASE_DIR,'logo'),
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
        self.logobutton = tk.Button(
            self,
            text="Upload Logo", 
            bg='#ebab34',
            font=("Arial",15,"bold"),
            command=self.logoupload
        )

        #Packing the elements in a grid
        self.data.grid(row=0,column = 1, padx=2)
        self.datarentry.grid(row=0,column = 2,padx=2)
        self.logobutton.grid(row=1,column = 1,pady = 2,columnspan=2)        
        self.progress.grid(row=2,column=1,columnspan=2,pady=15)
        self.submit.grid(row=3,column=1,columnspan=2,pady=25,padx=2)

    #QR code generation function
    def gen_qr_code(self):
        global BASE_DIR, qrcodefilename

        self.dataenc = self.datavalue.get()
        
        #Error generation
        if self.dataenc in ('',None): 
            messagebox.showerror('No Data Found!',"No data provided, please try again!")
            return False
        
        #Getting the data
        self.files_logo = os.listdir(os.path.join(BASE_DIR, 'logo'))
        
        self.progress['value'] = 20
        self.update_idletasks()

        #QR code generation
        self.x = datetime.now()
        try:
            self.filename = str(self.x.strftime("%a"))+ str(self.x.strftime("%f")) +  self.dataenc[0] + self.dataenc[1] +".png"
        except:
            self.filename = str(self.x.strftime("%a"))+ str(self.x.strftime("%f")) +  self.dataenc[0] +".png"

        self.progress['value'] = 50
        self.update_idletasks()
        
        self.url = pyqrcode.QRCode(self.dataenc, error='H')
        self.url.png(os.path.join(BASE_DIR, 'qrcode_images', self.filename), scale=10)

        self.progress['value'] = 60
        self.update_idletasks()
        
        self.im = Image.open(os.path.join(BASE_DIR, 'qrcode_images',self.filename))
        self.im = self.im.convert("RGBA")

        self.progress['value'] = 65
        self.update_idletasks()

        if self.logofilepath not in ('',' ',None):
            print(self.logofilepath)
            self.progress['value'] = 80
            self.update_idletasks()

            self.logo1 = Image.open(self.logofilepath)
            self.width, self.height = self.im.size
            
            # How big the logo we want to put in the qr code png
            self.logo_size = 100
            
            self.progress['value'] = 85
            self.update_idletasks()

            # Calculate xmin, ymin, xmax, ymax to put the logo
            self.xmin = self.ymin = int((self.width / 2) - (self.logo_size / 2))
            self.xmax = self.ymax = int((self.width / 2) + (self.logo_size / 2))

            self.region = self.logo1
            self.region = self.region.resize((self.xmax - self.xmin, self.ymax - self.ymin))
            self.im.paste(self.region, (self.xmin, self.ymin, self.xmax, self.ymax))

            self.progress['value'] = 100
            self.update_idletasks()

            self.im.save(os.path.join(BASE_DIR, 'qrcode_images', self.filename), scale=10)
        
        self.progress['value'] = 100
        self.update_idletasks()
        qrcodefilename = self.filename

        tk.Label(
            self, 
            text=f"DRIVE NAME : {BASE_DIR}",
            justify="left",
            font = ("Arial",18),
        ).grid(row=4,column=1,columnspan=2)
        tk.Label(
            self, 
            text="Folder : qrcode_images",
            justify="left",
            font = ("Arial",18),
        ).grid(row=5,column=1,columnspan=2)
        tk.Label(
            self, 
            text=f"Filename of the qrcode : {self.filename}.png",
            justify="left",
            font = ("Arial",18),
        ).grid(row=6,column=1,columnspan=2)

        QRCodeImageShow(master=self.master)


#The image display frame
class QRCodeImageShow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        global qrcodefilename, BASE_DIR
        
        self.master = master
        self.resizable(0,0)
        self.title("QR - Code generated - "+qrcodefilename)
        self.wm_iconbitmap(os.path.join(THIS_FOLDER,'static','images','logo.ico'))
        
        #Packing the Image        
        self.image = Image.open(os.path.join(BASE_DIR, 'qrcode_images',qrcodefilename))
        self.photo = ImageTk.PhotoImage(self.image,
            size=40,
        )
        self.imagelabel = tk.Label(
            self,
            image=self.photo,
        ).grid(row=4,column=2,columnspan=2,pady=25,padx=2)        


#__main__
if __name__ == '__main__':
    root = Root()
    if not os.path.isdir(os.path.join(BASE_DIR,'qrcode_images')): os.mkdir(os.path.join(BASE_DIR,'qrcode_images'))
    if not os.path.isdir(os.path.join(BASE_DIR,'logo')): os.mkdir(os.path.join(BASE_DIR,'logo'))

    title = Title(master=root)
    app = EntryInput(master=root)
    
    root.mainloop()
