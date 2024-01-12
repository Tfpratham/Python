import gtts
import playsound
# if __name__=='__main__':
#     print('welcome to robo speaker by pratham')
#     x= input('entre what you want me to speak:')
#     command =f"say {x}"
#     os.system(command)

text =input('tell something here:')
sound = gtts.gTTS(text,lang='hi')
sound.save('welcome.mp3')
playsound.playsound('welcome.mp3')
