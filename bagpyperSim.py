import numpy as np
from scipy.io.wavfile import write, read

infile = "./piano.wav"				#file from https://github.com/MTG/sms-tools
bagpyperfile = "./bagpyperSim.wav"		

fs, x = read(infile)
print(fs)
print(x.size)

timearr = np.arange(x.size) / fs

fb = 482/2
ft = 482/1
fh = 708

dronebass = np.sin(2 * np.pi * fb * timearr)
dronetenor = np.sin(2 * np.pi * ft * timearr)
droneharm = np.sin(2 * np.pi * fh * timearr)

y = 0.25 * x  400 * dronebass + 900 * dronetenor + 700 * droneharm
y = 0.1 * y

write(bagpyperfile, fs, y)
