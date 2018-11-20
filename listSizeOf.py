def solution(S):
    hd = S.split('\n')
    dlist = {'music': 0, 'images': 0, 'movies': 0, 'other': 0}
    for l in hd:
        line = str(l).split()
        name = line[0]
        size = int(line[1].split('b')[0])
        #print size
        other = True
        if music(name):
            inc = dlist['music'] + size
            dlist.update({'music': inc})
            other = False
        if images(name):
            inc = dlist['images'] + size
            dlist.update({'images': inc})
            other = False
        if movies(name):
            inc = dlist['movies'] + size
            dlist.update({'movies': inc})
            other = False
        if other:
            inc = dlist['other'] + size
            dlist.update({'other': inc})

    #print dlist['music']
    #print dlist
    output = 'music ' + str(dlist['music']) + 'b\n' + 'images ' + str(dlist['images']) + 'b\n' + 'movies ' + str(dlist['movies']) + 'b\n' + 'other ' + str(dlist['other']) + 'b'
    return output

def music(S):
    music = ['mp3','aac','flac']
    for m in music:
        if S.lower().find(m.lower()) != -1:
            return True

def images(S):
    images = ['jpg', 'bmp', 'gif']
    for i in images:
        if S.lower().find(i.lower()) != -1:
            return True

def movies(S):
    movies = ['mp4', 'avi', 'mkv']
    for m in movies:
        if S.lower().find(m.lower()) != -1:
            return True


    #word = "mp3"
    #if S.lower().find(word.lower()) != -1:
    #    return S

#print solution("mp3")



f = open("listSizeOf.txt","r")
for l in f:
    line = str(l).split()
    name = line[0]
    size = str(line[1].split('b')[0])
    #print name

#a = str(f.readline())
#print a

f.close()


S = "my.song.mp3 11b\ngreatSong.flac 1000b\nnot3.txt 5b\nvideo.mp4 200b\ngame.exe 100b\nmov!e.mkv 10000b"

#print S.split('\n')

print solution(S)