import tkinter as tk
import os

#The Title frame
class Title(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self)
        self.title["text"] = "QR CODE GENERATOR"
        self.title['justify'] = "center"
        
        self.title['font'] = "Times New Roman",24,"bold"
        
        self.title['bg'] = 'white'
        self.title['pady'] = self.title['pady'] = 34
        self.title['width'] = 30
        self.title['relief'] = 'groove'
        
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
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


#the image display frame
class QRCodeImageShow(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("QR - Code Generator")
        self.geometry("644x644")
        self.minsize(644,644)
        self.maxsize(644,1200)
        self.wm_iconbitmap(os.path.join('static','images','logo.ico'))

if __name__ == '__main__':
    root = Root()
    if not os.path.isdir(os.path.join('qrcode_images')): os.mkdir(os.path.join('qrcode_images'))

    title = Title(master=root)
    app = EntryInput(master=root)
    
    root.mainloop()