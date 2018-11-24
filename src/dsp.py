import scipy.signal as sig
import scipy.io.wavfile
from data_paths import good_plots, bad_plots
from os import listdir, path
import numpy as np
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt


def downsample(signal, old_sampling_rate, new_sampling_rate, method="fft",
               save=True, file_loc="default_sig.wav"):

    methods = {"fft": sig.resample, "mean": lambda x: x}

    d = np.max(signal.shape)
    new_sample_number =  int(np.ceil(d *  (float(new_sampling_rate) / old_sampling_rate)))
    print(new_sample_number, d)
    resamp_signal = methods[method](signal, new_sample_number)

    scipy.io.wavfile.write(file_loc, new_sampling_rate, resamp_signal)
    print("sampled signal")
    return resamp_signal


def downsample_folder(folder_path_in, folder_path_out, new_hz):

    def worker(file_path):
         f, s = scipy.io.wavfile.read(file_path)
         downsample(s, f, new_hz, )

    files = [path.join(folder_path, x) for x in listdir(folder_path)]

    pool = Pool(processes=cpu_count())

    pool.map(worker, files)


def spectrogram(signal, hz, plot=True):
    frequencies, times, spectrogram = sig.spectrogram(signal, hz)

    if plot:
        plt.pcolormesh(times, frequencies, spectrogram)
        plt.imshow(spectrogram[:25,:])
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()

    return (frequencies, times , spectrogram)



if __name__ == '__main__':

    gfiles_ = listdir(good_plots)
    bfiles_ = listdir(bad_plots)

    g = gfiles_[-2]
    b = bfiles_[0]

    print(g, b)
    fs, st = scipy.io.wavfile.read(path.join(bad_plots, b))
    fs, st2 = scipy.io.wavfile.read(path.join(good_plots, g))
    friend = st2[:-44100*60]
    # long_boy = np.concatenate((friend.reshape(1,-1), st2.reshape(1,-1)), axis =1).flatten()
    # spectrogram(st[:1000000], fs)
    nyquist = 22050
    new_hz = 22050
    # signal = downsample(st2[:1000000], fs, max(new_hz, nyquist) )
    length = 10000
    # plt.plot( np.linspace(0,19, len(st2[:length])), st2[:length])
    # plt.show()
    spectrogram(st[-50000:], fs)
    plt.show()
    spectrogram(st[:50000], fs)
    plt.show()
    spectrogram(st[5000000 - 800000:5000000+50000-800000], fs)
    # import ipdb; ipdb.set_trace()
