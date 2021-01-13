import pafy

url=input("Enter the Youtube link here : ")
res=pafy.new(url)

print("Title of the Video :" ,res.title,"\n")
print("Author of the Video :" ,res.author,"\n")
print("Duration of the Video :" ,res.duration,"\n")
print("Ratings of the Video :" ,res.rating,"\n")
print("Length of the Video :" ,res.length,"\n")

def vidonly():
    print("Please enter the format in which you want to download\n"
          "1.mp4 ","\n","2.webm","\n","3.flv","\n","4.3gp","\n","5.mov","\n","6.mkv","\n")
    opt=input()
    if (opt=="mp4" or opt=="webm" or opt=="flv" or opt=="3gp" or opt=="mov" or opt=="mkv"):
        video = res.getbestvideo(opt)
        video.download()
    else :
        print("Not prefered format")
        exit()


def audonly():
    print("Please enter the format in which you want to download\n"
          "1.m4a","\n","2.flac","\n","3.mp3","\n","4.mp4","\n","5.ogg","\n","6.aac","\n")
    opt=input()
    if (opt=="m4a" or opt=="flac" or opt=="mp3" or opt=="mp4" or opt=="ogg" or opt=="aac"):
        audio = res.getbestaudio(opt)
        audio.download()
    else :
        print("Not prefered format")
        exit()


def vidaud():
    print("Please enter the format in which you want to download\n"
          "1.mp4 ","\n","2.webm","\n","3.flv","\n","4.3gp","\n","5.mov","\n","6.mkv","\n")
    opt = input()
    if (opt == "mp4" or opt == "webm" or opt == "flv" or opt == "3gp" or opt == "mov" or opt == "mkv"):
        vidad = res.getbest(opt)
        vidad.download()

    else:
        print("Not prefered format")
        exit()

def can():
        exit()


print("You want to download : ")
print("1.Video only ")
print("2.Audio only ")
print("3.Video with audio ")
print("4.Cancel ")
n= int(input("Enter your option : "))

if n==1:
    vidonly()
elif n==2:
    audonly()
elif n==3:
    vidaud()
elif n==4:
    exit()
else:
    print("Invalid Option!!!\n")
