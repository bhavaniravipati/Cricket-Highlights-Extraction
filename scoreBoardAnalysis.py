class ScoreBoardAnalysis:
    def __init__(self):
        self.validTeamAbbreviations = ['CSK','RR','DD','RCB','KKR','MI','KXIP','DC']
        self.currentScoreVal = 0
        self.currentWicketCount = 0
        self.currentBallCount = 0

    def isTeamAbbreviation(self, inputVal):
        if inputVal in self.validTeamAbbreviations:
            return True
        else:
            return False
    
    def analyzeScoreBoard(self,scoreString, overString):
        scoreString = scoreString.split('-')
        if(len(scoreString) == 2):
            currentScoreVal = scoreString[0]
            currentWicketCount = scoreString[1]
            try:
                if((int(currentScoreVal) - self.currentScoreVal) >= 4) or ((int(currentWicketCount) - self.currentWicketCount) >= 1):
                    #event detected
                    print('Event detected')
                self.currentScoreVal = int(currentScoreVal)
                self.currentWicketCount = int(currentWicketCount)
            except ValueError:
                print(currentWicketCount)
        
        overString = overString.split('.')
        if(len(overString) == 2):
            #detect start & end of a ball
            self.currentBallCount =  int(overString[0])*6 + int(overString[1])

        print('Runs :',self.currentScoreVal, 'Wickets : ',self.currentWicketCount)
        print('Balls : ', self.currentBallCount)