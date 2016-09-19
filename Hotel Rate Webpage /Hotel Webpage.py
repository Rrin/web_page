
inforList=[]
YEGList=[]
YYCList=[]
YVRList=[]
file=input("Enter name of file: ")
if file=="hotels.data":
    ofile=open("hotels.data","r")
elif file=="Restaurants.data":
    ofile=open("Restaurants.data","r")
for line in ofile:
    line=line.strip("\n")
    line=line.split(";")
    if line[0]=="YEG":
        YEGList.append(line)
    elif line[0]=="YYC":
        YYCList.append(line)
    elif line[0]=="YVR":
        YVRList.append(line)
    else:
        inforList.extend(line)
ofile.close()
# sort YEGList according to price per night
YEGlist=[]
record=[]
for item in YEGList:
    data=int(item[3][1:])
    record.append(data)
    record.sort()
for i in record:
    for item in YEGList:
        if "$"+str(i) in item:
            YEGlist.append(item)
# sort YYCList accourding to price per night
YYClist=[]
record=[]
for item in YYCList:
    data=int(item[3][1:])
    record.append(data)
    record.sort()
for i in record:
    for item in YYCList:
        if "$"+str(i) in item:
            YYClist.append(item)
# sort YVRList accounding to price
YVRlist=[]
record=[]
for item in YVRList:
    data=int(item[3][1:])
    record.append(data)
    record.sort()
for i in record:
    for item in YVRList:
        if "$"+str(i) in item:
            YVRlist.append(item)
            
if file=="hotels.data":
    output=open("hotels.html","w")
elif file=="Restaurants.data":
    output=open("Restaurants.html","w")

# start the html page
output.write('<html>\n<body>\n<h1>Query Results</h1>\n<h2>From City: Calgary</h2>')
output.write('<table border="1" style="width:45%">\n<tr valign="middle">\n<th>'+inforList[1]+'</th>\n<th>Review</th>\n<th>'+inforList[3]+'</th>\n<th>Details</th>\n</tr>')
t=0
for item in YYClist:
    # draw the review stars in the webpage
    data=float(item[2])
    review=str((int(data//1))*"<img src='star-full.png' />")
    if data%1 != 0.0: 
        review=review+"<img src='star-half.png' />"
        number=4-int(data//1)
    else:
        number=5-int(data//1)
    review=review+str(number*"<img src='star-empty.png' />")
    
    #create secondary webpage
    if file=="Restaurants.data":
        title="restaurants-YYC-"+str(t)+".html"
    else:
        title="hotels-YYC-"+str(t)+".html"
    newPage=open(title,"w")
    More=('<html>\n<h1>Query Results</h1>\n<h2>From City: Calgary</h2>\n<img src="'+item[4]+'" />\n<p>'+item[6]+'</p>\n<ul>\n<li>'+inforList[1]+':'+item[1]+'</li>\n<li>Review:'+review+'</li>\n<li>'+inforList[3]+':'+item[3]+'</li>\n<li>URL: http://'+item[5]+'</li>\n<li>Phone:'+item[7]+'</li>\n<li>Address:'+item[8]+'</li>\n</ul>\n</html>')
    
    newPage.write(More)
    newPage.close()
    output.write('<tr>\n<td>'+item[1]+'</td>\n<td>'+review+'('+item[2]+')</td>\n<td>'+item[3]+'</td>\n<td>\n<a href="'+title+'"> More...</a>\n</td>\n</tr>')
    t=t+1
output.write("</table>")
output.write('<h2>From City: Edmonton</h2>')
output.write('<table border="1" style="width:55%">\n<tr valign="middle">\n<th>'+inforList[1]+'</th>\n<th>Review</th>\n<th>'+inforList[3]+'</th>\n<th>Details</th>\n</tr>')
y=0
for item in YEGlist:
    # draw the review stars in the webpage
    data=float(item[2])
    review=str((int(data//1))*"<img src='star-full.png' />")
    if data%1 != 0.0: 
        review=review+"<img src='star-half.png' />"
        number=4-int(data//1)
    else:
        number=5-int(data//1)
    review=review+str(number*"<img src='star-empty.png' />")
    #create secondary webpage
    if file=="Restaurants.data":
        title="restaurant-YEG-"+str(y)+".html"
    else:
        title="hotels-YEG-"+str(y)+".html"
    newPage=open(title,"w")
    More=('<html>\n<h1>Query Results</h1>\n<h2>From City: Edmonton</h2>\n<img src="'+item[4]+'" />\n<p>'+item[6]+'</p>\n<ul>\n<li>'+inforList[1]+':'+item[1]+'</li>\n<li>Review:'+review+'</li>\n<li>'+inforList[3]+':'+item[3]+'</li>\n<li>URL: http://'+item[5]+'</li>\n<li>Phone:'+item[7]+'</li>\n<li>Address:'+item[8]+'</li>\n</ul>\n</html>')
       
    newPage.write(More)
    newPage.close()
    output.write('<tr>\n<td>'+item[1]+'</td>\n<td>'+review+'('+item[2]+')</td>\n<td>'+item[3]+'</td>\n<td>\n<a href="'+title+'"> More...</a>\n</td>\n</tr>')
    y=y+1        
output.write("</table>")    

if file=="Restaurants.data":
    output.write('<h2>From City: Vancouver</h2>')
    output.write('<table border="1" style="width:55%">\n<tr valign="middle">\n<th>'+inforList[1]+'</th>\n<th>Review</th>\n<th>'+inforList[3]+'</th>\n<th>Details</th>\n</tr>')    
    j=0
    for item in YVRlist:
        # draw the review stars in the webpage
        data=float(item[2])
        review=str((int(data//1))*"<img src='star-full.png' />")
        if data%1 != 0.0: 
            review=review+"<img src='star-half.png' />"
            number=4-int(data//1)
        else:
            number=5-int(data//1)
        review=review+str(number*"<img src='star-empty.png' />")
        
        #create secondary webpage
        title="restaurant-YVR-"+str(t)+".html"
        newPage=open(title,"w")
        More=('<html>\n<h1>Query Results</h1>\n<h2>From City: Vancouver</h2>\n<img src="'+item[4]+'" />\n<p>'+item[6]+'</p>\n<ul>\n<li>'+inforList[1]+':'+item[1]+'</li>\n<li>Review:'+review+'</li>\n<li>'+inforList[3]+':'+item[3]+'</li>\n<li>URL: http://'+item[5]+'</li>\n<li>Phone:'+item[7]+'</li>\n<li>Address:'+item[8]+'</li>\n</ul>\n</html>')
        
        newPage.write(More)
        newPage.close()
        output.write('<tr>\n<td>'+item[1]+'</td>\n<td>'+review+'('+item[2]+')</td>\n<td>'+item[3]+'</td>\n<td>\n<a href="'+title+'"> More...</a>\n</td>\n</tr>')
        j=j+1
    
    output.write('</table>')
output.write('</html>')
    
    
output.close()

    


    