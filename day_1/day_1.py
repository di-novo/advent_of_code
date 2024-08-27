# Day 1
import re

f = open('/home/dinovo_phil/advent_of_code/day_1/input/day_1_input.txt') #Open puzzle text
print(type(f))

total = 0 #Initialize total calibration value
valid_nums = {'one':"1",'two':"2",'three':"3",'four':"4",'five':"5",'six':"6",'seven':"7",'eight':"8",'nine':"9",'zero':"0"}

new_puzzle = []

for line in f:
    print(list(enumerate(line)))
    #print("Current total is:",total)
    #d = re.findall(r'\d',l)
    #c = int(d[0]+d[-1])
    #total += c
    #print("Line:",l)
    #print("Combined Digit:",c)

#print(total)
