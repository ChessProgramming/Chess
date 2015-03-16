'''
Created on Mar 14, 2015

@author: Venkatesh
'''
from piece.image import get_image
from piece.piece import Piece


class Rook(Piece):
    '''
        Rook is a piece it can move horizontally and vertically
    '''


    def __init__(self, color, location):
        self.color = color
        self.location = location
        
        if(color == "white"):
            self.image = get_image("wR")
        else:
            self.image = get_image("bR")
        
    def is_possible(self, location,board):
        Piece.is_possible(self, location)

	xDiff = self.location[0] - location[0]
        yDiff = self.location[1] - location[1]
	if(self.color == "white"):
		colour = 1
	else:
		colour = -1

	if((xDiff == 0 or yDiff == 0) and (not(xDiff == 0 and yDiff == 0))):
		if(board[location[0]][location[1]] != colour):
			x = self.location[0]
			y = self.location[1]
			xinc=0
			yinc =0
			if(x > location[0]):
				xinc =-1
			else:
				xinc = 1
			if(y > location[1]):
				yinc = -1
			else:
				yinc = 1
			while(xinc !=0 and x != location[0]):
				x = x +	xinc
				if(x != location[0]):
					if(board[x][location[1]]!=0):
						return False	
			while(yinc !=0 and y != location[1]):
				y = y + yinc
				if(y != location[1]):
					if(board[location[0]][y] != 0):
						return False
			else:
				return False
		else:
			return False

	return True
		        
    def get_all_moves(self, board):
        Piece.get_all_moves(self)
	newLocation=[]
	x = self.location[0]
	y = self.location[1]
	if(self.color == "white"):
                colour = 1
        else:
                colour = -1
	while(x > 0):
		x -= 1
		if(board[x][self.location[1]] == 0):
			newLocation.append([x,self.location[1]])
			continue
		if(board[x][self.location[1]] == colour):
			break
		if(board[x][self.location[1]] == colour*-1):
			newLocation.append([x,self.location[1]])
			break
	x = self.location[0]
	while(x < 7):
		x +=1
		if(board[x][self.location[1]] == 0):
                        newLocation.append([x,self.location[1]])
                        continue
                if(board[x][self.location[1]] == colour):
                        break 
                if(board[x][self.location[1]] == colour*-1):
                        newLocation.append([x,self.location[1]])
                        break
	while(y > 0):
                y -= 1
                if(board[self.location[0]][y] == 0):
                        newLocation.append([self.location[0],y])
                        continue
                if(board[self.location[0]][y] == colour):
                        break 
                if(board[self.location[0]][y] == colour*-1):
                        newLocation.append([self.location[0],y])
                        break
        y = self.location[1]
        while(y < 7):
                y +=1
                if(board[self.location[0]][y] == 0):
                        newLocation.append([self.location[0],y])
                        continue
                if(board[self.location[1]][y] == colour):
                        break
                if(board[self.location[1]][y] == colour*-1):
                        newLocation.append([self.location[0],y])
                        break
		
	
	return newLocation

