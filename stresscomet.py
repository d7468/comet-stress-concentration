#stress concentration based on the Comet model 

def stress_concentration (format): 
    
    if format == "square": 
        kt = 300 #MPA
        
    elif format == "rectangular":
            kt = 250 #MPA
            
    elif format == "triangular":
                kt = 200 #MPA
                
    elif format == "circular": 
                    kt = 100 #MPA
                    
    else:
      return None 
                
    return kt



formats = ["square","rectangular","triangular","circular"]
 

for format in formats:
      kt = stress_concentration (format)
    
      print (f"format: {format}")
      print (f"stress concentration: {kt} MPa\n")
