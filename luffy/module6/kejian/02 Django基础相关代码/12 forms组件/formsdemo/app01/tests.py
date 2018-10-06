from django.test import TestCase

# Create your tests here.




import  requests


res=requests.get("http://www.ixxplayer.com/video.php?url=https://ixx.cnd-youku.com/20171216/Ty80asUW/index.m3u8")

with open("a.mp4","wb") as f:

    f.write(res.content)