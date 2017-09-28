from operator import methodcaller
statsFile = open('StatsDataSample_spa_test_final.txt','r')
#statsFile = open('dummy_test.txt','r')
message = statsFile.read()
lines = message.split('\n')
final_words =[[0,0]]
index = 0;
lcnt = 0;
for line in lines[1:]:
    #print map(split(':'),line)
    #print line
    if(not('convo' in line.strip().split(',')[0])):
        continue
    a = line.strip().split(',')[6:-1]
    b = map(methodcaller("split", ":"), a) #this is list of list
    b = [s for s in b if len(s)==2]
    c = zip(*b)[0] #this is tuple
    for str in c: #iterate over all the strings
        dummy = zip(*final_words)[0]
        if(len(str)==0):
            continue
        if(str in dummy):            
            idx = dummy.index(str)
            final_words[idx][1] = int(final_words[idx][1]) + int(b[c.index(str)][1])
        else:
            final_words.append(b[c.index(str)])
            if(index==0):
                del final_words[0]
                index = 1
    lcnt+=1
    print lcnt
print 'just wiriting'
output = open("words_frequency_conversation.txt",'w')
#print final_words
for item in final_words:
    if(len(item)==2):
        output.write("{}\t{}\n".format(item[0],item[1]))
    
output.close()
print "Done!"
#print final_words
#print len(final_words)
    #print map(methodcaller("split", ":"), line)
    


