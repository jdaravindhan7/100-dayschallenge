#print even numbers using while loop
i=0
n=int(input("enter n"))
while i<n:
	if(i%2==0):
		if(i!=18):
			print(i)
		else:
			print('its eighteen')
			break
	i+=1
	
