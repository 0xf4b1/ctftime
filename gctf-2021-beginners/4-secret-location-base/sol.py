set_mask = [67,20,2,57,0,5,18,1,64,2,1,18,1,4,0,64,16,2,0,9,0,0,8,65,22,0,0,0,65,22,1,4,66,1,0,24,67,24,2,65,16,2,68,19,72,2]
clr_mask = [0,3,16,4,25,2,65,2,17,0,6,65,0,2,0,16,64,4,3,0,1,8,0,24,64,0,5,2,16,65,6,0,21,0,2,65,24,67,8,18,64,0,19,64,2,117]

flag = ""
state = 0
for i in range(len(set_mask)):
    state |= set_mask[i]
    state &= ~clr_mask[i]
    flag += chr(state)

print(flag)