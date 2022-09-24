def molaridad(m, v): #  funcion que calcula la molaridad 
    c = m/(v)
    return c
def presion_gas_ideal(moles, temperatura, volumen): # funcion presion de un gas ideal 
    r = 0.08205
    return (moles * r * temperatura) / volumen
def volumen_gas_ideal(moles, temperatura, presion): # funcion volumen de un gas ideal 
    r = 0.08205
    return (moles * r * temperatura) / presion
def moles_gas_ideal(volumen, temperatura, presion): # funcion moles de un gas ideal 
    r = 0.08205
    return (presion* volumen) / ( r * temperatura)
def temperatura_gas_ideal(moles, presion, volumen): # funcion temperatura de un gas ideal 
    r = 0.08205
    return (presion * volumen ) / (moles * r)
def molalidad(moles, kg): #  funcion que calcula la molaridad 
    c = moles/(kg)
    return c

print("bienvenido si desea calcular la moralidad digite 1, si desea calcular la presion de un gas ideal digite 2, si desa calcular el volumen digite 3, si desea calcular los moles digite 4, si desa calcular la temperatura digite 5 ")
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
elif a=='3':
    print('ingrese las moles')
    moles=float(input())
    print('ingrese temperatura (K)')
    temperatura=float(input())
    print('ingrese presion (atm) ')
    presion=float(input())
    v=volumen_gas_ideal(moles, temperatura, presion)    
    print('El volumen es: ',v,'Litros')
elif a=='4':
    print('ingrese la presion')
    presion=float(input())
    print('ingrese temperatura (K)')
    temperatura=float(input())
    print('ingrese volumen (L) ')
    volumen=float(input())
    m=moles_gas_ideal(volumen, temperatura, presion)    
    print('Las moles son: ',m,)
elif a=='5':
    print('ingrese las moles')
    moles=float(input())
    print('ingrese volumen (L)')
    volumen=float(input())
    print('ingrese presion (atm) ')
    presion=float(input())
    t=temperatura_gas_ideal(moles, presion,volumen)    
    print('La temperatura es: ',t,'K')
elif a=='6':
    print('ingrese moles de soluto')
    moles=float(input())
    print('ingrese masa del solvente')
    kg=float(input())
    mola=molalidad(moles,kg)
    print('La molalidad es: ', mola) 
   
    
