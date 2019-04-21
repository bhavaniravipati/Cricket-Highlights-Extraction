import cv2
import os
import math
import scoreboard
from google.cloud import vision
import base64
from PIL import Image
import scoreBoardAnalysis
class VideoExtractor:
    def __init__(self):
        self.ocrClient = vision.ImageAnnotatorClient()
        self.sBAnalyzer = scoreBoardAnalysis.ScoreBoardAnalysis()

    def analyzeFrame(self,frame, width, height):
        cropped_frame = frame[int(0.87*height):int(0.92*height), int(0.055*width):int(0.45*width)]
        #analyze frame and return a filled scoreboard object
        # cv2.imshow('image',cropped_frame)
        # cv2.waitKey(100)
        # cv2.destroyAllWindows()
        retval, buff = cv2.imencode('.jpg', cropped_frame)
        jpg_as_text = base64.b64encode(buff)
        jpg_original = base64.b64decode(jpg_as_text)
        imageFrame = vision.types.Image(content=jpg_original)
        response = self.ocrClient.text_detection(image=imageFrame)
        if response.error and response.error.code == 3:
            print(response.error.message)
        else:
            texts = response.text_annotations
            # for text in texts:
            #     print('\n"{}"'.format(text.description))
            # validate text annotations
            # should of of form "{full desc}" "{teamName}" "2-0" "OVERS:" "0.4"
            if(len(texts) >= 5 and self.sBAnalyzer.isTeamAbbreviation(texts[1].description) and (texts[3].description == 'OVERS:')):
                self.sBAnalyzer.analyzeScoreBoard(texts[2].description,texts[4].description)

        #score = scoreboard.Scoreboard()
        #return score
    def extractVideoFrames(self,inputPath):
        capture = cv2.VideoCapture(inputPath)
        count = 0
        #Get frameRate of the capture
        frameRate = capture.get(5)
        width = int(capture.get(3))
        height = int(capture.get(4))
        while(capture.isOpened()):
            currentFrameNo = capture.get(1)
            retVal, frame = capture.read()
            if retVal == True:
                if (currentFrameNo % math.floor(frameRate) == 0) and (currentFrameNo/math.floor(frameRate) > 675):
                    # print("Read frame : %d" % count)
                    # pass the current & prev frame to ocr code
                    self.analyzeFrame(frame, width, height)
                    count+=1
            else:
                break
        capture.release()
        cv2.destroyAllWindows()
        