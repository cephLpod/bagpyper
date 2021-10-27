import numpy as np
from scipy.io.wavfile import write, read


#infile = "500Miles.wav"
infile = "./piano.wav"			#file from https://github.com/MTG/sms-tools
dronefile = "./dronemono.wav"		#file from https://freesound.org/people/lonemonk/sounds/32878/
bagpyperfile = "./bagpyperAdd.wav"

fs, x = read(infile)
fsd, d = read(dronefile)

print(fs)
print(x.size)
print(fsd)
print(d.size)

if fs != fsd:
	print('Sample frequencies are not equal.')

if x.size > d.size:
	N = np.ceil(x.size/d.size)
	dtile = np.tile(d, int(N))
	dloop = dtile[1:x.size + 1]
	
	y = 0.15 * x + 0.1 * dloop
	y = 0.01 * y
	
else:
	print('Input file is too short.')

write(bagpyperfile, fs, y)
