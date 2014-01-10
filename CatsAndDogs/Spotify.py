class Voter:        
    def __init__ (self, winner, loser):
        self.data=[]
        self.winner=winner
        self.winnerMatch=0
        self.loser=loser
        self.loserMatch=0
        self.satisfied=False
        
    def checkSatisfied(self):
        """The goal is to make as many people happy as possible.
            checkSatisfied will return True iff at winnerMatch+loserMatch is at least 1
            (the variable satisfied is also updated here)
            This means that at least one of their votes is reflected in the final
            outcome"""
        if (self.winnerMatch+self.loserMatch >0):
            self.satisfied=True
            return True
        return False

    def isWinnerMatch(self, ID):
        """This method updates the value of winnerMatch.
        If ID (the petID of a potential winner) matches self.winner (the petID of the voter's choice to win)
        winnerMatch is set to 1.  This is useful later when checking to see if this Voter is satisfied.
        Returns True if winnerMatch is updated, else False"""
        if (ID==self.winner):
            self.winnerMatch=1
            return True
        return False

    def isLoserMatch (self, ID):
        """Basically the same as isWinnerMatch, except about Losers, not Winners...
        This method updates the value of loserMatch.
        If ID (the petID of a potential loser) matches self.loser (the petID of the voter's choice to lose)
        loserMatch is set to 1.  This is useful later when checking to see if this Voter is satisfied.
        Returns True if loserMatch is updated, else False"""
        if (ID==self.loser):
            self.loserMatch=1
            return True
        return False



voters = []

def initVoters():
    V1= Voter ("C1", "D1")
    V2= Voter ("C1", "D1")
    V3= Voter ("C1", "D2")
    V4= Voter ("D2", "C1")
    global voters
    voters = [V1, V2, V3, V4]
    
contestantWIN={}
contestantLOSE={}

def createContestants(num):
    print num
    """initializes the dictionaries for contestantWIN and LOSE to contain the correct number of Cats and Dogs
    int num is taken in as a parameter to designate the total number of 1 type of animal"""
    for x in xrange (num):
        contestantWIN["C"+str(x+1)]=0
        contestantWIN["D"+str(x+1)]=0
        contestantLOSE["C"+str(x+1)]=0
        contestantLOSE["D"+str(x+1)]=0
##    print contestantWIN
##    print contestantLOSE

def highlander ():
    """I know it's really bad practice to name your methods obscure things,
    but this method makes sure there is exactly one value set to 1 in contestantWIN and LOSE.
    Why? BECAUSE THERE CAN ONLY BE ONE
    ...If you don't want to hire me on the grounds of a bad joke...that'd be pretty understandable

    Regardless, this method is run at the end just to make sure we actually came up with an answer
    returns TRUE if so, else FALSE"""
    winTotal=0
    loseTotal=0
    for x in contestantWIN.values():
        winTotal+=x

    for x in contestantLOSE.values():
        loseTotal+=x

    if (winTotal==1 and loseTotal==1):
        if (contestantWIN!= contestantLOSE):
            return True
    return False

def iterateThroughChoices():
    """Goes through every combination of winner and loser pet that does not involve
    the same pet winning and losing, prints out the number of voters happy with
    the best possible result"""
    bestHappiness = 0
    for win in contestantWIN.keys():
        contestantWIN[win]=1
        for lose in contestantLOSE.keys():
            if (win == lose):
                continue
            else:
                contestantLOSE[lose]=1
                newHappiness = calculateFitness (win, lose)
                if (newHappiness > bestHappiness):
                    bestHappiness = newHappiness
                contestantLOSE[lose]=0
        contestantWIN[win]=0
    print bestHappiness


def calculateFitness(win, lose):
    """Method that takes in the pet IDs of the current combination of
    winning and losing pets.  Iterates through all of the voters to see how
    satisfying such an answer would be""" 
    satisfiedVoters=0
    for voter in voters:
        voter.isWinnerMatch(win)
        voter.isLoserMatch(lose)
        if(voter.checkSatisfied()):
            satisfiedVoters= satisfiedVoters+ 1
            voter.winnerMatch=0
            voter.loserMatch=0
    return satisfiedVoters


initVoters()  
createContestants(4)
print "DONE"
iterateThroughChoices()


        

