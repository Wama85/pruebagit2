class Calculadora():
    def __init__(selft,a,b):
        selft.a=a
        selft.b=b
    def suma(selft):
        return selft.a+selft.b
    def resta(self ):
        return self.a-self.b

calculadoraTotal=Calculadora(3,2)
resultadoSuma= calculadoraTotal.suma()
resultadoResta=calculadoraTotal.resta()
print("la suma es: ", resultadoSuma)
print("La resta es: ", resultadoResta)