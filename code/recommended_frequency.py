
def calculate_recommended_frequency(nombre_tours):
    from scipy import interpolate
    file= open('freq', "r")
    line = file.readline()
    line = file.readline()
    x=list()
    y=list()
    a=list()
    i=0
    while line:
        a.append(line)
        x.append(int((a[i].split("/")[0])))
        y.append(int((a[i].split("/")[1])))
        i+=1
        line= file.readline()
        line = file.readline()
        line= file.readline()
        line = file.readline()
    file.close()
    f = interpolate.interp1d(x, y)
    y1 = int(f(nombre_tours)+1)
    return(y1)

def get_speed(nombre_tours):
    file = open("speed" , "r")
    x=list()
    y=list()
    a=list()
    i=0
    line = file.readline()
    while line :
        a.append(line)
        x.append(int((a[i].split(":")[0])))
        if(x[i]==int(nombre_tours)):
            return(int((a[i].split(":")[1]))-6)
        line= file.readline()
        i+=1
    return(1000)
        
            
        
        
    
    

    
    
    

    
    
