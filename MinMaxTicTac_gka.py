import math

class Game:

    def __init__(self): 

        self.board = [['_','_','_'],['_','_','_'],['_','_','_']]
        self.playerTurn = 'AI'

    def drawBoard(self):

        boardStr = ''
        for i in range(0,3):
            boardStr = boardStr + self.board[i][0] + ' ' + self.board[i][1] + ' ' + self.board[i][2] + '\n'
            
        print(boardStr+'****************')
        

    def isValid(self,i,j):

        if i<0 or i>2 or j<0 or j>2:
            return False

        if self.board[i][j] == 'O' or self.board[i][j] == 'X':
            return False
        
        return True 
    
    def getSuccessors(self,move):

        listOfSuccessors = []
        
        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == '_':
                    self.board[i][j] = move
                    listOfSuccessors.append((self.board[:],i,j))
                    self.board[i][j] = '_'
                    
        return listOfSuccessors

    def utilityFxn(self):

        for x in range(0,3):
            if self.board[x] == ['X','X','X']:
                return 1

            if self.board[x] == ['O','O','O']:
                return -1

            if self.board[0][x] == self.board[1][x] == self.board[2][x]  == 'X':
                return 1
                    
            if self.board[0][x] == self.board[1][x] == self.board[2][x]  == 'O':  
                return -1

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X':
            return 1

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':
            return 1

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O':
            return -1
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':
            return -1

        return 0

    def max(self):

        maximum,i_max,j_max = -math.inf,None,None 

        for i in range(0,3):
            for j in range(0,3):

                if self.board[i][j] == '_':

                    self.board[i][j] = 'X'

                    if self.isEnd():
                        utilityOfSuccessor =  self.utilityFxn()
                    else:
                        utilityOfSuccessor,_,_ =  self.min()

                    if utilityOfSuccessor >= maximum:
                        maximum,i_max,j_max = utilityOfSuccessor,i,j

                    self.board[i][j] = '_'
    
        return maximum,i_max,j_max


    def min(self):

        minimum,i_min,j_min = math.inf,None,None

        for i in range(0,3):
            for j in range(0,3):

                if self.board[i][j] == '_':
                    
                    self.board[i][j] = 'O'

                    if self.isEnd():
                        utilityOfSuccessor =  self.utilityFxn()
                    else:
                        utilityOfSuccessor,_,_ =  self.max()

                    if utilityOfSuccessor <= minimum:
                        minimum,i_min,j_min = utilityOfSuccessor,i,j

                    self.board[i][j] = '_'

        return minimum,i_min,j_min 

    def isEnd(self):

        for x in range(0,3):
            if self.board[x] == ['X','X','X'] or self.board[x] == ['O','O','O'] or (self.board[0][x] == self.board[1][x] == self.board[2][x]  != '_'):
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '_':
            return True 

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '_':
            return True 

        for i in range(0,3):
            for j in range(0,3):
                if self.board[i][j] == '_':
                    return False 
        
        return True 

    def getResult(self):

        s1 = 'AI is a winner'
        s2 = 'Well done - you have beaten AI'
        s3 = 'Its a draw'

        for x in range(0,3):
                if self.board[x] == ['X','X','X']:
                    return s1

                if self.board[x] == ['O','O','O']:
                    return s2

                if self.board[0][x] == self.board[1][x] == self.board[2][x]  == 'X':   
                    return s1
                        
                if self.board[0][2] == self.board[1][1] == self.board[2][0] == 'X':
                    return s1

                if self.board[0][x] == self.board[1][x] == self.board[2][x]  == 'O':   
                    return s2
                
                if self.board[0][2] == self.board[1][1] == self.board[2][0] == 'O':
                    return s2

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'X':
            return s1
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == 'O':
            return s2

        return s3


    def play(self):

        while True:
            
            self.drawBoard()

            if self.isEnd():
                print(self.getResult())
                break 

            # max 
            if self.playerTurn == 'AI':

                u,i,j = self.max()

                self.board[i][j] = 'X'
                
                if self.isEnd():
                    self.getResult()

                self.playerTurn = 'User'
                

            #min user turn 
            else:
               
                while(True):
                    i = int(input('Input i: '))
                    j = int(input('Input j: '))
                    
                    if self.isValid(i,j):
                        self.board[i][j] = 'O'

                        if self.isEnd():
                            print(self.getResult())

                        self.playerTurn='AI'
                        break 
                    else:
                        print('Invalid move, Try Again!')
            
g = Game()
g.play()
