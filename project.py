from module1 import *
from module2 import *
import move


def element(puzzle,start,size,current,final_puzzle):
	for i in range(start,size):
		for j in range(start,size):
			if puzzle[i][j]==final_puzzle[current]:
				return (i,j)
	return(-1.-1)

def check(size,puzzle,final_puzzle):

	if puzzle[size-2][size-2]==final_puzzle[(size-2)*size+size-2]:
		if puzzle[size-2][size-1]==final_puzzle[(size-2)*size+size-1]:
			if 	puzzle[size-1][size-2]==final_puzzle[(size-1)*size+size-2]:
				return True
	return False

def swap(puzzle,ar,ac,br,bc):
	return puzzle[br][bc],puzzle[ar][ac]

def zero(puzzle,start,size):
	for i in range(start,size):
		for j in range(start,size):
			if puzzle[i][j]=="0":
				return (i,j)
	return (-1,-1)

def first_row(puzzle,size,row,column,element_row,element_column):

	cornercase=0
	shuffle=0
	starting_row=row
	(zero_x,zero_y)=zero(puzzle,starting_row,size)
	if column == size-2 :
		if element_row==row and element_column==size-1:
			cornercase=1
		if element_row==row+1 and element_column==size-1 and zero_x==row and zero_y==size-1:
				puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
				cornercase=1
				element_row = element_row-1
				zero_x=zero_x+1
				move.display(size,puzzle)
		row+=1
		shuffle=1

	if column == size-1:
		column-=1

	if 	zero_x<=row :
		(zero_x,zero_y)=zero(puzzle,starting_row,size)
		puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
		if zero_x+1 == element_row and zero_y == element_column:
			element_row = element_row-1

		zero_x=zero_x+1
		move.display(size,puzzle)
	if element_column-column<0:
		(zero_x,zero_y,flag)=shift_zero1(puzzle,zero_x,zero_y,element_row,element_column,column,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			element_column=element_column+1
			move.display(size,puzzle)

		(zero_x,zero_y,element_column)=shift_col_right(puzzle,zero_x,zero_y,element_row,element_column,column,size)
	if element_column-column>0:
		(zero_x,zero_y)=zero(puzzle,starting_row,size)
		(zero_x,zero_y,flag)=shift_zero2(puzzle,zero_x,zero_y,element_row,element_column,column,row,size)

		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			element_column=element_column-1
			move.display(size,puzzle)

		(zero_x,zero_y,element_column)=shift_col_left(puzzle,zero_x,zero_y,element_row,element_column,column,size)

	if element_row-row>0:
		(zero_x,zero_y)=zero(puzzle,starting_row,size)
		(zero_x,zero_y,flag)=shift_zero4(puzzle,zero_x,zero_y,element_row,element_column,row,column,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			element_row = element_row-1
			move.display(size,puzzle)

		(zero_x,zero_y,element_row)=shift_row_up(puzzle,zero_x,zero_y,element_row,element_column,row,size)


	if shuffle == 1 and cornercase==0:

		if zero_y == size-3:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			move.display(size,puzzle)

		while zero_y<size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			move.display(size,puzzle)

		while zero_x>starting_row:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			move.display(size,puzzle)

		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
		zero_y=zero_y-1
		move.display(size,puzzle)

		puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
		zero_x=zero_x+1
		move.display(size,puzzle)

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


def first_column(puzzle,size,row,column,element_row,element_column):
	shuffle=0
	starting_column=column
	cornercase=0

	(zero_x,zero_y)=zero(puzzle,starting_column,size)
	if row==size-2 :
		if element_column==column and element_row==size-1:
			cornercase=1
		if element_column==column+1 and element_row==size-1 and zero_y==column and zero_x==size-1:
			cornercase=1
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			element_column = element_column-1
			zero_y=zero_y+1
			move.display(size,puzzle)
		column+=1
		shuffle=1

	if row==size-1:
		row-=1



	if  zero_y<=column:
		(zero_x,zero_y)=zero(puzzle,starting_column,size)
		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
		if zero_x == element_row and zero_y+1 == element_column:
			element_column = element_column-1
		zero_y=zero_y+1
		move.display(size,puzzle)

	if element_row-row<0:
		(zero_x,zero_y,flag)=shift_zero3(puzzle,zero_x,zero_y,element_row,element_column,row,shift_zero3)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
			zero_x=zero_x-1
			element_row=element_row+1
			move.display(size,puzzle)


		(zero_x,zero_y,element_row)=shift_row_down(puzzle,zero_x,zero_y,element_row,element_column,row,size)

	if element_row-row>0:
		(zero_x,zero_y)=zero(puzzle,starting_column,size)
		(zero_x,zero_y,flag)=shift_zero4(puzzle,zero_x,zero_y,element_row,element_column,row,column,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			element_row=element_row-1
			move.display(size,puzzle)


		(zero_x,zero_y,element_row)=shift_row_up(puzzle,zero_x,zero_y,element_row,element_column,row,size)

	if element_column-column>0:
		(zero_x,zero_y)=zero(puzzle,starting_column,size)
		(zero_x,zero_y,flag)=shift_zero2(puzzle,zero_x,zero_y,element_row,element_column,column,row,size)
		if flag==1:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			element_column=element_column-1
			move.display(size,puzzle)


		(zero_x,zero_y,element_column)=shift_col_left(puzzle,zero_x,zero_y,element_row,element_column,column,size)

	if shuffle==1 and cornercase==0:
		if zero_x == size-3:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
			zero_y=zero_y+1
			move.display(size,puzzle)

		while zero_x<size-1:
			puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
			zero_x=zero_x+1
			move.display(size,puzzle)

		while zero_y>starting_column:
			puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
			zero_y=zero_y-1
			move.display(size,puzzle)

		puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
		zero_x=zero_x-1
		move.display(size,puzzle)

		puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
		zero_y=zero_y+1
		move.display(size,puzzle)

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

def puzzle_solver(puzzle,final_puzzle,start,size):
	if start==size-2:
		flag=0
		count=0
		(zero_x,zero_y)=zero(puzzle,start,size)
		if check(size,puzzle,final_puzzle):
			flag=1
		while count<12 and flag==0 :

			while zero_y<size-1:
				puzzle[zero_x][zero_y],puzzle[zero_x][zero_y+1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y+1)
				zero_y=zero_y+1
				count+=1
				move.display(size,puzzle)
				if check(size,puzzle,final_puzzle):
					flag=1
					return True

			while zero_x<size-1:
				puzzle[zero_x][zero_y],puzzle[zero_x+1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x+1,zero_y)
				zero_x=zero_x+1
				count+=1
				move.display(size,puzzle)
				if check(size,puzzle,final_puzzle):
					flag=1
					return True

			while zero_y>size-2:
				puzzle[zero_x][zero_y],puzzle[zero_x][zero_y-1]=swap(puzzle,zero_x,zero_y,zero_x,zero_y-1)
				zero_y=zero_y-1
				count+=1
				move.display(size,puzzle)
				if check(size,puzzle,final_puzzle):
					flag=1
					return True

			while zero_x>size-2:
				puzzle[zero_x][zero_y],puzzle[zero_x-1][zero_y]=swap(puzzle,zero_x,zero_y,zero_x-1,zero_y)
				zero_x=zero_x-1
				count+=1
				move.display(size,puzzle)
				if check(size,puzzle,final_puzzle):
					flag=1
					return True


		if flag==0:
			print "not possible"

	else:

		for column in range(start,size-2):

			current=start*size+column
			(i,j)=element(puzzle,start,size,current,final_puzzle)
			first_row(puzzle,size,start,column,i,j)

		current=start*size+size-1
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_row(puzzle,size,start,size-1,i,j)

		current=start*size+size-2
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_row(puzzle,size,start,size-2,i,j)

		for row in range(start+1,size-2):

			current=row*size+start
			(i,j)=element(puzzle,start,size,current,final_puzzle)
			first_column(puzzle,size,row,start,i,j)

		current=(size-1)*size+start
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_column(puzzle,size,size-1,start,i,j)

		current=(size-2)*size+start
		(i,j)=element(puzzle,start,size,current,final_puzzle)
		first_column(puzzle,size,size-2,start,i,j)

		puzzle_solver(puzzle,final_puzzle,start+1,size)


if __name__=="__main__":
	size=input("enter the size of the square matrix: ")
	print "enter the initial state of puzzle : "
	puzzle=[raw_input().strip().split()[:size] for i in range(size) ]
	print "enter the final state of the solver:"
	final_puzzle=[]
	for x in range(size):
		final_puzzle.extend(raw_input().strip().split()[:size])
	puzzle_solver(puzzle,final_puzzle,0,size)
