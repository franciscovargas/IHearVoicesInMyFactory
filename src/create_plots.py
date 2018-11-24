from scipy.io import wavfile
import os
import scipy
import scipy.signal as sig
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser

from os import path, listdir, curdir


notebook_path = path.realpath(__file__)
data_path = path.join(path.dirname(path.dirname(notebook_path)), "data")
audio_path = path.join(data_path, "Sample Audio")
good_plots = path.join(data_path, "good_examples")

fss = []
datas = []
files  =[]

for file_ in listdir(good_plots):
   fs,data = wavfile.read(path.join(good_plots, file_))
   fss.append(fs)
   _filename = str(parser.parse(file_.split("_")[-1].split(".")[0]))
   files.append(_filename.replace(":", "_"))
   # import pdb; pdb.set_trace()
   datas.append(data)

# datas = datas[]
for i in range(len(datas)):
   print(i)
   # if i < 8: continue
   plt.figure()
   plt.plot(datas[i])
   plt.savefig(files[i])
   plt.clf()
