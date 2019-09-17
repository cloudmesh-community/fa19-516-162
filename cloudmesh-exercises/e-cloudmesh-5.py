# fa19-516-162: Cloudmesh Common
# E.Cloudmesh.Common.5
# Develop a program that demonstrates the use of cloudmesh.common.StopWatch.

from cloudmesh.common.StopWatch import StopWatch
from time import sleep

# Calculate time taken by sleep function
StopWatch.start("sw1")
sleep(1)
StopWatch.stop("sw1")
print (StopWatch.get("sw1"))

# Calculate time taken to multiple numbers from 9999 to 100000
StopWatch.start("sw2")
sum = 1
for count in range(9999, 100000):
    sum *= count
print(sum)
StopWatch.stop("sw2")
print (StopWatch.get("sw2"))
