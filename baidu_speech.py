from aip import AipSpeech
 
""" 你的 APPID AK SK """
APP_ID = '19948902'
API_KEY = 'S4fy84Km1Ayp2zheNhaPYR53'
SECRET_KEY = 'mqgS4MdVk2iH0V5gPyaIqxkw06ZctEKs'
 
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

f = open('text.txt', 'r', encoding = 'utf-8')

text = f.read()
 
result  = client.synthesis(text, 'zh', 1, {
    'vol': 5,'per':0,'spd':4
})
 
 
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)