import numpy as np
from os import listdir
from os.path import isfile, join
import re
import matplotlib.pyplot as plt
import time

from collections import Counter

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
#path = 'C:\Users\dell1\Dropbox\COMP 551\Project1\DataSet'
path = "C:\\Users\\akumar47\\Dropbox\\Courses\\COMP 551-AML\\Project1\\DataSet"
directoryFiles = [files for files in listdir(path) if isfile(join(path, files))]

directoryFiles = [files for files in listdir(path) if isfile(join(path, files))]

#statsFile = open('StatsDataSample_spa_test_final.csv','w')
statsFile = open('StatsDataSample_spa_test_final.txt','w')
statsFile.write('Filename,#words,#people,#new words,#utterances,#turn,word-frequency\n')

total_utterances = 0
new_words = [] #array to store any new words found in all the conversations
words_num = []
new_words_num = []
trials = 1
total_word_freq = Counter({})

file_count = 0
total_file = len(directoryFiles)
for convFile in directoryFiles:
    #if convFile not in ['europarl-v7.es-en.es']: continue
    
    file_count += 1
    #print 'Processing File {}/{}'.format(file_count,total_file)
    
    file_read = open(join(path,convFile),'r')    
    message = file_read.read()
    file_read.close()
    lines = message.split('\n')
    #iterating over every element in the array read from the file
    i = 1
    speakers = []
    speaker_id = {}
    total_words = 0
    total_new_words = 0
    
    turn = 0
    last_spkr = ''
    file_word_freq = Counter({})
    file_word_list = []
    
    i_newWords = 0
    flag = True
    for line in lines:
        if(flag):
            flag = False
            continue
        if(len(line)==0 or not(':' in line)): #ignoring the case when there is an empty line
            continue
        a = line.split(':') #a is just a temporary variable for each line
        s = (''.join(a[1:len(a)])).rstrip().lstrip()
        words = s.split(' ')
    
        words = map(removeSymbols,words)
	words = [x for x in words if x!='']
    
        total_words += len(words)
    
        a[0] = a[0].rstrip().lstrip()
        
        for w in words:
            if(not(w in new_words)):
                new_words.append(w)    #placing any of the new words found in the new_words array
                total_new_words += 1
                i_newWords = i_newWords+1
		
	#count word frequency, add to file word counter
	file_word_list += words#dict((x,words.count(x)) for x in words)
	#file_word_freq += Counter(utt_word_freq)
		
        if(not(a[0] in speaker_id.values())):
            speakers.append(a[0])
            speaker_id[i] = a[0]
            i= i+1
        #count turns
	if last_spkr=='':
	    last_spkr = a[0]
	elif (a[0]!=last_spkr):
	    turn += 1
	    last_spkr = a[0]

    words_num.append(total_words)
    new_words_num.append(total_new_words)
    file_word_freq = Counter(dict((x,file_word_list.count(x)) for x in file_word_list))
    file_word_freq_formatted = ''
    for word,freq in file_word_freq.most_common():
        file_word_freq_formatted += ('{}:{},'.format(word,freq))
    statsFile.write('{},{},{},{},{},{},{}\n'.format(convFile,total_words,len(speaker_id),total_new_words,len(lines)-1,turn,file_word_freq_formatted))
    total_utterances += len(lines)-1 
	
    total_word_freq += file_word_freq

statsFile.close()
    
#file_w_f = open('word_freq_count_test_final.csv','w')
file_w_f = open('word_freq_count_test_final.txt','w')
file_w_f.write('word,frequency\n')
for item in total_word_freq.most_common():
    file_w_f.write('{},{}\n'.format(item[0],item[1]))
file_w_f.close()

'''
#plots are generated here    
#pathPlot = 'C:\\Users\\Amar Kumar\\Dropbox\\Courses\\COMP 551-AML\\Project1\\Plots\\'
pathPlot = "C:\\Users\\akumar47\\Dropbox\\Courses\\COMP 551-AML\\Project1\\Plots\\"
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
'''

print "Total utternaces: {}".format(total_utterances)
end_time = time.time()
print "Time taken : {}".format(end_time-start_time)
print "!Done!"      
    
