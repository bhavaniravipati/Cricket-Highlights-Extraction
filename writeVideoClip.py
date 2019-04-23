from moviepy.editor import VideoFileClip
import os
import shutil
class WriteVideoClip:
    def __init__(self, inputVideoPath):
        self.subDir = './clips/'
        if os.path.isdir(self.subDir):
            try:
                shutil.rmtree(self.subDir)
            except OSError as e:
                print ("Error: %s - %s." % (e.filename, e.strerror))
        os.makedirs(self.subDir)
        self.videoEditor = VideoFileClip(inputVideoPath)

    def clipFrame(self, ballNumber, score, wickets, startTime, endTime):
        new_clip = self.videoEditor.subclip(startTime, endTime)
        print('new clip duration : ',new_clip.duration)
        new_clip_name = self.subDir+'Ball_'+str(ballNumber)+'Score_'+str(score)+'Wickets_'+str(wickets)+'.mp4'
        new_clip.write_videofile(new_clip_name, codec="libx264", fps=25)
        new_clip.close()
    