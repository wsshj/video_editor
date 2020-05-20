from moviepy.editor import *
from aip import AipSpeech

start = 60

f = open('testText.txt', 'r', encoding='utf-8')
text = f.read()

""" 你的 APPID AK SK """
APP_ID = '19948902'
API_KEY = 'S4fy84Km1Ayp2zheNhaPYR53'
SECRET_KEY = 'mqgS4MdVk2iH0V5gPyaIqxkw06ZctEKs'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis(text, 'zh', 1, {'vol': 5, 'per': 0, 'spd': 5})

if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

video = VideoFileClip("test.mp4")

audio = AudioFileClip('auido.mp3')
endtime = audio.end

v = video.subclip(start, start + endtime)
vv = v.set_audio(audio)
vv.write_videofile("test_%s.mp4" % '', fps=25)