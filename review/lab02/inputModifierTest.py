from inputModifier import *

name = inputString("Input a procces name: ")
threads =  inputInt("Input the number of threads: ")

total_mem = 0
for i in range(threads):
    memory = inputFloat(f"Input amount of memory used by thread {i}: ")
    total_mem += memory

print(f"Sum of memory consumed by proccess {name} is {total_mem}.")


