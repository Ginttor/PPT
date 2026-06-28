import random

def ia():   #ia del juego
    return str(random.randint(1, 3))
def ga(j,i):#comprobar resultados
    jj="";ii=""
    if   j=="1":jj="✊"
    elif j=="2":jj="✋"
    elif j=="3":jj="✌️"
    if   i=="1":ii="✊"
    elif i=="2":ii="✋"
    elif i=="3":ii="✌️"
    itf="IA    vs    "+jp
    print(itf)
    if   j==i:print(ii+"**EMPATE**"+jj)
    elif i=="1" and j=="2":print(ii+"   GANA-->"+jj)
    elif i=="1" and j=="3":print(ii+"<--GANA   "+jj)
    elif i=="2" and j=="1":print(ii+"<--GANA   "+jj)
    elif i=="2" and j=="3":print(ii+"   GANA-->"+jj)
    elif i=="3" and j=="1":print(ii+"   GANA-->"+jj)
    elif i=="3" and j=="2":print(ii+"<--GANA   "+jj)
    else:print("%%% JUGADA IMBALIDA %%%")

itf="""
=====================================
*--\     "     *--\     "     *-----*
|  |     "     |  |     "        |
|--/     "     |--/     "        |
|        "     |        "        |
|        "     |        "        |
=====================================
"""
print(itf)
jp="";com=""
jp=input("Nombre del jugador para inisiar: ")
while com!="x":
    itf="""
    [x]:salir
    
       **ESCOGE**
    +-(1)-(2)-(3)-+
    | ✊  ✋  ✌️  |
    +-------------+
    """
    print(itf)
    com=input("->: ")
    ga(com,ia())
    if jp=="":com="x"
    print("+----------------------------------------------------------------------------+")
    com=input("¿salir?")
