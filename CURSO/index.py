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
                break
            
    def CalcularnumeroMinimoNotas(self):

        sumarNotas = 0 
        contador = 0 
        
        for i in range(len(self.__notas)):
                    sumarNotas += self.__notas[i]
                    contador += 1
                    if sumarNotas >  30:
                            return contador
                    
                    else:
                      return -1
    
    def cambairNotas(self): 
        for i in range(len(self.__notas)):
            if self.__notas[i] > 4.0 :
                self.__notas[i] -= self.__notas[i] * 0.05

            elif self.__notas[i] < 2.0:
                self.__notas[i] += self.__notas[i] *0.5

        return self.__notas
    
    def darMenorNota(self):
         menorNota = self.__notas[0]

         for nota in self.__notas:         
             if nota < menorNota:
                nota = menorNota
         return menorNota
                    

    def darRangoConMasNotas(self):
        rango1 = 0
        rango2 = 0
        rango3 = 0

        for nota in self.__notas:
            if nota >= 0.0 and nota < 1.99:
                rango1 += 1 
            elif nota >= 2.0 and nota < 3.49:
                 rango2 += 1 
            elif nota >= 3.5 and nota <= 5.0:
                rango3 += 1 

        if rango1 < rango2 and rango1 > rango3:
            return 1
        if rango2 < rango1 and rango2 > rango3:
            return 2
        else:
            return 3