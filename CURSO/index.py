class curso:
    
    def __init__(self):    
     
     self.__notas =[3,4,5,2,3.5,0,1,2,5,4,3,4.2]
     
     
    def promedion(self):
        print("Promedion")
        print(self.__notas)
        self.__notas.append(self.__notas.pop(0))
        
        
    '''def Calcularpromedio2(self):
        
        prom = 0
        indice = 0 
        
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        prom += self.__notas[indice]
        indice += 1
        
        return prom/indice'''
   
    def Calcularpromedio3(self):
       
       promedio = 0 
       indice = 0
       
       while( indice < 12):
           
           promedio += self.__nota[indice]
           indice += 1
           
           return promedio / indice
       
    def calcularCuantosAprueban(self):  
                
        contardorNotas = 0 
        indice = 0 
        
        while indice < len(self.__notas):
            if 3 <= self.__notas[indice] <= 5:
                    contardorNotas += 1
            indice += 1
        print("Cantidad de notas que pasan: ", contardorNotas )
       