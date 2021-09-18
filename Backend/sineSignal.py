import os
import eel
import numpy as np
import pylab as plt
import struct as stu
import timeit
import pyaudio


signalParamsTest = {
    "message": '',
    "freq": 440
}


def character2AmplitudeValues(character: str = '', maxAmp: int = 100, alphabetLen: int = 27):

    _character2AmplitudeValues = {
        'a': maxAmp / alphabetLen*(alphabetLen),
        'b': maxAmp / alphabetLen*(alphabetLen-1),
        'c': maxAmp / alphabetLen*(alphabetLen-2),
        'd': maxAmp / alphabetLen*(alphabetLen-3),
        'e': maxAmp / alphabetLen*(alphabetLen-4),
        'f': maxAmp / alphabetLen*(alphabetLen-5),
        'g': maxAmp / alphabetLen*(alphabetLen-6),
        'h': maxAmp / alphabetLen*(alphabetLen-7),
        'i': maxAmp / alphabetLen*(alphabetLen-8),
        'j': maxAmp / alphabetLen*(alphabetLen-9),
        'k': maxAmp / alphabetLen*(alphabetLen-10),
        'l': maxAmp / alphabetLen*(alphabetLen-11),
        'm': maxAmp / alphabetLen*(alphabetLen-12),
        'n': maxAmp / alphabetLen*(alphabetLen-13),
        'o': maxAmp / alphabetLen*(alphabetLen-14),
        'p': maxAmp / alphabetLen*(alphabetLen-15),
        'q': maxAmp / alphabetLen*(alphabetLen-16),
        'r': maxAmp / alphabetLen*(alphabetLen-17),
        's': maxAmp / alphabetLen*(alphabetLen-18),
        't': maxAmp / alphabetLen*(alphabetLen-19),
        'u': maxAmp / alphabetLen*(alphabetLen-20),
        'v': maxAmp / alphabetLen*(alphabetLen-21),
        'w': maxAmp / alphabetLen*(alphabetLen-22),
        'x': maxAmp / alphabetLen*(alphabetLen-23),
        'y': maxAmp / alphabetLen*(alphabetLen-24),
        'z': maxAmp / alphabetLen*(alphabetLen-25),
        ' ': maxAmp / alphabetLen*(alphabetLen-26)
    }
    print(character)
    print(_character2AmplitudeValues[character])
    return _character2AmplitudeValues[character]
# character2AmplitudeValues


eel.init('../Frontend/dist')


def createWavFile(nameFile, samples):

    if(os.path.isdir('../sound') == False):
        os.mkdir('../sound/')
    fileWav = open('../sound/'+nameFile+'.wav', 'wb')

    for sample in samples:
        fileWav.write(stu.pack('b', int(sample)))

    fileWav.close()

    return True
# createWavFile


def playSound(samples):
    p = pyaudio.PyAudio()

    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=44100, output=True)
    stream.write(samples)
    stream.stop_stream()
    stream.close()

    p.terminate()

    return False
# playSound


@eel.expose
def testing(dummy_param):
    return "string_value", 1, 1.2, True, [1, 2, 3, 4], {"name": "eel"}
# testing


def createSignal(character: str = signalParamsTest["message"], fc: int = signalParamsTest["freq"]):
    Fs = 44100
    Amp = character2AmplitudeValues(character)
    duration = 1/(4*fc)

    # tic = np.round(timeit.default_timer() * 1000, 3);
    x = np.arange(Fs * duration)*fc/Fs
    samples = (Amp * np.sin(2 * np.pi * x)).astype(np.float32)
    # toc = np.round(timeit.default_timer() * 1000, 3);

    return samples
# createSignal


def sendMessage(signalParams: dict):
    for i in range(0, len(signalParams["message"])):
        character = signalParams["message"][i]
        samples = createSignal(character, signalParams["freq"])
        playSound(samples)
        createWavFile(character, samples)
# sendMessage


@eel.expose
def main(signalParams: dict = signalParamsTest):
    sendMessage(signalParams)
# main


eel.start('index.html', size=(1000, 600), port=8080)
