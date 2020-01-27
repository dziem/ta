dir = r"O:\Agony stuff\TA\data\Skin Care Talk\Thread Make Up Remover and Facial Cleanser Part 2"
rawFile = dir + r"\raw selected [25].txt"
autoFile = dir + r"\raw divided [20].txt"
manualFile = dir + r"\raw divided [5].txt"

f = open(rawFile, "r", encoding='utf-8')
lines = f.readlines()

posts = []
#print(lines[0][:5])
i = 0
for line in lines:
    if line[:5] == '-----':
        if i == 0:
            str = ''
            str += line
        else:
            posts.append(str)
            str = ''
            str += line
    else:
        str += line
    i += 1
    
posts.append(str)
    #print(line)
f.close()

#auto_list = []
#manual_list = []

fileAuto = open(autoFile,'w', encoding='utf-8') 
fileManual = open(manualFile,'w', encoding='utf-8') 

for i in range(len(posts)):
    if i % 5 == 4:
        fileManual.write(posts[i])
        fileManual.write('\n')
    else:
        fileAuto.write(posts[i])
        fileAuto.write('\n')

fileAuto.close()
fileManual.close()