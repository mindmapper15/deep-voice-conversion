import os
import glob
import datetime
from numpy import savez
from hparam import hparam as hp

from data_load import get_mfccs_and_spectrogram

def preprocessing(dataset_path):
    wav_files = glob.glob(dataset_path)
    for i in range(len(wav_files)):
        f_name = wav_files[i].replace('wav', 'npz')
        mfccs, mag_db, mel_db = get_mfccs_and_spectrogram(wav_files[i])
        savez(f_name, mfccs=mfccs, mag_db=mag_db, mel_db=mel_db)


if __name__ == '__main__':
    hp.set_hparam_yaml('temp')
    dataset_path = './datasets/'
    dataset_name = input("Write your dataset's path in \'datasets\' folder : ")
    dataset_path = dataset_path + dataset_name + '/*.wav'
    print(dataset_path)
    
    s = datetime.datetime.now()
    
    preprocessing(dataset_path)
    
    e = datetime.datetime.now()
    diff = e - s
    print("Done. elapsed time:{}s".format(diff.seconds))
