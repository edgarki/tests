#in:
#20
#[[1,8],[2,7],[3,14]]
#[[1,5],[2,10],[3,14]]

#out
#3 1


#in:
#20
#[[1,8],[2,15],[3,9]]
#[[1,8],[2,11],[3,12]]

#out
#1 3
#3 2

o = []

for i in range(len(foregroundAppList)):
    	for j in range(len(backgroundAppList)):
    		#print i,j
    		#print foregroundAppList[i],backgroundAppList[j]
    		f = foregroundAppList[i]
    		b = backgroundAppList[j]
    		s = f[1] + b[1]
    		if s <= deviceCapacity:
    			
    			o.append([[f[0],b[0],s]])

w = 0
wi = 0
ow = [[0,0]]
for i in range(len(o)):
	if o[i][0][2] == w:
		ow.append([o[i][0][0],o[i][0][1]])
		wi += 1
	if o[i][0][2] > w:
		w = o[i][0][2]
		ow[wi] = [o[i][0][0],o[i][0][1]]
	
print ow
