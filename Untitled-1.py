from tkinter import *
from tkinter import messagebox as ce

class Aplicacion:
    def __init__(self):
        self.ven = Tk()
        self.ven.title("Ejer2")
        self.ven.geometry("400x400+300+500")
        self.ven.config(bg="blue")

        self.vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        Label(self.ven, text="VOCAL O CONSONANTE", font=("Arial", 14)).place(x=100, y=20)
        Label(self.ven, text="Ingrese una cadena:", font=("Arial", 12)).place(x=20, y=70)

        self.txtCadena = Entry(self.ven, font=("Arial", 14), justify=CENTER)
        self.txtCadena.place(x=20, y=100, width=200)

        self.labelResultado = Label(self.ven, text="Resultado:", font=("Arial", 12))
        self.labelResultado.place(x=20, y=150)

        Button(self.ven, text="Verificar", font=("Arial", 12), fg="white", bg="green", command=self.presionar).place(x=20, y=200)
        Button(self.ven, text="Limpiar", font=("Arial", 12), fg="white", bg="black", command=self.limpiar).place(x=120, y=200)
        Button(self.ven, text="Salir", font=("Arial", 12), fg="white", bg="red", command=self.salir).place(x=220, y=200)
        self.ven.mainloop()
        
        
        

    def presionar(self):
        texto = self.txtCadena.get()
        if len(texto) == 0:
            ce.showinfo("Error", "Ingrese una cadena")
        if texto[0] in self.vocales:
            self.labelResultado.config(text="Es vocal")
        else:
            self.labelResultado.config(text="Es consonante")
        
       
    
    
        
    def limpiar(self):
     self.txtCadena.delete(0, END)
     self.labelResultado.config(text="Resultado:")
      
   
    def salir(self):
     self.ven.destroy()

   
        
app = Aplicacion()