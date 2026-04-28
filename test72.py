file=open("beam_data.txt","r") #opening the file

beam_number=1 # take beam number as 1

for line in file: # reading the file line by line
    L,E,I,P= map(float,line.split())  #defining values 

    P=P*1000   # change kN into  N
    E=E*10**9 # change GPa into Pa
    Dmax=(P*(L**3)) / (48*E*I) 
    Smax=(P*L) / (4*I)

    print(f"Beam {beam_number}: Length: {L:.1f} m",end=", ") 
    print(f"Max Deflection: {Dmax:.6f} m",end=", ")
    print(f"Max Bending Stress: {Smax:.2f} Pa")

    beam_number=beam_number+1 

file.close() 