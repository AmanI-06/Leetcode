def Uni(lst1, lst2): 
    final_list = list(set(lst1) | set(lst2)) 
    return final_list 

if __name__=="__main__":
    aa=list(map(int,input().split(' ')))
    bb=list(map(int,input().split(' ')))
    g=Uni(aa,bb)
    print(g)
