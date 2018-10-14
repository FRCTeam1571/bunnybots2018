def numMap(x, in_min, in_max, out_min, out_max):
    '''Takes value of X and maps it to another value. Taken from the Arduino libary'''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

for i in range(-10, 11):
    i = i/10
    p = numMap(i, -1.0, 1.0, 0.0, 1.0)
    print(i, p)
