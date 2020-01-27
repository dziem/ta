dir = r"O:\Agony stuff\TA\data\Skin Care Talk\Thread Make Up Remover and Facial Cleanser Part 2"
rawAutoFile = dir + r"\raw divided [20].txt"
rawManualFile = dir + r"\raw divided [5].txt"
autoFile = dir + r"\cleaned divided [20].txt"
manualFile = dir + r"\cleaned divided [5].txt"

fAuto = open(rawAutoFile, "r", encoding='utf-8')
lines = fAuto.readlines()
str = ''
for line in lines:
    if line != '\n' and line[:5] != '-----':
        str += line
fAuto.close()
fileAuto = open(autoFile,'w', encoding='utf-8') 
fileAuto.write(str)
fileAuto.close()

fManual = open(rawManualFile, "r", encoding='utf-8')
lines = fManual.readlines()
str = ''
for line in lines:
    if line != '\n' and line[:5] != '-----':
        str += line
fManual.close()
fileManual = open(manualFile,'w', encoding='utf-8') 
fileManual.write(str)
fileManual.close()