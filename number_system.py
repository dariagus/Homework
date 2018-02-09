def dec2bin(x):
    s = ''
    while x > 0:
        z = str(x % 2)
        s = z + s
        x = int(x / 2)
    return s

def dec2oct(x):
    y = ''
    while x > 0:
        z = str(x % 8)
        y = z + y
        x = int(x / 8)
    return y

def dec2hex(x):
    a = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8',
         9:'9',10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    b = ''
    while x > 0:
        z = x % 16
        b = a[z] + b
        x = x // 16
    return b

def bin2dec(x):
    return(int(x, 2))

def oct2dec(x):
    return(int(x, 8))

def hex2dec(x):
    return(int(x, 16))

