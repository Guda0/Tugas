Regards=input(' ').lower().replace(" ","")
RG=Regards[0:5]
if(Regards=='hello'):
    cuan=0
elif(RG=='hello'):
    cuan=0
elif(Regards[0]=='h'):
    cuan=20
else :
    cuan=100

print ('$',cuan)