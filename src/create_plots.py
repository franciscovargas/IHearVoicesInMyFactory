from scipy.io import wavfile
import os
import scipy
import scipy.signal as sig
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import parser

from data_paths import bad_plots, good_plots
from os import listdir, path


def plot_signals(wav_dir):
    fss = []
    datas = []
    files  =[]

    for file_ in listdir(wav_dir):
       fs,data = wavfile.read(path.join(wav_dir, file_))
       fss.append(fs)
       _filename = str(parser.parse(file_.split("_")[-1].split(".")[0]))
       files.append(_filename.replace(":", "_"))
       datas.append(data)

    for i in range(len(datas)):
       print(i)
       plt.figure()
       plt.plot(datas[i])
       plt.savefig(files[i])
       plt.clf()


if __name__ == '__main__':
    plot_signals(bad_plots)
    plot_signals(good_plots)
