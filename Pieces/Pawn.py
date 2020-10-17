from piece import Piece

class Pawn(Piece):
    def __init__(self,board,color,group,row,col):
        super().__init__(board,color,group,"Pawn",row,col)

    def availableMoves(self):
        #Returns a set of the avaiable moves the Pawn can make
        moves=set()
        #Up
        # ex row=2 col=C
        tempRow=self.row-1 #1
        tempCol=self.possibleCol[self.col] #2
        #if black:
        if self.color == 'BLACK':
            #top position
            if  0<=tempRow+1<=7 and self.board[tempRow+1][tempCol] is None:
                moves.add((tempRow+1,tempCol))

            #if at second col
            if tempRow==1 and self.board[tempRow+1][tempCol] is None and self.board[tempRow+2][tempCol] is None:
                moves.add((tempRow+2,tempCol))
                
            print((0<=tempRow+1<=7,0<=tempCol+1<=7,self.validMove(tempRow,tempCol)))

            #Now the capture moves
            if 0<=tempRow+1<=7 and 0<=tempCol-1<=7 and self.board[tempRow+1][tempCol-1] is not None and self.validMove(tempRow+1,tempCol-1):
                moves.add((tempRow+1,tempCol-1))
            if 0<=tempRow+1<=7 and 0<=tempCol+1<=7 and self.board[tempRow+1][tempCol+1] is not None and self.validMove(tempRow+1,tempCol+1):
                moves.add((tempRow+1,tempCol+1))
        else:
            #top position
            if  0<=tempRow-1<=7 and self.board[tempRow-1][tempCol] is None:
                moves.add((tempRow-1,tempCol))

            #if at second col
            if tempRow==6 and self.board[tempRow-1][tempCol] is None and self.board[tempRow-2][tempCol] is None:
                moves.add((tempRow-2,tempCol))
                
            print((0<=tempRow+1<=7,0<=tempCol+1<=7,self.validMove(tempRow,tempCol)))

            #Now the capture moves
            if 0<=tempRow-1<=7 and 0<=tempCol-1<=7 and self.board[tempRow-1][tempCol-1] is not None and self.validMove(tempRow-1,tempCol-1):
                moves.add((tempRow-1,tempCol-1))
            if 0<=tempRow-1<=7 and 0<=tempCol+1<=7 and self.board[tempRow-1][tempCol+1] is not None and self.validMove(tempRow-1,tempCol+1):
                moves.add((tempRow-1,tempCol+1))
        return moves
