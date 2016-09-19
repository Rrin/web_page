inforList=[]
YEGList=[]
YYCList=[]
YVRList=[]
ofile=open("hotels.data","w")
output=open("hotels.txt","r")
for line in output:
  
     ofile.write(line)
output.close()
ofile.close()
