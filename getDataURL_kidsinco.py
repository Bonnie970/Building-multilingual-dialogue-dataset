import urllib
import re,cgi

urls_file = open('source urls vm.txt','r')
urls = urls_file.read().split("\n")
#print urls
lookFor = "www.kidsinco.com"
filePath = 'C:\\Users\\Amar Kumar\\Dropbox\\Courses\\COMP 551-AML\\Project1\\DataSet\\'
all_address = []
for url in urls:
    if(lookFor in url):

        fileName = url.split(":",1)[0].rstrip()
        #print fileName
        address = url.split(":",1)[1].lstrip()
        if(not(address in all_address)): #checking that the same address is not visited again
            all_address.append(address)
            print '{} : {}'.format(fileName,address)
            dummy_file = open("dummy.txt",'w')
            link = urllib.urlopen(address) 
            myfile = link.read()
            dummy_file.write(myfile)
            dummy_file.close()
            lines_file = myfile.split('\n')
            conv_file = open('C:\\Users\\akumar47\\Dropbox\\Courses\\COMP 551-AML\\Project1\\DataSet\\{}.txt'.format(fileName),'w')
            conv_file.write('#{}.txt : {}\n'.format(fileName,address))
            for each_line in lines_file:
                
                if(':</span>' in each_line.replace(' ','')):
                    if('NARRADOR' in each_line or 'web Kidsinco.com' in each_line or 'Guion en Ingles' in each_line or 'GUION' in each_line):
                        continue
                    #print each_line
                    escape_chars = re.compile(r'(<!--.*?-->|<[^>]*>)')
                    
                    # all the tags are removed here
                    no_tags = escape_chars.sub('', each_line)
                    cleaned_each_line = cgi.escape(no_tags)
                    cleaned_each_line = cleaned_each_line.lstrip().rstrip()
                    #print cleaned_each_line
                    conv_file.write(cleaned_each_line+'\n')
            conv_file.close()
            #break
            #print lines_file
print "!Done!"
            