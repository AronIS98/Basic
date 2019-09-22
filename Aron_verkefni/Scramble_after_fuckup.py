import string
name=input()
try:
    skra=open(name,"r")
except FileNotFoundError:
    print(("File {} not found!").format(name))
def scrambl(texti):
    nota=""
    utkoma=""
    inserted=""
    place=0
    if texti[(len(texti)-1)] in string.punctuation:
        punct=texti[len(texti)-1]
        nota=texti[0:len(texti)-2]
    else:
        nota=texti[0:len(texti)-1]
        punct=""
    byrjun = nota[0]
    lok=nota[len(nota)-1]
    midja=nota[1:len(nota)-1]
    reps = len(midja)//2
    if len(midja)%2==1:
        inserted=midja[len(midja)-1]
    while reps>0:
        stafur_1=midja[(0+place)]
        stafur_2=midja[(1+place)]
        utkoma+=(stafur_2+stafur_1)
        reps-=1
        place+=2
    return (byrjun+utkoma+inserted+lok+punct)
outcome=""
for lines in skra:
    lines=lines.rstrip()
    outcome+=(scrambl(lines)+" ")
    print(outcome)
#print(scrambl("research,"))