def stock(p):
    maxpro=0
    minprice=float('inf')  #initillly set to a big value
    for i in p:
        minprice=min(minprice,i)
        maxpro=max(maxpro,i-minprice)

    print(maxpro)
    

h=[7,6,4,3,1]
stock(h)