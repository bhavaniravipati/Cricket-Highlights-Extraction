import writeVideoClip

class ScoreBoardAnalysis:
    def __init__(self, inputPath):
        self.validTeamAbbreviations = ['CSK','RR','DD','RCB','KKR','MI','KXIP','DC']
        self.currentScoreVal = 0
        self.currentWicketCount = 0
        self.currentBallCount = 0
        self.currentBallStartTime = 0
        self.currentBallEndTime = 0
        self.isCurrentBallAnEvent = False
        self.videoWriter = writeVideoClip.WriteVideoClip(inputPath)
        

    def isTeamAbbreviation(self, inputVal):
        if inputVal in self.validTeamAbbreviations:
            return True
        else:
            return False
    
    def analyzeScoreBoard(self,scoreString, overString, frameTime):
        scoreString = scoreString.split('-')
        if(len(scoreString) == 2):
            currentScoreVal = scoreString[0]
            currentWicketCount = scoreString[1]
            try:
                if((int(currentScoreVal) - self.currentScoreVal) >= 4) or ((int(currentWicketCount) - self.currentWicketCount) >= 1):
                    #event detected
                    print('Event detected')
                    self.isCurrentBallAnEvent = True
                self.currentScoreVal = int(currentScoreVal)
                self.currentWicketCount = int(currentWicketCount)
            except ValueError:
                print(currentWicketCount)
        
        overString = overString.split('.')
        if(len(overString) == 2):
            #detect start & end of a ball
            currentBallCount =  int(overString[0])*6 + int(overString[1])
            if (currentBallCount - self.currentBallCount >= 1):
                self.currentBallEndTime = frameTime
                if (self.isCurrentBallAnEvent == True):
                    try:
                        self.videoWriter.clipFrame(self.currentBallCount, self.currentScoreVal, self.currentWicketCount, self.currentBallStartTime,self.currentBallEndTime)
                    except Exception:
                        print('Could not generate output clip for this event')
                # reset currentBallStartTime, currentBallEndTime, isCurrentBallAnEvent
                self.currentBallCount = currentBallCount
                self.isCurrentBallAnEvent = False
                self.currentBallStartTime = frameTime

        print('Runs :',self.currentScoreVal, 'Wickets : ',self.currentWicketCount)
        print('Balls : ', self.currentBallCount)