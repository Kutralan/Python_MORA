import math 
def analyseSeriesCircuit(k,series_output): 
    
    for i in range(len(k)): 
          R=float(k[i][1]) 
          L=float(k[i][2]) 
          C=float(k[i][3]) 
          V=float(k[i][4]) 
          F=float(k[i][5]) 
          
          ZL=2*math.pi*F*L*0.001 #inductive reactance
          ZC=(1/(2*math.pi*F*C*0.000001)) #capacitive reactance
          ZT=(math.sqrt(R**2 + (ZL-ZC)**2)) #total impedance
          A =(V/ZT) if ZT != 0 else 0 #current
          PHI =math.degrees(math.atan((ZL-ZC)/R)) if R != 0 else 0 #phase angle
          series_output.append([round(ZL,1),round(ZC,1),round(ZT,1),round(A,1),round(PHI,1)]) #store result
  
def analyseParallelCircuit(k,parallel_output): 
   
    for i in range(len(k)): #loop through circuits
          R=float(k[i][1]) 
          L=float(k[i][2]) 
          C=float(k[i][3]) 
          V=float(k[i][4]) 
          F=float(k[i][5]) 
          
          ZL=2*math.pi*F*L*0.001 
          ZC=(1/(2*math.pi*F*C*0.000001)) 
          if ZL != 0 and ZC != 0 and R != 0: #check valid values
            ZT_ = math.sqrt((1/R**2) + (((1/ZL)-(1/ZC))**2)) #reciprocal impedance
            ZT = 1/ZT_ # total impedance 
            PHI= math.degrees(math.atan(((1/ZL)-(1/ZC))*R)) 
          else:
            ZT = 0
            PHI = 0
          A = (V/ZT) if ZT != 0 else 0 
          
          parallel_output.append([round(ZL,1),round(ZC,1),round(ZT,1),round(A,1),round(PHI,1)])
filename=input()
no_of_circuits=[]
with open(filename) as file: 
    for line in file:
        data=line.split() 
        no_of_circuits.append(data)
series_circuits=[] 
parallel_circuits=[]      
for i in range(len(no_of_circuits)):
    if no_of_circuits[i][0]=="series": #filter series
        series_circuits.append(no_of_circuits[i])
for i in range(len(no_of_circuits)):
    if no_of_circuits[i][0]=="parallel": #filter parallel
        parallel_circuits.append(no_of_circuits[i])

series_output=[]    
parallel_output=[]
analyseSeriesCircuit(series_circuits,series_output) #analyse series
analyseParallelCircuit(parallel_circuits,parallel_output) #analyse parallel
result=[]
s=0
p=0
for i in range(len(no_of_circuits)):
    
    if no_of_circuits[i][0]=="series": #maintain order
        result.append(series_output[s])
        s=s+1
        
    else:
        result.append(parallel_output[p])
        p=p+1


with open("result.txt", "w") as f:
    for row in result:
        f.write(" ".join(map(str, row)) + "\n")    