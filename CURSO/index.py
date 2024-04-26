class curso:
    
    def __init__(self):    
     
     self.__notas =[2,4,5,2,3.5,0,1.5,2,5,2.5,3,4.2]
     
     
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
       
    '''def cambairNotas(self):

        # retornar un  metodo '''
    def HayAlgunCinco(self):
        existe = False
        contador =  0
        
        while contador < len(self.__notas) and not existe:
            
            if self.__notas[contador] == 5:
                existe = True
                
            contador += 1
            
        return existe
    
    def HayAlgunCinco2 (self):
        existe = False
        
        for i in range(len(self.__notas)):
            
            if self.__notas[i] == 5:
                existe = True
                
                break
            
        return existe
    
    def HayAlgunCinco3(self):
        existe = False
        
        for nota in self.__notas:
            
            if nota == 5:
                existe = True
                
                break
            
        return existe
    
    def EncontrarTresNotas(self):
        existe = False
        
        for i in range(len(self.__notas)):
            if self.__notas[i] == 1.5:
                self.__notas[i] = 2.5
                
            existe = True
            
            break
        return existe
    
    def EncontrarTresNotasDelValor5(self):
        contador = 0
        
        for i in range(len(self.__notas)):
            if self.__notas[i] == 5.0:
                contador += 1
                if contador == 3:
                    return 1
        
                else:
                
                    return -1
        
    def RemplazarNotas(self):

        for i in range(len(self.__notas)):

            if self.__notas[i] < 3.0 :
                self.__notas[i] == 0.0 

            else:
                return 0
            