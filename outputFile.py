import numpy as np
from os import listdir
from os.path import isfile, join
import re
import matplotlib.pyplot as plt
import time

start_time = time.time()
#useful functions
def removeSymbols(s):
    #\xc2\xa1- is the inverted exclamation symbol
    symbols = "!@#$%^&*()_+-=~`;[]{}\|,./<>?\xc2\xa1"
    for i in s:
        if (i in symbols):
            s = s.replace(i,"")    
    return s

#path for the file where conversations are placed
path = 'C:\\Users\\Amar Kumar\\Dropbox\\Courses\\COMP 551-AML\\Project1\\DataSet\\'
#path = 'C:\\Users\\akumar47\\Dropbox\\Courses\\COMP 551-AML\\Project1\\DataSet\\'
directoryFiles = [files for files in listdir(path) if isfile(join(path, files))]
outFile = open('ExistingCorpus_spa_final.xml','w')
outFile.write('<dialog>\n')
statsFile = open('ExistingCorpusStats_spa_final.txt','w')
statsFile.write('Filename \t #words \t #people \t #new words \t #utterances\n')
print directoryFiles
total_utterances = 0
new_words = [] #array to store any new words found in all the conversations
words_num = []
new_words_num = []
trials = 1

for convFile in directoryFiles:
    file_read = open(path+convFile,'r')
    #if(trials==600):
        #break
    #trials += 1

    #print (convFile)
    if(not("ep-" in convFile)):
        continue
    statsFile.write(convFile+'\t')
    message = file_read.read()
    file_read.close()
    #for a single conversation
    outFile.write('<s>')
    lines = message.split('\n')
    #iterating over every element in the array read from the file
    i = 1
    speakers = []
    speech = []
    speaker_id = {}
    total_words = 0;
    total_new_words = 0;
    words = []
    
    #new_words =[]
    i_newWords = 0
    flag = True
    for line in lines:
        if(flag):
            flag = False;
            continue
        if(len(line)==0 or not(':' in line)): #ignoring the case when there is an empty line
            continue
        a = line.split(':') #a is just a temporary variable for each line
        s = (''.join(a[1:len(a)])).rstrip().lstrip()
        words = s.split(' ')
        #print a
        words = map(removeSymbols,words)
        #print words
        total_words += len(words)
        #print s
        a[0] = a[0].rstrip().lstrip()
        
        for w in words:
            if(not(w in new_words)):
                new_words.append(w)    #placing any of the new words found in the new_words array
                total_new_words += 1
                i_newWords = i_newWords+1
        
        speech.append(s)      
        if(not(a[0] in speaker_id.values())):
            speakers.append(a[0])
            speaker_id[i] = a[0]
            i= i+1
        #print speakers
        outFile.write('<utt uid = "{}">{}</utt>'.format( {v: k for k, v in speaker_id.iteritems()}.get(a[0]),s))
    words_num.append(total_words)
    new_words_num.append(total_new_words)
    statsFile.write('{}\t{}\t{}\t{}\n'.format(total_words,len(speaker_id),total_new_words,len(lines)-1))
    total_utterances += len(lines)-1 
    outFile.write('</s>\n')

#plots are generated here    
print words_num
pathPlot = 'C:\\Users\\Amar Kumar\\Dropbox\\Courses\\COMP 551-AML\\Project1\\Plots\\'
#pathPlot = "C:\\Users\\akumar47\\Dropbox\\Courses\\COMP 551-AML\\Project1\\Plots\\"
fig, ax = plt.subplots()
width = 0.2
xind = np.arange(len(words_num))
rect1 = ax.bar(xind,words_num,width,label = '# of Words')
rect2 = ax.bar(xind+width,new_words_num,width,label = ' # of new words')
ax.set_ylabel('Occurance of words')
ax.set_xlabel('Conversation File number')
ax.axis([0-width, len(words_num)+1, min(words_num)-5, max(words_num)+5])
ax.legend()
#ax.xticks(np.arange(0, len(words_num)+1, 1))
ax.set_xticks(xind + width / 2)
ax.set_xticklabels(directoryFiles)
name1 = "Number Plot"
for item in ([ax.title, ax.xaxis.label, ax.yaxis.label]):
    item.set_fontsize(15)
plt.savefig(pathPlot+name1) 
#plt.show()        

outFile.write('</dialog>')
outFile.close()
statsFile.close()
print "Total utternaces: {}".format(total_utterances)
end_time = time.time()
print "Time taken : {}".format(end_time-start_time)
print "!Done!"      
    