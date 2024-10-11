class Calculadora():
    def __init__(selft,a,b):
        selft.a=a
        selft.b=b
    def suma(selft):
        return selft.a+selft.b

calculadoraTotal=Calculadora(3,2)
resultado= calculadoraTotal.suma()
print("la suma es: ", resultado)