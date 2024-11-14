'''INTELIGENTIA - CÓMO USAR CLASS, SELF, __INIT__'''

'''EJERCICIO PRÁCTICO - Inmobiliaria'''

'''
PRIMERA PARTE: COMO HACERLO MAL
Tenemos una inmobiliaria y queremos hacer una aplicación con los pisos que tenemos en venta
Vamos a asignarle a cada apartamento, su piso, sus metros, su orientación, su precio y si está o no vendido.

#APARTAMENTO 1
apartamento_1_precio = 120000
apartamento_1_metros = 150
apartamento_1_orientacion = "Sur"
apartamento_1_piso = 1
apartamento_1_vendido = False

#APARTAMENTO_2
apartamento_2_precio = 120000
apartamento_2_metros = 150
apartamento_2_orientacion = "Sur"
apartamento_2_piso = 1
apartamento_2_vendido = False

apartamento_1 =[apartamento_1_metros, apartamento_1_piso....]'''

'''
SEGUNDA PARTE: COMO HACERLO CON CLASES Y EL MÉTODO SELF
Si tenemos 50 apartamentos, la cosa se nos complica.
Self lo que hace es darle atributos a cada variable.
Los elementos que queramos, por ejemplo los mismos. Primero sin el self


class Apartamento():
    metros = 150
    piso = 1
    orientacion = "Sur"
    precio = 150000
    vendido = False

apartamento_1 = Apartamento()
print(apartamento_1.metros, apartamento_1.vendido)
apartamento_2 = Apartamento()
print(apartamento_2.metros)
apartamento_2.metros = 200
print(apartamento_2.metros)'''

'''
TERCERA PARTE: EL MÉTODO SELF
Ahora lo que vamos a hacer es cambiar nuestra clase para que cada apartamento sea diferente.
Podremos asignar valores directamente a cada apartamento.
No pasa como atributo, podemos pasar cualquier cosa, pero tiene que ser acorde a lo que haya dentro de la función.
Cada función tiene su propio self, que es diferente. Por eso puedes cambiarlo
'''

class Apartamento():
    def __init__(self, metros, piso, orientacion,precio,vendido):
        self.metros = metros
        self.piso = piso
        self.orientacion = orientacion
        self.precio = precio
        self.vendido = vendido

apartamento_1 = Apartamento(150,1,"Sur",150000,False)
print(apartamento_1.metros)
apartamento_2 = Apartamento(120,2,"Norte",230000,True)


