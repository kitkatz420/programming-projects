import glob
import os
from pydub import  AudioSegment
import shutil

maindir = "C:\\Users\\cats\\Desktop\\tts\\sounds\\"


def copyy(filename):
	target = r'C:\Users\cats\Desktop\tts\copyall'
	shutil.copy(filename,target)


gen = "C:\\Users\\cats\\Desktop\\tts\\gen\\gen.wav"

pathDis = {'hi': maindir + 'hi.wav','my':maindir + 'my.wav','name':maindir+'name.wav','is':maindir+'is.wav','cats':maindir+'cats.wav','and':maindir + 'and.wav','this':maindir + 'this.wav','what':maindir + 'what.wav','I':maindir + 'I.wav','wanted':maindir + 'wanted.wav','to':maindir + 'to.wav','tell':maindir + 'tell.wav','you':maindir + 'you.wav','very':maindir+'very.wav','good':maindir+'good.wav','laptop':maindir + 'laptop.wav'}

# hi = AudioSegment.from_wav(maindir + 'hi.wav')
# my = AudioSegment.from_wav(maindir + 'my.wav')
# name = AudioSegment.from_wav(maindir + 'name.wav')
# _is = AudioSegment.from_wav(maindir + 'is.wav')
# cats = AudioSegment.from_wav(maindir + 'cats.wav')
# _and = AudioSegment.from_wav(maindir + 'and.wav')
# this = AudioSegment.from_wav(maindir + 'this.wav')
# what = AudioSegment.from_wav(maindir + 'what.wav')
# I = AudioSegment.from_wav(maindir + 'I.wav')
# wanted = AudioSegment.from_wav(maindir + 'wanted.wav')
# to = AudioSegment.from_wav(maindir + 'to.wav')
# tell = AudioSegment.from_wav(maindir + 'tell.wav')
# you = AudioSegment.from_wav(maindir + 'you.wav')
# very = AudioSegment.from_wav(maindir + 'very.wav')
# good = AudioSegment.from_wav(maindir+'good.wav')
#
# audioDis = [hi,my,name,_is,cats,_and,this,what,I,wanted,to,tell,you,very,good]

#00000000000000000000000000000000000
input = input("Type your text here:-  ")


# filenameswithbeep = [hi,my,name,_is,cats]

# copyy(pathDis['my'])
# copyy(pathDis['hi'])
# copyy(pathDis['name'])
# copyy(pathDis['is'])
# copyy(pathDis['cats'])
#hi my name
#['hi','my','name']
def mainMan(inp):
	combined = AudioSegment.empty()
	res = inp.split()
	filenames = glob.glob('C:\\Users\\cats\\Desktop\\tts\\copyall\\' + '*.wav')
	sss = 'C:\\Users\\cats\\Desktop\\tts\\copyall\\' + '*'
	filenameswithbeep = []

	for i in res:
		copyy(pathDis[i])

	for ss in res:
		xx = AudioSegment.from_wav(maindir + ss + '.wav')
		filenameswithbeep.extend(xx)

	for fname in filenameswithbeep:
		combined += fname

	for tt in os.listdir('C:\\Users\\cats\\Desktop\\tts\\copyall\\'):
		os.remove(os.path.join('C:\\Users\\cats\\Desktop\\tts\\copyall\\',tt))

	combined.export(gen, format="wav")

mainMan(input)
