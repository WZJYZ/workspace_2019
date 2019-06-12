'''

with open("./m10.crp", "r") as f:
    sum = 0
    lines = f.readlines();
    for i in range(len(lines)):
        line = lines[i].strip().split(" ")
        sum += int(line[1])
    print(sum)
    print(len(lines))
    print(sum/len(lines))


'''
import numpy as np
with open("./c1000_id0.crp", "r") as f:
    f.readline()
    lines = f.readlines()
    sum = 0
    arr = list()
    for i in range(len(lines)):
        line = lines[i].strip().split(" ")
        arr.append(list(line[7]))
    arr = np.array(arr, dtype=np.int)
    #print(arr[0])
    for i in range(len(arr[0])):
        print(np.sum(arr[:, i])/len(arr))

