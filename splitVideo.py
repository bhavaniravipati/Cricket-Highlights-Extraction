import cv2
from moviepy.editor import VideoFileClip
from skimage.measure import compare_ssim
import os
from natsort import natsorted
from PIL import Image

def split_video(start,end):

    my_clip = VideoFileClip("/Users/bhavanirishitharavipati/Desktop/Full Match IPL 2010 MATCH32 - CSK vs RR, 2010-04-03 - YouTube.mp4" )
    # print("Duration of video : ", my_clip.duration)
    # print("FPS : ", my_clip.fps)

    new_clip = my_clip.subclip(start,end)
    print('new clip duration : ',new_clip.duration)
    new_clip.write_videofile("/Users/bhavanirishitharavipati/Desktop/sample1_clip.mp4", codec="libx264", fps=25)
    new_clip.close()

#compare_match_images("/Users/bhavanirishitharavipati/Desktop/Machine Learning/bowleraction/bnb13.jpg","/Users/bhavanirishitharavipati/Desktop/Machine Learning/live/bnb851.jpg")


def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()
 
 
    


def FrameCapture(path): 
      
    # Path to video file 
    vidObj = cv2.VideoCapture(path) 
  
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1
    
    #success, image_prev = vidObj.read() 
    
    #image_A = "/Users/bhavanirishitharavipati/Desktop/Machine Learning/bowleraction/bnb13.jpg"
  
    while success: 
  
        # vidObj object calls read 
        # function extract frames 
        success, image = vidObj.read() 
        
#        print(image.shape)
        
        #image = image.resize((360,64), Image.ANTIALIAS)
  
        # Saves the frames with frame-count 
        if(success):
            cv2.imwrite("/Users/bhavanirishitharavipati/Desktop/exp/%d.jpg" % count, image)
#             crop("/Users/bhavanirishitharavipati/Desktop/exp/"+str(count)+".jpg", (0,304,450,360), "/Users/bhavanirishitharavipati/Desktop/Machine Learning/cropped_image/"+str(count)+".jpg")
            
            
#             img = Image.open("/Users/bhavanirishitharavipati/Desktop/Machine Learning/cropped_image/"+str(count)+".jpg")
#             img = img.resize((161,81), Image.ANTIALIAS)
            
#             img.save("/Users/bhavanirishitharavipati/Desktop/Machine Learning/cropped_image/"+str(count)+".jpg")
            
#             crop_image("/Users/bhavanirishitharavipati/Desktop/exp/"+str(count)+".jpg",count)
            
            feature = extract_features_image("/Users/bhavanirishitharavipati/Desktop/exp/"+str(count)+".jpg")
        
            #print("hello")
            
            if(clf.predict(feature) == 1):
                os.remove("/Users/bhavanirishitharavipati/Desktop/exp/"+str(count)+".jpg")
#             else: 
#                 imageA = cv2.imread(image_A)
#                 imageB = cv2.imread("/Users/bhavanirishitharavipati/Desktop/exp/"+str(count)+".jpg")
#                 (score, diff) = compare_ssim(imageA, imageB, full=True, multichannel=True)
#                 if(score<0.6):
#                     os.remove("/Users/bhavanirishitharavipati/Desktop/exp/"+str(count)+".jpg")
            
            count += 1
            
    
            #image_prev = image
        

#split_video(522,720)
#FrameCapture("/Users/bhavanirishitharavipati/Desktop/sample1_clip.mp4")

#loop_over_frames()

#FrameCapture("/Users/bhavanirishitharavipati/Desktop/sample2_clip.mp4")