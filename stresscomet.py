#Concentração de tensões baseado no caso do Comet (avião)

def concentracao_tensoes (formato): 
    
    if formato == "quadrado": 
        kt = 300 #MPA
        
    elif formato == "retangular":
            kt = 250 #MPA
            
    elif formato == "triangular":
                kt = 200 #MPA
                
    elif formato == "circular": 
                    kt = 100 #MPA
                    
    else:
      return None 
                
    return kt



formatos = ["quadrado","retangular","triangular","circular"]
 

for formato in formatos:
      kt = concentracao_tensoes(formato)
    
      print (f"formato: {formato}")
      print (f"concentracao de tensoes: {kt} MPa\n")