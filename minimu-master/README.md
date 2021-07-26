# minimu
the name came from 'mini music player'

a small, hidden and clean lightweight music player

fork from [michaelgundlach/mp3play](https://github.com/michaelgundlach/mp3play), updated to support python3 and unicode file name

only for python3, windows, mp3

some songs can't play, I don't know why

**New feature**: keep waking up the Bluetooth devices by playing silent song every 100s

### how to use
0. install
```
pip install git+https://github.com/nightttt7/minimu
```

1. play one song
```
import minimu

# load the file
s=minimu.load(r'example.mp3')

# play
s.play()

# pause
s.pause()

# resume
s.resume()

# stop
s.stop()

# True: play or pause | False: stop
s.isplaying()

# set volume%
s.volume(50) 
```

2. play one folder
```
import minimu

# load the floder
li = minimu.loadlist(r'testmusic')

# show play list
li.shownames()

# play music 1
li.play()

# play music 6
li.play(6)

# same with single song play
li.pause()
li.resume()
li.stop()
li.isplaying()
li.volume(80)

# play next one
# sorry it can't auto play next, do it by hand
li.next()

# play last one
li.last()

# stop playing
li.stop()
```

3.Keep waking up Bluetooth devices
```
import minimu
minimu.wakeup()
# or run wakeup.bat
```

---

# minimu [中文]
名字取自mini music player

一个小巧,隐蔽,干净的超轻量音乐播放器

Fork自[michaelgundlach/mp3play](https://github.com/michaelgundlach/mp3play), 更新以支持python3和unicode文件名.

只支持python3, windows平台, mp3格式

有些歌无法播放, 我也不知道原因

**新功能**: 每100秒播放无声音乐, 保持蓝牙音响开启
