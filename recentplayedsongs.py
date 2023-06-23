songname = int(input('Enter a song name: '))
Recent_playlist = ["s1","s2","s3"]
new_playlist=[]
while songname != 0:
    
    
    s = "s"+str(songname)
    print("Old playlist " + str(Recent_playlist))
    
    if s in Recent_playlist:
        
        Recent_playlist.remove(s)
    if songname==0:
        brake;
    else:   
       
        Recent_playlist.append(s)
    new_playlist=Recent_playlist[-3::]
    print("New playlist " + str(new_playlist))
        
    
    
    
    songname = int(input('Enter a song name: '))

print("song name is invalid ")    