# random module to simulate dice flow
import random


# reference for snake and ladders
grid = [i for i in range(101)]
grid[2] = 23
grid[8] = 12
grid[17] = 93
grid[29] = 54
grid[31] = 14
grid[32] = 51
grid[39] = 80
grid[41] = 20
grid[59] = 37
grid[62] = 78 
grid[67] = 50
grid[70] = 89
grid[75] = 96
grid[83] = 80
grid[92] = 76
grid[99] = 4


i = 0 
a,b=0,0

while(True):
	count = random.randint(1,6)
	if(i==0):
		print("Player A turn: ",end="")
		x = input()
		i = abs(1-i)
		print("A got {}".format(count))
		if(a+count==100):
			print("A wins")
			break
		
		elif(a+count<100):
			a += count
			if(grid[a]>a):
				print("A got ladder at {} and went to {}".format(a,grid[a]))

			elif(grid[a]<a):
				print("A got bitten at {} and went to {}".format(a,grid[a]))
			else:
				print("A went to {}".format(a))
		else:
			print("not possible to move")
		a = grid[a]
		print()


	else:
		print("Player B turn: ",end="")
		x = input()
		i = abs(1-i)
		print("B got {}".format(count))
		if(b+count==100):
			print("B wins")
			break
		
		elif(b+count<100):
			b+= count
			if(grid[b]>b):
				print("B got ladder at {} and went to {}".format(b,grid[b]))
			elif(grid[a]<a):
				print("B got bitten at {} and went to {}".format(b,grid[b]))
			else:
				print("B went to {}".format(b))
		else:
			print("not possible to move")
		b = grid[b]
		print()
		
