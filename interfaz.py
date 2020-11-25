from tkinter import *
#import analisis_tiempo_real as atr

ventana = Tk()
ventana.title("Afinador")
ventana.geometry("400x400")

v = StringVar()

def apretar():
    lblCuerda = Label(ventana, text="5ta (La) - 110 Hz")
    lblCuerda.pack()
    lblFrecuenciaActual = Label(ventana, text="Frecuencia Actual")
    lblFrecuenciaActual.pack()
    lblNumeroFrecuencia = Label(ventana, text="107.6 Hz")
    lblNumeroFrecuencia.pack()
    lblApretar = Label(ventana, text="Es necesario apretar")
    lblApretar.pack()

def aflojar():
    lblCuerda = Label(ventana, text="5ta (La) - 110 Hz")
    lblCuerda.pack()
    lblFrecuenciaActual = Label(ventana, text="Frecuencia Actual")
    lblFrecuenciaActual.pack()
    lblNumeroFrecuencia = Label(ventana, text="114.6 Hz")
    lblNumeroFrecuencia.pack()
    lblApretar = Label(ventana, text="Es necesario aflojar")
    lblApretar.pack()

def correcta():
    lblCuerda = Label(ventana, text="5ta (La) - 110 Hz")
    lblCuerda.pack()
    lblFrecuenciaActual = Label(ventana, text="Frecuencia Actual")
    lblFrecuenciaActual.pack()
    lblNumeroFrecuencia = Label(ventana, text="110.4 Hz")
    lblNumeroFrecuencia.pack()
    lblApretar = Label(ventana, text="La afinación es correcta")
    lblApretar.pack()


def etiquetas():
    apretar()
    aflojar()
    correcta()

'''lblCuenta = Label(ventana, text="Cuenta:")
lblCuenta.pack()

txtCuenta = Entry(ventana)
txtCuenta.pack()

lblPorcentajePropina = Label(ventana, text="Porcentaje de propina:")
lblPorcentajePropina.pack()

sclPropina = Scale(ventana, from_=0, to_=20, orient=HORIZONTAL)
sclPropina.pack()'''

btnCalcular = Button(ventana, text="Iniciar", command = etiquetas)
btnCalcular.pack()

'''lblTotalAPagar = Label(ventana, text="Total a pagar:")
lblTotalAPagar.pack()

lblMontoTotal = Label(ventana, textvariable=strTotal)
lblMontoTotal.pack()'''

ventana.mainloop()