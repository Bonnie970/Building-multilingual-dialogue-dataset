# Building-multilingual-dialogue-dataset
Couple of useful codes for building a database containing multiple conversations in a specified language.
Description of the files present

link to the Dataset folder on dropbox: https://www.dropbox.com/sh/9m3dhhsydyonksc/AAAieYzU0ptzFUF2qs6NxgnSa?dl=0
------------------------------------------------------------------------------------------------------------------------------
source urls vm.txt - contains the source url of different websites from where data can be loaded

spanish dictionary.txt - a txt format of the words in spanish dictionary

StatsDataSample_spa_final.txt - complete statistics of all the words that are to be analyzed including the one from EU proceedings

getDataURL_kidsico.py - script to download plays from the web and then process it

outputFile.py -  the main script to generate the xml file. One has to be careful to execute this paths needs to be modified and the Dataset on which the script is running also needs to be checked. In the current state it will build a corpora from the EU proceedings.

outputStats.py - script to outptut the main statistics of a file

outputStats_amar.py - a modified version of outputStats.py for a defined purpose of knowing the statistics of an exisiting corpora

