import math
class Checkers:
    def __init__(self,state, player):
        if state is None:
            self.gamestate = dict()
            for row in range(0,8):
                for col in range(0,8):
                    self.gamestate[row,col] = ' '
        else:
            self.gamestate=state

        self.whoseTurn=player

    def loadCharacters(self):
        for row in range(0, 8):
            for col in range(0, 8):
                if row<=2 and ((row+col)%2!=0):
                    self.gamestate[row,col]='w'
                if row>=5 and ((row+col)%2==1):
                    self.gamestate[row,col]='b'



    def __str__(self):
        s=""
        for r in range(0,8):
            for c in range(0,8):
                s += self.gamestate[r,c]
        return s
    def display(self):
        """
                       A pleasant view of the current game state
                       :return: nothing
                       """
        for row in range(0, 8):
            print("+-+-+-+-+-+-+-+-+")
            print("|", end="")
            for column in range(0, 8):
                print(self.gamestate[row, column], end="")
                print("|", end="")
            #print(self.gamestate[row, 6], end="")
            print("")
        print("+-+-+-+-+-+-+-+-+")

    def isWhiteMoveValid(self,iR,iC,fR,fC):  ##This function should be edited to handle when a charactre becomes king
        if self.gamestate[fR,fC]=='w':
            return False

        if fR-iR==1 and abs(iC-fC)==1:
            ##if self.gamestate[fR,fC]=='b':

            return True
        return False


