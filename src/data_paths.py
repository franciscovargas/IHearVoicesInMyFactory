from os import path, listdir, curdir


notebook_path = path.realpath(__file__)
data_path = path.join(path.dirname(path.dirname(notebook_path)), "data")
audio_path = path.join(data_path, "Sample Audio")
good_plots = path.join(data_path, "good_examples")
bad_plots = path.join(data_path, "failure_examples")
bad_plots2 = path.join(data_path, "bad3")
# bad_plots2 = path.join(data_path, "bad5")
