#-------------Importing modules---------------

from os import getcwd,chdir,system
from time import sleep
from random import choice
from sys import platform
#-----------Packages auto install-------------
try:
  import youtube_dl
  from googlesearch import search  
except:
  print("Downloading Libraries.. (about 3mb)")
  system("python3 -m pip install youtube-dl google")
  import youtube_dl
  from googlesearch import search

#-----------------Variables----------------------

options_mp3={
'format':'bestaudio/best',
'keepvideo':False}

options_mp4 = {}

options = {"v":options_mp4,"a":options_mp3}

#------------------Functions-----------------------
def get_user_agent():
  filename = "user_agents.txt"

  with open(filename) as f:
     user_agents = f.readlines()
  return str(choice(user_agents).replace("\n", ""))
  
  
def cls():
  if platform == "win32":
   system("cls")
  else:
    system("clear")

#-----------------------------------------------------

def get_url():
 print("How would you like to download the video?")
 ch = input("1> By Video Title\n2> By URL\n>>>>> \t")
 
 if "1" in ch:
  query = input("Enter the video title:—\n(Please specify in quite detail)\n>>>>>\t")
  vidname = query+" original video youtube"
  links = [] 
  for x in search(query=vidname,
  tld="com",
  num=3,
  stop=3,
  pause=2,
  user_agent=get_user_agent() ):
   links.append(x)  
  video_url = links[0]
 elif "2" in ch:
  video_url = input("Enter the URL of the video\n>>>>>\t")
  query = input("By which name would you like to save it ?\n>>>>>\t")
 else:
  exit("Invalid Choice, Try again later...")
 global songname
 songname = query
 return video_url

#----------------------------------------------------- 
def get_type():
 print("In which format would you like to download it?")
 ch = input("1> Audio\n2> Video\n>>>>>\t")
 if "1" in ch:
  type = "a"
 elif "2" in ch:
  type = "v"
 return type

#-----------------------------------------------------
 
def change_dir():
 print("Where do you want to save this song?")
 ch = input("1> Current Directory\n2> Internal Shared Storage (Android only)\n3> I want to specify my own path.\n>>>>>\t")
 if "1" in ch:
  path = getcwd()
 elif "2" in ch:
  folder = input("Please specify the folder where you want to save\nLeave blank to save not in any folder\n(Eg: myfolder/subfolder)\n>>>>>\t")
  path = "/storage/emulated/0/"+folder
 elif "3" in ch:
  path = input("Please specify the path\n>>>>>\t")
 chdir(path)

#-----------------------------------------------------

def download(video_url,type):
    if type == "v":
     ext = ".mp4"
    elif type == "a":
     ext = ".mp3"
     
    video_info = youtube_dl.YoutubeDL().extract_info(
 url = video_url,download=False)
    
    withext = getcwd()+"/"+songname.title()+ext
    
    options_mp3={
    'format':'bestaudio/best',
    'keepvideo':False,"outtmpl":withext}
    options_mp4 = {"outtmpl":withext}

    options = {"v":options_mp4,"a":options_mp3}
    
    with youtube_dl.YoutubeDL(options[type]) as ydl:
        ydl.download([video_info['webpage_url']])
    return songname

#--------------End of Functions-----------------
    
    
#------------------Main Code---------------------
            
if __name__ == "__main__":
 print("Welcome,\n")
 url = get_url()
 cls()
 type = get_type()
 cls()
 change_dir()
 cls()
 vidname = download(url,type)
 cls()
 print(f"{vidname} has been successfully downloaded!")