import random

def cop(r):#comprobar respuesta
    global cod
    if r==str(cod):
        print("\n\n\n👏👏👏 Felisidades "+jp+" as gando. 👏👏👏\n\n\n")
        return input("¿quieres salir?")
    else:
        global cor
        x=0;mm=""
        while x<len(str(cod)):
            if str(cod)[x]==r[x]:mm+=r[x]
            else:mm+="x"
            x+=1
        cor=mm
        global its
        its-=1
        if its==0:
            print("perdite ...",cod)
            cod=random.randint(1000,9999)
            its=5;cor="xxxx"
            return input("¿quieres salir?")
    return ""
    
itf="""
=====================================
CODE
=====================================
"""
print(itf)
jp="";com="";cor="xxxx";cod=random.randint(1000,9999);its=5
jp=input("Nombre del jugador para inisiar: ")
while com!="x":
    itf="""
    [x]=salir
    
    ¿CUAL ES EL CODIGO?
    ["""+cor+"]    INTENTOS:"+str(its)
    print(itf)
    com=input("->: ")
    if len(com)==4:
        com=cop(com)
    else:print("Escribe bien el codigo")
    if jp=="":com="x"
