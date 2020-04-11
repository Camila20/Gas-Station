


#Los argumentos A y B deben tener el mismo tamaño
def funcion(A,B):
    N=len(A)
    Ac=A[:]     # Copia de A
    Bc=B[:]     # Copia de B
    Tank=0
    Requeried=0
    i=0
    while True:
        try:
            if B[i]<=A[i]:      # Si el combustible requerido es menor que el que se tiene
                index=i
                break           # No se continúa buscando una posición
            else:               # Si el combustible requerido es mayor que el que se tiene
                Ac+=[Ac.pop(i)] # Se mueve el elemnto de la posición i hacia el final
                Bc+=[Bc.pop(i)]
                i+=1
        except IndexError:      # No hay más valores
            index=-1            # El retorno será -1
            return index
            break
    for j in range(N):          # Se completa casi una vuelta
        Tank+=Ac[i]             
        Requeried=Bc[i]
        Tank-=Requeried
        if Requeried>Tank:      # Si no hay suficiente gas para avanzar se retorna -1
            break
            print ("error")
    Tank+=Ac[0]
    if Tank-Bc[0]>=0:       # Vuelta que completa el recorrido
        index=i
    return index            # Se retornará la posición esde la cual se empezó

print (funcion([1,2],[2,1]))


