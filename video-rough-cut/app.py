import scipy.io.wavfile
from pydub import AudioSegment
import os
import matplotlib.pyplot as plt
import numpy as np

# CONFIG
input_video_folder_path = os.path.join(os.path.dirname(__file__),"VideoFiles")
seconds_padding = 1
output_width=1920
output_height=1080

def get_files(folder, file_type):
    for file_name in sorted(os.listdir(folder)):
        if file_name.lower().endswith(file_type.lower()):
            yield os.path.join(folder, file_name)
            

if __name__ == '__main__':
    
    videos  = []
    for video in get_files(input_video_folder_path, file_type='.MP4'):
        videos.append(video)
        print(video)
        
        wav_filename = os.path.join(input_video_folder_path,os.path.splitext(os.path.basename(video))[0] + '.wav')
        AudioSegment.from_file(video).export(wav_filename,format='wav')
        
        rate,audData=scipy.io.wavfile.read(wav_filename)


        print(rate) # 48000 samples per second
        print(audData) #both channels of audio data

        

        channel1=audData[:,0] #left
        channel2=audData[:,1] #right
        duration = audData.shape[0]/rate
        print(duration)

        print(len(channel1))
        print(len(channel2))

        # Next - time to calculate at X seconds before something interesting happens.
        
        