def molaridad(m, ma, v): #  funcion que calcula la molaridad 
    c = m/(ma*v)
    return c



def presion_gas_ideal(moles, temperatura, volumen): # funcion presion de un gas ideal 
    r = 8.314
    return (moles * r * temperatura) / volumen

print("bienvenido si desea calcular la moralidad ingrese 1, si desea calcular la presion de un gas ideal ingrese 2")
a=input() # lo que entra el usuario 

if a=='1': #el usuario metio 1
    print('ingrese m')
    m=float(input())
    print('ingrese ma')
    ma=float(input())
    print('ingrese v')
    v=float(input())
    m=molaridad(m,ma,v)
    print('la molaridad es:', m)
elif a=='2':
    print('ingrese las moles')
    moles=float(input())
    print('ingrese temperatura')
    temperatura=float(input())
    print('ingrese volumen ')
    volumen=float(input())
    p=presion_gas_ideal(moles, temperatura, volumen)    
    print('la presion del gas ideal es: ',p,'atm')