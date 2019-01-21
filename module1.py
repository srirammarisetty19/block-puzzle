import pigame
def swap(puzzle,ar,ac,br,bc):						# to swap
	return puzzle[br][bc],puzzle[ar][ac]


def zero_up(puzzle,element_row,zero_x,zero_y,size):  # to move the zero upwards
	zx=zero_x
	for i in range(zx-1,element_row-1,-1):
		puzzle[zero_x][zero_y],puzzle[i][zero_y]=swap(puzzle,zero_x,zero_y,i,zero_y)
		zero_x=i
		pigame.display(size,puzzle,0)
	return (zero_x,zero_y)

def zero_down(puzzle,element_row,zero_x,zero_y,size):   # to move the zero downwards
	zx=zero_x
	for i in range(zx+1,element_row+1):
		puzzle[zero_x][zero_y],puzzle[i][zero_y]=swap(puzzle,zero_x,zero_y,i,zero_y)
		zero_x=i
		pigame.display(size,puzzle,0)
	return (zero_x,zero_y)

def zero_right(puzzle,element_column,zero_x,zero_y,size):     # to move the zero rightwards
	zy=zero_y
	for i in range(zy+1,element_column+1):
		puzzle[zero_x][zero_y],puzzle[zero_x][i]=swap(puzzle,zero_x,zero_y,zero_x,i)
		zero_y=i
		pigame.display(size,puzzle,0)
	return (zero_x,zero_y)

def zero_left(puzzle,element_column,zero_x,zero_y,size):    #  to move the zero leftwards
	zy=zero_y
	for i in range(zy-1,element_column-1,-1):
		puzzle[zero_x][zero_y],puzzle[zero_x][i]=swap(puzzle,zero_x,zero_y,zero_x,i)
		zero_y=i
		pigame.display(size,puzzle,0)
	return 	(zero_x,zero_y)

def shift_zero_tomove_ele_left(puzzle,zero_x,zero_y,element_row,element_column,column,size): # to move the element
	flag=0																				# such that we can move element
	if element_column-zero_y>0 :													    # towards its left
		(zero_x,zero_y)=zero_right(puzzle,element_column-1,zero_x,zero_y,size)
	if 	element_column-zero_y<0 :
		(zero_x,zero_y)=zero_left(puzzle,element_column+1,zero_x,zero_y,size)
		flag=1
	if element_column-zero_y == 0:
		(zero_x,zero_y)=zero_right(puzzle,element_column+1,zero_x,zero_y,size)
		flag=1

	if element_row-zero_x<0:
		(zero_x,zero_y)=zero_up(puzzle,element_row,zero_x,zero_y,size)
	if element_row - zero_x > 0:
		(zero_x,zero_y)=zero_down(puzzle,element_row,zero_x,zero_y,size)

	return (zero_x,zero_y,flag)

def shift_zero_tomove_ele_right(puzzle,zero_x,zero_y,element_row,element_column,column,row,size): # to move the zero
	flag=0																			 # such that we can move element
	if element_column-zero_y>0 :													 # towards its right
		(zero_x,zero_y)=zero_right(puzzle,element_column-1,zero_x,zero_y,size)
		flag=1
	if element_column-zero_y<0:
		(zero_x,zero_y)=zero_left(puzzle,element_column+1,zero_x,zero_y,size)
	if element_column-zero_y == 0:

		if (zero_y-1==column and zero_x>row) or zero_y-1>column or element_column==size-1:
			(zero_x,zero_y)=zero_left(puzzle,element_column-1,zero_x,zero_y,size)
			flag=1
		else:
			(zero_x,zero_y)=zero_right(puzzle,element_column+1,zero_x,zero_y,size)

	if element_row-zero_x<0:
		(zero_x,zero_y)=zero_up(puzzle,element_row,zero_x,zero_y,size)
	if element_row - zero_x > 0:
		(zero_x,zero_y)=zero_down(puzzle,element_row,zero_x,zero_y,size)

	return (zero_x,zero_y,flag)

def shift_zero_tomove_ele_down(puzzle,zero_x,zero_y,element_row,element_column,row,size): # to move the zero
	flag=0																				# such that we can move element
	if element_row-zero_x<0:														    # downwards
		(zero_x,zero_y)=zero_up(puzzle,element_row+1,zero_x,zero_y,size)
		flag=1
	if element_row - zero_x >0:
		(zero_x,zero_y)=zero_down(puzzle,element_row-1,zero_x,zero_y,size)
	if element_row - zero_x ==0:
		(zero_x,zero_y)=zero_down(puzzle,element_row+1,zero_x,zero_y,size)
		flag=1
	if element_column-zero_y>0 :
		(zero_x,zero_y)=zero_right(puzzle,element_column,zero_x,zero_y,size)
	if element_column-zero_y<0:
		(zero_x,zero_y)=zero_left(puzzle,element_column,zero_x,zero_y,size)

	return (zero_x,zero_y,flag)

def shift_zero_tomove_ele_up(puzzle,zero_x,zero_y,element_row,element_column,row,column,size): # to move the zero
	flag=0																				# such that we can move element
	if element_row-zero_x<0:															# upwards.
		(zero_x,zero_y)=zero_up(puzzle,element_row+1,zero_x,zero_y,size)
	if element_row - zero_x >0:
		(zero_x,zero_y)=zero_down(puzzle,element_row-1,zero_x,zero_y,size)
		flag=1
	if element_row - zero_x ==0:
		if zero_x-1>row or (element_row-1==row and zero_y>column) or element_row==size-1:
			(zero_x,zero_y)=zero_up(puzzle,element_row-1,zero_x,zero_y,size)
			flag=1
		else:
			(zero_x,zero_y)=zero_down(puzzle,element_row+1,zero_x,zero_y,size)

	if element_column-zero_y>0 :
		(zero_x,zero_y)=zero_right(puzzle,element_column,zero_x,zero_y,size)
	if element_column-zero_y<0:
		(zero_x,zero_y)=zero_left(puzzle,element_column,zero_x,zero_y,size)

	return (zero_x,zero_y,flag)
