from tkinter import *
class Application:
      def __init__(self, master=None):
            self.widget1 = Frame(master)
            self.widget1.pack()
            self.msg = Label(self.widget1, text="Primeiro widget")
            self.msg.pack ()
root = Tk()
Application(root)
root.mainloop()

texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()