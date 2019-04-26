from moviepy.editor import VideoFileClip, concatenate_videoclips
clip1 = VideoFileClip("/home/dharshini/Documents/ML/code/1.mp4")
clip2 = VideoFileClip("/home/dharshini/Documents/ML/code/2.mp4")
final_clip = concatenate_videoclips([clip1,clip2])
final_clip.write_videofile("/home/dharshini/Documents/ML/code/my_concatenation.mp4")
