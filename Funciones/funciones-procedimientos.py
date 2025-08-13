"""
funciones = siempre devuelve un valor (return)
precedimiento = No devuelve un valor
scope = Es el alacance que tiene una cariable dentro del codigo
"""
#Variable global
name = "Alexander"

def saludo():
    global name
    
    print(name)

saludo()