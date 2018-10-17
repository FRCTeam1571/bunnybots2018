def numMap(x, in_min, in_max, out_min, out_max):
    '''Takes value of X and maps it to another value. Taken from the Arduino libary'''
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
