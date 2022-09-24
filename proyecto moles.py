def molaridad(m, v): #  funcion que calcula la molaridad 
    c = m/(v)
    return c
def molalidad(moles, kg): #  funcion que calcula la molaridad 
    c = moles/(kg)
    return c


def presion_gas_ideal(moles, temperatura, volumen): # funcion presion de un gas ideal 
    r = 0.08205
    return (moles * r * temperatura) / volumen

print("bienvenido si desea calcular la moralidad digite 1, si desea calcular la presion de un gas ideal digite 2, si desa calcular el volumen digite 3, si desea calcular los moles digite 4, si desa calcular la temperatura digite 5, si desea calcular la molalidad digite 6 ")
a=input() # lo que entra el usuario 

if a=='1': #el usuario metio 1
    print('ingrese moles')
    m=float(input())
    print('ingrese volumen (L)')
    v=float(input())
    m=molaridad(m,v)
    print('la molaridad es:', m)
elif a=='2':
    print('ingrese las moles')
    moles=float(input())
    print('ingrese temperatura (K)')
    temperatura=float(input())
    print('ingrese volumen (L)')
    volumen=float(input())
    p=presion_gas_ideal(moles, temperatura, volumen)    
    print('la presion del gas ideal es: ',p,'atm')
elif a=='6':
    print('ingrese moles de soluto')
    moles=float(input())
    print('ingrese masa del solvente')
    kg=float(input())
    mola=molalidad(moles,kg)
    print('La molalidad es: ', mola)
