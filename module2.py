import pigame
def swap(puzzle,ar,ac,br,bc):    # to swap
	return puzzle[br][bc],puzzle[ar][ac]

def shift_col_left(puzzle,zero_x,zero_y,element_row,element_column,column,size):  # to move the column of the element
	while element_column>column:												  # towards left
		flag=0
		if element_row==size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			pigame.display(size,puzzle,0)
			flag=1
		else:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			pigame.display(size,puzzle,0)

		for x in range(2):
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			pigame.display(size,puzzle,0)

		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			pigame.display(size,puzzle,0)
		else:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
		zero_y=zero_y+1
		element_column=element_column-1
		pigame.display(size,puzzle,0)

	return (zero_x,zero_y,element_column)

def shift_col_right(puzzle,zero_x,zero_y,element_row,element_column,column,size): # to move the column of the element
	while element_column<column:												  # towards right
		flag=0

		if element_row==size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			pigame.display(size,puzzle,0)
			flag=1

		else:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			pigame.display(size,puzzle,0)

		for x in range(2):
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)

		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			pigame.display(size,puzzle,0)
		else:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
		zero_y=zero_y-1
		element_column=element_column+1
		pigame.display(size,puzzle,0)

	return (zero_x,zero_y,element_column)

def shift_row_down(puzzle,zero_x,zero_y,element_row,element_column,row,size): # to move the column of the element
	while element_row< row:													  # downwards
		flag=0

		if element_column==size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			pigame.display(size,puzzle,0)
			flag=1

		else:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)

		for x in range(2):
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			pigame.display(size,puzzle,0)

		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)

		else:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
		zero_x=zero_x-1
		element_row=element_row+1
		pigame.display(size,puzzle,0)

	return (zero_x,zero_y,element_row)

def shift_row_up(puzzle,zero_x,zero_y,element_row,element_column,row,size): # to move the column of the element
	while element_row>row:													# upwards
		flag=0

		if element_column==size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			pigame.display(size,puzzle,0)
			flag=1

		else:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)

		for x in range(2):
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			pigame.display(size,puzzle,0)

		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)
		else:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
		zero_x=zero_x+1
		element_row=element_row-1
		pigame.display(size,puzzle,0)

	return (zero_x,zero_y,element_row)
