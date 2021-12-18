# e314-music-visualization
Fall 2021 ECEN 314 Honors Project

Howdy! Welcome to my Music Visualization Project! Here is the story ... 

Checkout the demo video here: https://youtu.be/O8_USCbpqz8

The instruction of how to use these codes is listed in the how_to_use.txt and is also down at the bottom
A great appreciation to Mina PECHEUX, I mainly use her code in the animation portion.

Original Thoughts...
My intial intention was to create a visualizer that can help people with hearing diabilities to "hear" the music in another format: visualization. Therefore, I was thinking about make patterns based on the lyrics. However, I found that to be too difficult to achieve at my current level because the design and the programming portion would needs a lot of resources, and the core part of the project might be shifted since the emphasis will be on signals and systems. 

Currently, I have provided code that will conver .mp3 file into a .wav file which can be used to perform frequency analysis and draw plots based on the Fast FOurier Transform. 

Future Implementation Idea:
1. Various colors through the waveform instead of just one selection
2. (A far stretch goal)Combine with other APIs (hope there would be one) that can show related patterns based on the lyris


Music Visualizer
------------
Saini Ye & E314 [December 2021]

Credit to:
Mina PECHEUX
Based on the work by Yu-Jie Lin
(Public Domain)
Github: https://gist.github.com/manugarri/1c0fcfe9619b775bb82de0790ccb88da

LICENSE: CC0 (Public Domain) - see the file in the archive for more info

DISCLAIMERS:
  - all bash scripts use ffmpeg, so you need to install it first if
    you don't have it yet (https://ffmpeg.org/)
  - for now, the project only works with .wav and .mp4 files
  - all scripts and commands except file names WITHOUT their extension
  - the Python script doesn't automatically merge the audio and video
    (see step 4)


TL;DR:
------
A test audio file of some fingers snapping is provided with the scripts to
easily try out the project. Here is the entire process to get a fully finished
generated video:

  0. (optional) Start a virtual environment
  1. Install the Python packages:

      ~$ pip install -r requirements.txt
  
  2. Convert the .mp3 to .wav file (you may skip if you have the .wav filr already)

    (1) python3 data_manip.py

    (2) Following the input promp, type in the filename, For example:

        test.mp3

        And the output file will be test.wav in the same directory, it will also gives you 4 graphs: double and single channel fft spectrumand spectrogram

  2. Convert the test audio file, which is mono, to stereo:

      ~$ bash convert_to_stereo.sh test

  3. Create the video from the sound file (may take a while):
    
      ~$ python main.py -m bars -c "#ddddff" --output test_stereo

      (hints: The input after the -m gives the pattern options: bars, wave, spectrum, rain)
      (hints: The input after the -c gives the color option in hexadecimal format)

  4. Merge the video and the audio:

      ~$ bash add_audio_to_video.sh -a test_stereo -v test_stereo

  5. Your final video is now available: it's the "test_stereo_processed.mp4" file 


Reference:
https://pythonbasics.org/convert-mp3-to-wav/

https://towardsdatascience.com/understanding-audio-data-fourier-transform-fft-spectrogram-and-speech-recognition-a4072d228520

https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files

https://medium.com/nerd-for-tech/how-to-visualize-music-using-python-5db9440ab23e
