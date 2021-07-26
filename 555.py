import os
from pygame import mixer 
import time
from tkinter import *
from PIL import Image
import math
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
import keyboard
from pynput import keyboard
import sounddevice
from tkinter import StringVar, IntVar
import minimu

win = Tk() # 如果使用直譯器的話，在這行Enter後就會先看到一個視窗了！
win.wm_attributes('-topmost',1)#顯示視窗在最上面
win.attributes("-alpha",1)#視窗透明
win.title('九宮格撥放器') # 更改視窗的標題
#win.configure(bg='black')
''
win.geometry('600x500') # 修改視窗大小(寬x高)
''
win.resizable(True, True)
devs = sounddevice.query_devices()
empty = []


for dev in devs:
    dev['name']
    dev['max_output_channels']
    if dev['max_output_channels']>=2:
        if (dev['hostapi'])==1:
            empty.append(dev['name'])
        
    
text = StringVar()
text.set('耳麥式耳機')
text1= StringVar()
text1.set('           1')
text2= StringVar()
text2.set('           2')
text3= StringVar()
text3.set('           3')
text4= StringVar()
text4.set('           4')
text5= StringVar()
text5.set('           5')
text6= StringVar()
text6.set('           6')
text7= StringVar()
text7.set('           7')
text8= StringVar()
text8.set('           8')
text9= StringVar()
text9.set('           9')



file_path_1="Ready.mp3"
file_name_1="1"
file_path_2="Ready.mp3"
file_name_2="2"
file_path_3="Ready.mp3"
file_name_3="3"
file_path_4="Ready.mp3"
file_name_4="4"
file_path_5="Ready.mp3"
file_name_5="5"
file_path_6="Ready.mp3"
file_name_6="6"
file_path_7="Ready.mp3"
file_name_7="7"
file_path_8="Ready.mp3"
file_name_8="8"
file_path_9="Ready.mp3"
file_name_9="9"

song = minimu.load(file_path_1)
###############################################
dev="耳麥式耳機 (2- Corsair VOID PRO Wireless Gaming Headset)"
volume=0.1
volume2=10
var = 0

ggg=0
print (var)


###############################################
# 按鍵事件
def on_press(event):
    #print('on_press: event:', event)
    #print('on_press: keysym:', event.keysym)
    #print(event.keysym)
   

    key=event.keysym
    print("鍵盤輸入為:"+key)
    
    
    if var==1:
        if key=="1":
            a()
        elif key=="2":
            b()
        elif key=="3":
            c()
        elif key=="4":
            d()
        elif key=="5":
            e()
        elif key=="6":
            f()
        elif key=="7":
            g()
        elif key=="8":
            h()
        elif key=="9":
            i()
        elif key=="Return":
            stop()
def on_release(event):
    #print('on_release: event:', event)
    #print('on_release: keysym:', event.keysym)
    #print('{0} release'.format(event.keysym))
    #print(event.keysym)



    if var==1 and event.keysym == 'Escape':
        print("exist program")
        win.destroy()

win.bind('<KeyPress>', on_press)
win.bind('<KeyRelease>', on_release)




###############################################
###############################################
def a():    
    file=file_path_1
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play()    
def aPath():
    global file_path_1
    global file_name_1
    file_path_1 = filedialog.askopenfilename()
    print(os.path.basename(file_path_1))
    file_name_1=os.path.basename(file_path_1)
    text1.set(file_name_1.replace('.mp3', '')) 
def b():
    file=file_path_2
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def bPath():
    global file_path_2
    global file_name_2
    file_path_2 = filedialog.askopenfilename()
    print(os.path.basename(file_path_2))
    file_name_2=os.path.basename(file_path_2)
    text2.set(file_name_2.replace('.mp3', '')) 
def c():
    file=file_path_3
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def cPath():
    global file_path_3
    global file_name_3
    file_path_3 = filedialog.askopenfilename()    
    print(os.path.basename(file_path_3))
    file_name_3=os.path.basename(file_path_3)
    text3.set(file_name_3.replace('.mp3', ''))   
def d():
    file=file_path_4
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def dPath():
    global file_path_4
    global file_name_4
    file_path_4 = filedialog.askopenfilename()    
    print(os.path.basename(file_path_4))
    file_name_4=os.path.basename(file_path_4)
    text4.set(file_name_4.replace('.mp3', ''))
def e():
    file=file_path_5
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def ePath():
    global file_path_5
    global file_name_5
    file_path_5 = filedialog.askopenfilename()    
    print(os.path.basename(file_path_5))
    file_name_5=os.path.basename(file_path_5)
    text5.set(file_name_5.replace('.mp3', ''))
def f():
    file=file_path_6
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def fPath():
    global file_path_6
    global file_name_6
    file_path_6 = filedialog.askopenfilename()    
    print(os.path.basename(file_path_6))
    file_name_6=os.path.basename(file_path_6)
    text6.set(file_name_6.replace('.mp3', ''))
def g():
    file=file_path_7
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def gPath():
    global file_path_7
    global file_name_7
    file_path_7 = filedialog.askopenfilename()    
    print(os.path.basename(file_path_7))
    file_name_7=os.path.basename(file_path_7)
    text7.set(file_name_7.replace('.mp3', ''))
def h():
    file=file_path_8
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def hPath():
    global file_path_8
    global file_name_8
    file_path_8 = filedialog.askopenfilename()    
    print(os.path.basename(file_path_8))
    file_name_8=os.path.basename(file_path_8)
    text8.set(file_name_8.replace('.mp3', ''))
def i():
    file=file_path_9
    mixer.init(devicename=dev)
    mixer.music.load(file)
    mixer.music.set_volume(volume)
    mixer.music.play()
    global song
    song=minimu.load(file)
    print (file)
    song.volume(volume2)
    song.play() 
def iPath():
    global file_path_9
    global file_name_9
    file_path_9 = filedialog.askopenfilename()    
    print(os.path.basename(file_path_9))
    file_name_9=os.path.basename(file_path_9)
    text9.set(file_name_9.replace('.mp3', ''))     
###############################################
def Check():
    global var
    if var==0:
        var=1
        print ("啟用鍵盤")
    else:
        var=0
        print ("停用鍵盤")
  
def change():
    mixer.quit()
    song.stop()
    global dev
    if dev=="耳麥式耳機 (2- Corsair VOID PRO Wireless Gaming Headset)":
        dev="CABLE Input (VB-Audio Virtual Cable)"
        print (dev)
        text.set('CABLE Input')
    else:
        dev="耳麥式耳機 (2- Corsair VOID PRO Wireless Gaming Headset)"
        print (dev)
        text.set('耳麥式耳機')
def stop():
    mixer.quit()
    song.stop()
 
def go(*args):   #处理事件，*args表示可变参数
    mixer.quit()
    song.stop()
    print(comboxlist.get()) #打印选中的值
    global dev
    dev=str(comboxlist.get())
    text.set(comboxlist.get())

 #CABLE Input (VB-Audio Virtual Cable)
 
############################################### 
#調整音量 
def up():
    global volume
    if volume<1:
        volume=round(volume,1)+0.1
        mixer.music.set_volume(volume)
        print (volume)
    global volume2
    if volume2<100:
        volume2=volume2+10
        song.volume(volume2)
        print (volume2)     
def down():
    global volume
    if volume>0:
        volume=round(volume,1)-0.1
        mixer.music.set_volume(volume)
        print (volume)
    global volume2
    if volume2>00:
        volume2=volume2-10
        song.volume(volume2)
        print (volume2)
def aaScale(asd):
    global volume
    volume=int(asd)/100
    print ("音量1:"+str(volume*100))
def bbScale(asd):
    global volume2
    volume2=int(asd)
    print ("音量2:"+str(volume2))

def attributes(asd):
    
    win.attributes("-alpha",asd)#視窗透明
          

###############################################        
###############################################    
#介面
label7= Button(win, textvariable=text7,anchor=W,width="10", height="4", command=g,wraplength =75)
label7.place(x = 0, y = 0)
        
label7= Button(win, text='7選取',width="5", height="4", command=gPath)
label7.place(x = 80, y = 0)
        
label4= Button(win, textvariable=text4,anchor=W,width="10", height="4", command=d,wraplength =75)
label4.place(x = 0, y = 100)

label4= Button(win, text='4選取',width="5", height="4", command=dPath)
label4.place(x = 80, y = 100)

label1= Button(win, textvariable=text1,anchor=W,width="10", height="4", command=a,wraplength =75)
label1.place(x = 0, y = 200)

label1= Button(win, text='1選取',width="5", height="4", command=aPath)
label1.place(x = 80, y = 200)


label8= Button(win, textvariable=text8,anchor=W,width="10", height="4", command=h,wraplength =75)
label8.place(x = 160, y = 0)
        
label8= Button(win, text='8選取',width="5", height="4", command=hPath)
label8.place(x = 240, y = 0)
        
label5= Button(win, textvariable=text5,anchor=W,width="10", height="4", command=e,wraplength =75)
label5.place(x = 160, y = 100)

label5= Button(win, text='5選取',width="5", height="4", command=ePath)
label5.place(x = 240, y = 100)

label2= Button(win, textvariable=text2,anchor=W,width="10", height="4", command=b,wraplength =75)
label2.place(x = 160, y = 200)

label2= Button(win, text='2選取',width="5", height="4", command=bPath)
label2.place(x = 240, y = 200)


label9= Button(win, textvariable=text9,anchor=W,width="10", height="4", command=i,wraplength =75)
label9.place(x = 320, y = 0)
        
label9= Button(win, text='9選取',width="5", height="4", command=iPath)
label9.place(x = 400, y = 0)
        
label6= Button(win, textvariable=text6,anchor=W,width="10", height="4", command=f,wraplength =75)
label6.place(x = 320, y = 100)

label6= Button(win, text='6選取',width="5", height="4", command=fPath)
label6.place(x = 400, y = 100)

label3= Button(win, textvariable=text3,anchor=W,width="10", height="4", command=c,wraplength =75)
label3.place(x = 320, y = 200)

label3= Button(win, text='3選取',width="5", height="4", command=cPath)
label3.place(x = 400, y = 200)
###############################################





labelchange= Label(win, textvariable=text,width="30", height="4",fg="blue",relief="ridge",wraplength =200)
labelchange.place(x = 0, y = 300)

labelstop= Button(win, text='stop',width="30", height="4", command=stop)
labelstop.place(x = 250, y = 300)

labelup= Button(win, text='^',width="5", height="6", command=up)
#labelup.place(x = 460, y = 20)

labeldown= Button(win, text='v',width="5", height="6", command=down)
#labeldown.place(x = 460, y = 150)

labelkey= Checkbutton(win,text="鍵盤輸入", variable=var,command=Check)
labelkey.place(x = 0, y = 400)


aScalText=Label(win, width=9, height=2,textvariable=text,wraplength =60,relief="ridge")
aScalText.place(x = 460, y = 0)

aScale=Scale(win,from_=100,to=0,length=230,digits=0,showvalue="1",width="20",command=aaScale)
aScale.place(x = 460, y = 40)
aScale.set(10)

bScalText=Label(win, width=9, height=2,text="監聽音量",wraplength =60,relief="ridge")
bScalText.place(x = 530, y = 0)

bScale=Scale(win,from_=100,to=0,length=230,digits=0,showvalue="1",width="20",command=bbScale)
bScale.place(x = 530, y = 40)
bScale.set(10)

attributesText=Label(win, width=9, height=2,text="透明度",wraplength =60,relief="ridge")
attributesText.place(x = 500, y = 290)

attributes=Scale(win,from_=1,to=0,length=100,digits=2,resolution=0.1,showvalue="1",width="20", orient="horizontal",command=attributes)
attributes.place(x = 480, y = 330)
attributes.set(1)


comvalue=tkinter.StringVar()#窗体自带的文本，新建一个值
comboxlist=ttk.Combobox(win,textvariable=comvalue,state="readonly") #初始化
comboxlist["values"]=(empty)
comboxlist.current(0)  #选择第一个
comboxlist.bind("<<ComboboxSelected>>",go)  #绑定事件,(下拉列表框被选中时，绑定go()函数)
comboxlist.place(x = 100, y = 400)                                     
print(comboxlist["values"])                            
###############################################

win.mainloop()     