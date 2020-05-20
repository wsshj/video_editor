# 语音播报模块
import pyttsx3

# 模块初始化
engine = pyttsx3.init()

print('准备开始语音播报...')

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 70)

# # 设置要播报的Unicode字符串
# engine.say("君不见，黄河之水天上来，奔流到海不复回。")

# # 等待语音播报完毕
# engine.runAndWait()

f = open('text.txt', 'r', encoding='utf-8')

text = f.read()

engine.save_to_file(text, 'abc.mp3')
print(type(engine))

engine.runAndWait()