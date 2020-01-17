filename = './three.mov'

from moviepy.editor import VideoFileClip
import numpy as np

from PIL import Image

clip = VideoFileClip(filename)


# np.zeros is how we generate an empty ndarray
img = np.zeros((clip.size[1], clip.size[0], 3), dtype='uint8')
#creates a blank black image to past "slices" into. The width & height is equal to width & height of the video. numpy is y first then x

currentX = 0
slitwidth = 1
#slitpoint = clip.size[0] // 2 #starting point, should be less than the clip size.
slitpoint = clip.size[1] // 2 #starting point, should be less than the clip size.

# generate our target fps with width / duration
target_fps = clip.size[0] / clip.duration

for i in clip.iter_frames(fps=target_fps, dtype='uint8'): #iterate through each of the video frames
    if currentX < (clip.size[0] - slitwidth): #making sure we are staying within the bounds of the image
        img[currentX:currentX + slitwidth,:,:] = i[slitpoint:slitpoint+slitwidth,:,:]
        # img[:,currentX:currentX + slitwidth,:] = i[:,slitpoint:slitpoint+slitwidth,:]
    currentX += slitwidth

output = Image.fromarray(img)
output.save('output6.png')