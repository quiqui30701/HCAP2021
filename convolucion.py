import numpy as np

def convolucion(Ioriginal,Kernel):
    fr=len(Ioriginal)-(len(Kernel)-1)
    cr=len(Ioriginal[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr))
    #For para recorrer filas
    for i in range(len(Resultado)):
        #For para recorrer columnas
        for j in range(len(Resultado[0])):
            suma=0
            #hace las multiplicaciones y las sumas
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                    suma+=Kernel[m][n]*Ioriginal[m+i][n+j]
            Resultado[i][j]=suma
    return Resultado
#imagen artificial
K=[[-1,0,1],[-1,0,1],[-1,0,1]]
I=[[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]

#imagenes a numpy array
In=np.array(I)
Kn=np.array(K)

#funcion de convolucion
R=convolucion(In,Kn)
print(R)
