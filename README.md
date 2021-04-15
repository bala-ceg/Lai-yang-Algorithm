# Lai-yang-Algorithm
Distributed snapshot algorithm designed in such way that it will work for both NON-FIFO & FIFO Channels

Coded Language 	   : Python3
Dependency libaries: numpy,random,queue 
Executed Machine   : windows 
Editor used	   : Microsoft Visual studio code

(Please make sure the above dependency libaries is installed in target system,
in which you are execute this program)


-----------------------------------------
Assumptions i made for this simulation:
------------------------------------------
1. I assumed the no of time-instance for this simulation is 12 (time-instance t0 to t11,each time-instance is of 5 units)
   at time-instant t0 we cannot send or receive messages

2. I assumed the N+1 Send messages between the processes and N+1 Receive messages between the processes in this simulation

3. According to my first assumption,the maximum process i considered as per the time stamp is 2,3 and 4.

4. I have assumed that each send message is taken from the user at each time-instant and each receive message will be processed as both
   Non-FIFO & FIFO at each time-instant based on the randomly generated priority. I used Priority Queue implementation for this.


----------------
Working Status
----------------
  I found that my program is working fine for 2,3 and 4 Processes and please find the 
  attached logs in the folder.This Program will work for both FIFO & NON-FIFO communication channels
