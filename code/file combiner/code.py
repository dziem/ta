import os
rootdir = 'O:\Agony stuff\TA\data'

ff1 = open('dataTrain.tsv','w', encoding='utf-8') 
#ff2 = open('dataTest.tsv','w', encoding='utf-8') 
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file == 'labeled_divided_4.tsv':
            pile = os.path.join(subdir, file)
            f = open(pile, "r", encoding='utf-8')
            lines = f.readlines()
            for line in lines:
                ff1.write(line)
            ff1.write('\n')
            ff1.write('\n')
            f.close()
        '''
        elif file == 'labeled_divided_1.tsv':
            pile = os.path.join(subdir, file)
            f = open(pile, "r", encoding='utf-8')
            lines = f.readlines()
            for line in lines:
                ff2.write(line)
            ff2.write('\n')
            ff2.write('\n')
            f.close()
        '''
ff1.close()
#ff2.close()