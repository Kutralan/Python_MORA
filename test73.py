import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
################################################################################
# Please do not edit anything above this line.


# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    with open(file_name,"r") as file:  #opening the file
        for line in file: # reading line by line
            values=line.split() 
            speed.append(int(values[1]))   #second column=speed    (appending those values to the list)
    
################## YOUR CODE ENDS HERE. ########################################     
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
    speeds_in_kmph=get_speed(filename) #adding speed values to this list
    speeds_in_ms=[]
    
    for speed in speeds_in_kmph:
        ms_speed=speed*(5/18) 
        speeds_in_ms.append(round(ms_speed,4))   #appending to ms list
        
    return speeds_in_ms
   
   
################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.    
    for i in range(1,len(speeds)):
        acc=(speeds[i]-speeds[i-1])/0.1   #100ms=0.1s   calculating acceleration using velocity difference 
        acceleration.append(round(acc,2)) 
################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

        # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
        # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
        
# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')      
# Time values (in seconds)
time=[i/1000 for i in range(0,1100,100)]

model1_speed=convert_kmph_to_ms(MODEL_1_INPUT_FILE)
model2_speed=convert_kmph_to_ms(MODEL_2_INPUT_FILE)
model3_speed=convert_kmph_to_ms(MODEL_3_INPUT_FILE)

model1_acc=get_acceleration(model1_speed)
model2_acc=get_acceleration(model2_speed)
model3_acc=get_acceleration(model3_speed)

plt.plot(time,model1_acc,label='model1')
plt.plot(time,model2_acc,label='model2')
plt.plot(time,model3_acc,label='model3')
# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.show()


# Write maximum acceleration to file
with open("max_acceleration.txt","w") as file:
    file.write("model1 " + str(max(model1_acc)) + "\n")
    file.write("model2 " + str(max(model2_acc)) + "\n")
    file.write("model3 " + str(max(model3_acc)) + "\n")



################################################################################
# Please do not edit anything below this line.
evaluate_lab7()


##################### End of the programme #####################################