import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime
from gtts import gTTS

import os

while True :
    
 robot_ear = speech_recognition.Recognizer()
 with speech_recognition.Microphone() as mic:
    print("robot : I'm listening")
    audio = robot_ear.record(mic, duration= 5)
    print("\nSiri: ....")
    audio=robot_ear.listen(mic)
 try:
    you=robot_ear.recognize_google(audio,language='vi-VN')
 except:
    you=" "
 print("you:" +you)
 if  "chào" in you :
     robot= "xin chào bạn tên là gì "
 elif "tên" in you:
      robot="chào bạn nghe giọng nói bạn thật ấm áp  bạn quê ở đâu"
 elif "ở" in you:
      robot="wow đó là một vùng quê tuyệt vời bạn có hay về quê không"
 elif "có" in you:
      robot="vậy thì khi nào về cho tôi theo với nhé tạm biệt bạn"
      print ("robot : " + robot)
 elif "không" in you:
      robot="tại sao vậy"
 elif "vì" in you:
      robot="vậy thì hãy về quê thường xuyên nhé tôi rất thích vùng đất đó tạm biệt bạn "
      print ("robot : " + robot)
      
 elif "tháng" in you:
      robot="tôi cũng vậy nhưng bạn có người yêu chưa"
 elif "rồi" in you:
      robot="ôi yêu đương gì tầm này bạn ơi chào người có tình yêu nhé bye"
      print ("robot : " + robot)

 elif "chưa" in you:
      robot="đúng là con người của công việc phải lo cho tương lai trước đã tạm biệt bạn nhé bye"
      print ("robot : " + robot)

 elif "tuần" in you:
      robot="tôi cũng vậy nhưng bạn có người yêu chưa"
 elif "ngày" in you :
    today=date.today()
    robot=today.strftime("%B %d, %Y")
 elif "giờ" in you :
    now= datetime.now()
    robot=now.strftime("%H hour %M minutes %S seconds")
 elif "biệt" in you:
     robot="bye dương hẹn gặp lại dương nhé yêu dương nhiều"
     print ("robot : " + robot)

     robot_speech = gTTS(text=robot, lang='vi')
     robot_speech.save("Siri.mp3")
     os.system("start Siri.mp3")
     os.remove("Siri.mp3")
     break

 else:
    robot="xin lỗi tôi không nghe rõ bạn có thể nói lại không "
    print ("robot : " + robot)


 robot_speech = gTTS(text=robot, lang='vi')
 robot_speech.save("Siri.mp3")
 os.system("start Siri.mp3")
 os.remove("Siri.mp3")

 