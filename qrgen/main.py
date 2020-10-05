import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#The main root class
class Root(tk.Tk):
    global BASE_DIR
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("QR - Code Generator")
        self.geometry("644x644")
        self.minsize(644,644)
        self.maxsize(644,1200)
        
        self.wm_iconbitmap(os.path.join(BASE_DIR, 'qrgen','static','images','logo.ico'))


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

    def create_widgets(self):
        self.data = tk.Label(
            self, 
            text="Data to be Encoded :",
            justify="left",
            font = ("Arial",18),
        )

        self.datavalue = tk.StringVar()
        self.datarentry = tk.Entry(
            self, 
            textvariable = self.datavalue,
            font = ("Times New Roman",18),
        )
        
        self.data['pady'] = self.data['padx'] = 34

        self.datarentry.pack(side="right")
        self.data.pack(side="left",anchor="w")


#Submit Button frame
class SubmitButton(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        from tkinter.ttk import Progressbar
        
        self.progress = Progressbar(
            self, 
            orient = 'horizontal', 
            length = 500, 
            mode = 'determinate'
        )
        self.submit = tk.Button(
            self,
            text="Generate QR-Code",
            font=("Arial",15,"bold"),
            bg='white',
            command=self.say_hi,
            width=40
        )
        

        self.progress.pack(
            side="top",
            anchor='n',
            padx =34
        )
        self.submit.pack(
            side="bottom",
            anchor='s',
            pady = 25,
            padx =34,
        )
    
    def say_hi(self):
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
    if not os.path.isdir(os.path.join('qrcode_images')): os.mkdir(os.path.join(BASE_DIR,'qrcode_images'))

    title = Title(master=root)
    app = EntryInput(master=root)
    submit = SubmitButton(master=root)
    
    root.mainloop()
