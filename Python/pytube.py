from pytube import YouTube 
SAVE_PATH = "E:/" 
link=["https://www.youtube.com/watch?v=cBVGlBWQzuc"]
  
for i in link: 
    try:
        yt = YouTube(i) 
    except:     
        print("Connection Error") 
    mp4files = yt.filter('mp4') 
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    try: 
     
        d_video.download(SAVE_PATH) 
    except: 
        print("Some Error!") 
print('Task Completed!')
