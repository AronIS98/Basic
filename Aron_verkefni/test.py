import string
strengur=" acccccca,, "
svar=""
for char in strengur:
    if char in string.punctuation:
        char=""
    svar+= char
print(svar)
svar= svar.strip()
print(svar)
listi=[]
#------------remove duplicates------------
mylist = list(dict.fromkeys(mylist))
#eða eitthvað sem er ekki bannað:
res = [] 
for i in test_list: 
    if i not in res: 
        res.append(i) 
a= r "nammi \n lala"