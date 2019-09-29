def create_list(size):
    listi=[]
    for each in range(size):
        inp=float(input("Element no {}: ".format(each)))
        listi.append(inp)
    return listi

def dot_product(listi_1,listi_2):
    listi_3=[]
    ans=0
    for each in range(0,len(listi_1)):
        temp_ans=listi_1[each]*listi_2[each]
        listi_3.append(temp_ans)
    for each in listi_3:
        ans+=each
    return ans


size=int(input("Input vector size: "))
listi_1=create_list(size)
listi_2=create_list(size)
ans=dot_product(listi_1,listi_2)
print("Dot product is:",ans)