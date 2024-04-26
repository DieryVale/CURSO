notas =[1,4,5,2,3.5,0,1,3,5,4,3,4.2]
    
contador = 0
        
for i in range(len(notas)):
    if notas[i] == 5.0:
        contador += 1
        if contador == 3:
         
         print(1) 
        
        else:
                
            print(-1) 


print('--------------------------------------')



for i in range(len(notas)):

            if notas[i] < 3 :
                notas[i] = 0.0 
            print(notas[i])

