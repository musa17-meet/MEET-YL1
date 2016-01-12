def palidrome(m):
	if m[::-1]==m:		
		print ("true")
	else:
		print("false")

print("please enter a string")
m=input()
palidrome(m)
