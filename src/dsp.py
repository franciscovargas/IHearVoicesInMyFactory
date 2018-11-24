import scipy.signal as sig
import scipy.io.wavfile
from data_paths import good_plots, bad_plots, bad_plots2
from os import listdir, path
import numpy as np
from multiprocessing import Pool, cpu_count
import matplotlib.pyplot as plt

from scipy.signal import butter, lfilter


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band', analog=False)
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


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
    # print hz
    # import pdb; pdb.set_trace()
    frequencies, times, spectrogram = sig.spectrogram(signal, hz)
    # import pdb; pdb.set_trace()
    # plt.plot(st, times)
    if plot:
        size = 25
        plt.pcolormesh(times[:], frequencies[:size], spectrogram[:size, :])
        # plt.imshow(spectrogram[:,:])
        plt.ylabel('Frequency [Hz]')
        plt.xlabel('Time [sec]')
        plt.show()

    return (frequencies, times , spectrogram)



if __name__ == '__main__':

    gfiles_ = listdir(good_plots)
    bfiles_ = listdir(bad_plots2)

    g = gfiles_[-2]
    b = bfiles_[0]

    print(g, b)
    fs, st = scipy.io.wavfile.read(path.join(bad_plots2, b))
    fs, st2 = scipy.io.wavfile.read(path.join(good_plots, g))

    sto = st
    st = butter_lowpass_filter(st, 600, 44100)
    t =  np.linspace(0, 19, len(st))
    plt.plot(t[], st)
    plt.show()
    # plt.plot
    # st = st2
    # friend = st2[:-44100*60]
    # long_boy = np.concatenate((friend.reshape(1,-1), st2.reshape(1,-1)), axis =1).flatten()
    # spectrogram(st[:1000000], fs)
    nyquist = 22050
    new_hz = 22050
    # signal = downsample(st2[:1000000], fs, max(new_hz, nyquist) )
    length = 10000
    # plt.plot( np.linspace(0,19, len(st2[:length])), st2[:length])
    # plt.show()
    print st.shape
    spectrogram(st[:2646000*10], fs)
    plt.show()
    spectrogram(st[-2646000*6:], fs)
    plt.show()
    spectrogram(st[2646000*6:2646000*2*6], fs)
    plt.show()
    mid= int(max(st.shape) * 0.5)
    spectrogram(st[mid :mid +   2646000*2  ], fs)
    # import ipdb; ipdb.set_trace()
