import numpy as np
import random
from queue import PriorityQueue

print("welcome to the demo of Lai-yang algorithm!")
N= int(input("\nEnter the No of Process (Please enter from any number from 2,3 and 4): "))
print("No of Process :",N)
number_list = [x for x in range(1,N+1)]
total_time = 60 # time instance is in seconds
sample_time = 5 # time instance at which sample starts
sample_size = int(total_time/sample_time) #time ins
print("No of Time instance assummed for this simulation:",sample_size)
Process_lists = [[] for _ in range(N)]
sendmsg_lists = [[] for _ in range(N)]
recmsg_lists  = [[] for _ in range(N)]
#print(lists)
for i in range(N):
    Process_lists[i] = (1,sample_size)
    Process_lists[i] = np.zeros((sample_size,), dtype=int)

for i in range(N):
    sendmsg_lists[i] = (1,sample_size)
    sendmsg_lists[i] = np.zeros((sample_size,), dtype=int)

for i in range(N):
    recmsg_lists[i] = (1,sample_size)
    recmsg_lists[i] = np.zeros((sample_size,), dtype=int)

for index1 in range(0,N):
    for index2 in range(1):
        Process_lists[index1][index2] = int(input("\nEnter the Process"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t"))

print("Initialized Successfully at time instant t0"+ ' '*1 + str(sample_time) +"units")

total_amount_value = 0

for index1 in range(0,N):
    for index2 in range(1):
      total_amount_value = total_amount_value + Process_lists[index1][index2]
print("Total amount in INR before transacation:",total_amount_value)

for index1 in range(0,N):
    print ("\nProcess"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",Process_lists[index1])

#stack = []
data = list(range(0,N+1))
random.shuffle(data)
print("Data",data)
q = PriorityQueue()
msg_exchange  = []
flag = 0
k=1
# Running the simulation for N-1 times 
for i in range(1,sample_size):
    print("iteration:\t",i)
    print("simulation at time instant t"+ str(i) + ' '*1 +  str((i+1)*sample_time) +"units")
     
    if i <= N+1 : 
         
      print("Send message from one process to another process")
             
      for index1 in range(0,N):
        Process_lists[index1][i] = Process_lists[index1][i-1]
      for index1 in range(0,N):
        print ("\nProcess"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",Process_lists[index1])
      sen = int(input('sending msg from which Process we have Process'+ ' '*1 + str(number_list) + ' '*1+ 'enter integers only'+' '*1))
      rec = int(input('sending msg  to  which Process we have Process'+ ' '*1 + str(number_list) + ' '*1+ 'enter integers only'+' '*1))
      inr = int(input('enter the amount you want transfer from Process'+ ' '*1 + str(sen) +' '*1 +'to'+ ' '*1 +'Process' + ' '*1 +str(rec)+' '*1))
        #print ("Process P_" + str(sen))
      Process_lists[sen-1][i] = Process_lists[sen-1][i-1]-inr 
      sendmsg_lists[sen-1][i] = inr
      q.put((data[i-1],sen,rec,inr))
      #stack.append(inr)
      #stack.append(sen)
      #stack.append(rec)
      msg_exchange.append("Message send from"+ ' '*1+ str(sen)+ "to"+' '*1 +str(rec)+ ' '*1 + "amount"+' '*1+str(inr) )
      #print("stack:\t",stack)
      for index1 in range(0,N):
        print ("\nProcess"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",Process_lists[index1])
        print("Send array:",sendmsg_lists[index1])
      flag = flag + 1
        
    elif k <= N+1 :
      print("Recieve message from one process to another process")
      k = k+1
      print ("Receiving queue contains more than one message at the time we can only process receive message.")
      for index1 in range(0,N):
        Process_lists[index1][i] = Process_lists[index1][i-1]
          
      for index1 in range(0,N):
        print ("\nProcess"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",Process_lists[index1])
      print("iteration:\t",i)

      list1 = q.get()
      #print("size of the receiver stack:",len(stack)) 
      #length = len(stack)
      sen = list1[1]
      rec = list1[2]
      inr = list1[3]
      msg_exchange.append("Message receive from"+ ' '*1+ str(sen)+ "to"+' '*1 +str(rec)+ ' '*1 +"amount"+' '*1+str(inr) )
      Process_lists[rec-1][i] = Process_lists[rec-1][i-1]+inr
      recmsg_lists[rec-1][i] = inr
      for index1 in range(0,N):
        print ("\nProcess"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",Process_lists[index1])
        print ("\nSend Process"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",sendmsg_lists[index1])
      print("receiving buffer not yet processed in the order of send process and receive process and amount")
    else:
      print("\n The system assumed that you don't want to anything at this particular time instant") 
      print("iteration:\t",i)
      for index1 in range(0,N):
        Process_lists[index1][i] = Process_lists[index1][i-1]
      for index1 in range(0,N):
        print ("\nProcess"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",Process_lists[index1])

for index1 in range(0,N):
  print ("\nProcess"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",Process_lists[index1])
  print ("\nSend Process"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",sendmsg_lists[index1])
  print ("\nReceive Process"+ ' '*1+ str(index1+1) + ' '*1 +"Initial value:\t",recmsg_lists[index1])
  

GS_initator = 1
print("\nEnter the Global Snapshot time time instance:")
print ("\nThe possible time instance values are"+ ' '*1+ "from 1 to  "+str(sample_size-1))
GS_time_inst  = int(input("\nplease enter the value:"))
process_init_values = []
process_current_state = []
process_init_values  =  [0 for i in range(N)]
process_current_state = [0 for i in range(N)]
Global_state_value = 0
for index1 in range(0,N):
  index2 = 0 
  process_init_values[index1] = Process_lists[index1][index2]

print("\nProcess_initial_values:",process_init_values)

for index1 in range(0,N):
  index2 = GS_time_inst
  process_current_state[index1] = process_init_values[index1] - (sendmsg_lists[index1][index2]+recmsg_lists[index1][index2])

print("\nProcess_current_state at GS initiating time:",process_current_state)
print("\nGlobal State Recording is Initiated by Process 1 and Process 1 turns red")

for index1 in range(1,N):
  print("\n Now the Process"+' '*1 +str(index1+1)+ ' '*1 + "turns red")

print("\nAt Global State Time Instance T"+str(GS_time_inst) + ":")

print("\n total message exchange between the process:",msg_exchange)
print("\n these are the white messages sent by the processes before P1 turning red")
print(msg_exchange[0:GS_time_inst])
print("\n these are the red message sent by the process:")
print(msg_exchange[GS_time_inst:N+N+1])



for index1 in range(0,N):
  index2 = GS_time_inst
  Global_state_value = Global_state_value + process_current_state[index1] + (sendmsg_lists[index1][index2]+recmsg_lists[index1][index2])

print("\nGlobal State value:",Global_state_value)

if Global_state_value == total_amount_value :
  print("\nGlobal state value preserved is matching the Total amount value")
else:
  print("Global state value is not preserved, please check anything wrong in the inputs provided")