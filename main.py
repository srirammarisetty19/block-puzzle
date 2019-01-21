from module1 import *
from module2 import *
import os
import pigame


def element(puzzle,start,size,current,final_puzzle):         # to find out the position of the element in the
	for i in range(start,size):								 # current puzzle to be placed in the appropriate
		for j in range(start,size):							 # place.
			if puzzle[i][j]==final_puzzle[current]:
				return (i,j)
	return(-1.-1)

def check(size,puzzle,final_puzzle):										# to check whether the elements in the
	if puzzle[size-2][size-2]==final_puzzle[(size-2)*size+size-2]:			# 2X2 matrix are in their current position.
		if puzzle[size-2][size-1]==final_puzzle[(size-2)*size+size-1]:
			if 	puzzle[size-1][size-2]==final_puzzle[(size-1)*size+size-2]:
				return True
	return False

def swap(puzzle,ar,ac,br,bc):							# to swap two numbers
	return puzzle[br][bc],puzzle[ar][ac]

def zero(puzzle,start,size):							# to find out the position of zero in the matrix.
	for i in range(start,size):
		for j in range(start,size):
			if puzzle[i][j]=="0":
				return (i,j)
	return (-1,-1)

def first_row(puzzle,size,row,column,element_row,element_column):   # solves the topmost row in the given matrix.

	cornercase=0
	shuffle=0
	starting_row=row
	(zero_x,zero_y)=zero(puzzle,starting_row,size)
	if column == size-2 :												# when the element is to be placed in the
		if element_row==row and element_column==size-1:					# second rightmost column,it places the element
			cornercase=1												# in the next row of the same column.
		if element_row==row+1 and element_column==size-1 and zero_x==row and zero_y==size-1:
				puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
				cornercase=1
				element_row = element_row-1
				zero_x=zero_x+1
				pigame.display(size,puzzle,0)
		row+=1
		shuffle=1

	if column == size-1:								# when the element is to be placed in the rightmost column
		column-=1										# it places the element in the second rightmost column
														# of the same row.

	if 	zero_x<=row :										# to move the zero when it is in the row smaller than
		(zero_x,zero_y)=zero(puzzle,starting_row,size)  	# or equal to the concerned row as it might effect
		puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)   # already solved
		if zero_x+1 == element_row and zero_y == element_column:									#ones.
			element_row = element_row-1

		zero_x=zero_x+1
		pigame.display(size,puzzle,0)

# different moves based on the position of the element with respect to that of the position where it has
# to be brought

	if element_column-column<0:
		(zero_x,zero_y,flag)=shift_zero_tomove_ele_left(puzzle,zero_x,zero_y,element_row,element_column,column,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			element_column=element_column+1
			pigame.display(size,puzzle,0)

		(zero_x,zero_y,element_column)=shift_col_right(puzzle,zero_x,zero_y,element_row,element_column,column,size)
	if element_column-column>0:
		(zero_x,zero_y)=zero(puzzle,starting_row,size)
		(zero_x,zero_y,flag)=shift_zero_tomove_ele_right(puzzle,zero_x,zero_y,element_row,element_column,column,row,size)

		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			element_column=element_column-1
			pigame.display(size,puzzle,0)

		(zero_x,zero_y,element_column)=shift_col_left(puzzle,zero_x,zero_y,element_row,element_column,column,size)

	if element_row-row>0:
		(zero_x,zero_y)=zero(puzzle,starting_row,size)
		(zero_x,zero_y,flag)=shift_zero_tomove_ele_up(puzzle,zero_x,zero_y,element_row,element_column,row,column,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			element_row = element_row-1
			pigame.display(size,puzzle,0)

		(zero_x,zero_y,element_row)=shift_row_up(puzzle,zero_x,zero_y,element_row,element_column,row,size)

# in the case where the element has to be placed in the last and second last column

	if shuffle == 1 and cornercase==0:

		if zero_y == size-3:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			pigame.display(size,puzzle,0)

		while zero_y<size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)

		while zero_x>starting_row:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
		zero_y=zero_y-1
		pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
		zero_x=zero_x+1
		pigame.display(size,puzzle,0)

# a cornercase where a problem gets created when the element to be placed on the second most column
# is present in the last column of the same row.

	if cornercase==1:
		for i in range(2):
			(zero_x,zero_y)=zero_down(puzzle,element_row+2-i,zero_x,zero_y,size)
			(zero_x,zero_y)=zero_left(puzzle,element_column,zero_x,zero_y,size)
			(zero_x,zero_y)=zero_up(puzzle,element_row,zero_x,zero_y,size)
			element_row+=1
			(zero_x,zero_y)=zero_right(puzzle,element_column+1,zero_x,zero_y,size)
		(zero_x,zero_y)=zero_down(puzzle,element_row,zero_x,zero_y,size)
		(zero_x,zero_y,abc)=shift_row_up(puzzle,zero_x,zero_y,row,size-1,row-1,size)
		(zero_x,zero_y)=zero_left(puzzle,element_column,zero_x,zero_y,size)
		(zero_x,zero_y)=zero_up(puzzle,row-1,zero_x,zero_y,size)
		(zero_x,zero_y)=zero_right(puzzle,element_column+1,zero_x,zero_y,size)

		current=(row-1)*size+size-2
		(i,j)=element(puzzle,row,size,current,final_puzzle)
		first_row(puzzle,size,row-1,size-2,i,j)


def first_column(puzzle,size,row,column,element_row,element_column):  #solves the leftmost column in the matrix.
	shuffle=0
	starting_column=column
	cornercase=0

	(zero_x,zero_y)=zero(puzzle,starting_column,size)
	if row==size-2 :												# when the element is to be placed in the
		if element_column==column and element_row==size-1:			# second last row, it places the element
			cornercase=1											# in the next column of the same row.
		if element_column==column+1 and element_row==size-1 and zero_y==column and zero_x==size-1:
			cornercase=1
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			element_column = element_column-1
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)
		column+=1
		shuffle=1

	if row==size-1:									# when the element is to be placed in the last row, it places the
		row-=1										# element in the second last row of the same column.

# different moves based on the position of the element with respect to that of the position where it has
# to be brought

	if  zero_y<=column:
		(zero_x,zero_y)=zero(puzzle,starting_column,size)
		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
		if zero_x == element_row and zero_y+1 == element_column:
			element_column = element_column-1
		zero_y=zero_y+1
		pigame.display(size,puzzle,0)

	if element_row-row<0:
		(zero_x,zero_y,flag)=shift_zero_tomove_ele_down(puzzle,zero_x,zero_y,element_row,element_column,row,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			element_row=element_row+1
			pigame.display(size,puzzle,0)


		(zero_x,zero_y,element_row)=shift_row_down(puzzle,zero_x,zero_y,element_row,element_column,row,size)

	if element_row-row>0:
		(zero_x,zero_y)=zero(puzzle,starting_column,size)
		(zero_x,zero_y,flag)=shift_zero_tomove_ele_up(puzzle,zero_x,zero_y,element_row,element_column,row,column,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			element_row=element_row-1
			pigame.display(size,puzzle,0)


		(zero_x,zero_y,element_row)=shift_row_up(puzzle,zero_x,zero_y,element_row,element_column,row,size)

	if element_column-column>0:
		(zero_x,zero_y)=zero(puzzle,starting_column,size)
		(zero_x,zero_y,flag)=shift_zero_tomove_ele_right(puzzle,zero_x,zero_y,element_row,element_column,column,row,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			element_column=element_column-1
			pigame.display(size,puzzle,0)


		(zero_x,zero_y,element_column)=shift_col_left(puzzle,zero_x,zero_y,element_row,element_column,column,size)

# in the case where the element has to be placed in the last and second last column

	if shuffle==1 and cornercase==0:
		if zero_x == size-3:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			pigame.display(size,puzzle,0)

		while zero_x<size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			pigame.display(size,puzzle,0)

		while zero_y>starting_column:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
		zero_x=zero_x-1
		pigame.display(size,puzzle,0)

		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
		zero_y=zero_y+1
		pigame.display(size,puzzle,0)

# a cornercase where a problem gets created when the element to be placed on the second most row
# is present in the last row of the same column.

	if cornercase==1:
		for i in range(2):
			(zero_x,zero_y)=zero_right(puzzle,element_column+2,zero_x,zero_y,size)
			(zero_x,zero_y)=zero_up(puzzle,element_row,zero_x,zero_y,size)
			(zero_x,zero_y)=zero_left(puzzle,element_column,zero_x,zero_y,size)
			(zero_x,zero_y)=zero_down(puzzle,element_row+1,zero_x,zero_y,size)
		(zero_x,zero_y)=zero_right(puzzle,element_column+2,zero_x,zero_y,size)
		(zero_x,zero_y,abc)=shift_col_left(puzzle,zero_x,zero_y,size-1,element_column+1,element_column,size)
		(zero_x,zero_y)=zero_up(puzzle,row,zero_x,zero_y,size)
		(zero_x,zero_y)=zero_left(puzzle,element_column,zero_x,zero_y,size)
		(zero_x,zero_y)=zero_down(puzzle,size-1,zero_x,zero_y,size)

		current=(size-2)*size+column-1
		(i,j)=element(puzzle,column,size,current,final_puzzle)
		first_column(puzzle,size,size-1,column-1,i,j)

def puzzle_solver(puzzle,final_puzzle,start,size):  # function which gets recursively called to solve the problem.

	if start==size-2:								# base case when the matrix becomes a 2X2 matrix.
		flag=0
		count=0
		(zero_x,zero_y)=zero(puzzle,start,size)
		if check(size,puzzle,final_puzzle):
			flag=1
			pigame.exit(size,flag,puzzle)
		while count<12 and flag==0 :			# it tries to solve the 2X2 matrix by rotating it anticlockwise.
												# there are 12 such possibilities.
			while zero_y<size-1:
				puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
				zero_y=zero_y+1
				count+=1
				pigame.display(size,puzzle,0)
				if check(size,puzzle,final_puzzle):
					flag=1
					pigame.exit(size,flag,puzzle)

			while zero_x<size-1:
				puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
				zero_x=zero_x+1
				count+=1
				pigame.display(size,puzzle,0)
				if check(size,puzzle,final_puzzle):
					flag=1
					pigame.exit(size,flag,puzzle)

			while zero_y>size-2:
				puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
				zero_y=zero_y-1
				count+=1
				pigame.display(size,puzzle,0)
				if check(size,puzzle,final_puzzle):
					flag=1
					pigame.exit(size,flag,puzzle)

			while zero_x>size-2:
				puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
				zero_x=zero_x-1
				count+=1
				pigame.display(size,puzzle,0)
				if check(size,puzzle,final_puzzle):
					flag=1
					pigame.exit(size,flag,puzzle)


		if flag==0:
			pigame.exit(size,flag,puzzle)


	else:

		for column in range(start,size-2):					# to look at different columns in the topmost row
															# till the third last column.
			current=start*size+column
			(i,j)=element(puzzle,start,size,current,final_puzzle)
			first_row(puzzle,size,start,column,i,j)

		current=start*size+size-1	# after that it sends the last column of that row to be placed in its position.
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_row(puzzle,size,start,size-1,i,j)

		current=start*size+size-2 # after that it sends the second last column of that row to be placed in its position.
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_row(puzzle,size,start,size-2,i,j)

		for row in range(start+1,size-2):				# to look at different row in the leftmostmost column
														# till the third last row.
			current=row*size+start
			(i,j)=element(puzzle,start,size,current,final_puzzle)
			first_column(puzzle,size,row,start,i,j)

		current=(size-1)*size+start		# after that it sends the last row  of the column to be placed in its position.
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_column(puzzle,size,size-1,start,i,j)

		current=(size-2)*size+start# after that it sends the secondlast row  of the column to be placed in its position.
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_column(puzzle,size,size-2,start,i,j)

		puzzle_solver(puzzle,final_puzzle,start+1,size)


if __name__=="__main__":
	size=input("enter the size of the square matrix: ")  # size of the sliding puzzle
	print "enter the initial state of puzzle : "
	puzzle=[raw_input().strip().split()[:size] for i in range(size) ]  # take the initial state of the puzzle.
	print "enter the final state of the solver:"
	final_puzzle=[]
	for x in range(size):
		final_puzzle.extend(raw_input().strip().split()[:size])  # final state of the puzzle.
	pigame.display(size,puzzle,0)
	puzzle_solver(puzzle,final_puzzle,0,size)
