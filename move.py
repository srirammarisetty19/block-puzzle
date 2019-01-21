import pigame
moves=0
def display(size,puzzle):
    global moves
    moves+=1
    if isinstance(size,int):
		print "move",moves
		for i in range(size):
			for j in range(size):
				print str(puzzle[i][j])+" ",
			print
