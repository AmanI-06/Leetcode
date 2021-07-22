def decimalToBinary(x,y):
    xor = x ^ y
    print(xor)
    count = 0
    for i in range(32):
        count += xor & 1
        xor = xor >> 1
    return count
print(decimalToBinary(1,4))
    