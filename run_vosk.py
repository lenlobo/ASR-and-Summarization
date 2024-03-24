import os
import glob

model_list = ['vosk-model-de-0.21',
              'vosk-model-de-tuda-0.6-900k']

vid_files = glob.glob('/home/dlobo/videos/*.mp4')
for vid_path in vid_files:
  vid_name=vid_path.split('/')[-1].split('.')[0]
  i=0
  for model_name in model_list:
      i=i+1
      print("Running Model: ",model_name)
      command = 'vosk-transcriber -n {} -i {} -o /home/dlobo/outputs/from_vid/{}_{}.txt'.format(model_name,vid_path,vid_name,model_name)
      os.system(command)


# wav_files = glob.glob('/home/dlobo/videos/*.wav')
# for wav_path in wav_files:
#   i=0
#   wav_name=wav_path.split('/')[-1].split('.')[0]
#   for model_name in model_list:
#       i=i+1
#       print("Running Model: ",model_name)
#       command = 'vosk-transcriber -n {} -i {} -o /home/dlobo/outputs/from_wav/{}_{}.txt'.format(model_name,wav_path,wav_name,i)
#       os.system(command)