from os import walk
from os.path import isfile, join
import sys
from subprocess import call
#from html_parser import BasicParser
from HTMLParser import HTMLParser

total_no = 0;
version = 1.0
files = []
global_map = {}
ident_map = {}
uid = 1
output_file = '/home/hacker/Hackathon/results/train.fv.input'
DEFAULT_EXT = '/home/hacker/Hackathon/bin/SimpleHtmlExtractor'
USE_DEFAULT = False
class BasicParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start Tag Processing for", tag
        if tag == "meta":
            print attrs 
            for i in attrs: 
                if i[0] in "name":
                    if i[1] in "description":
            if index != -1 or index == None:
                word_list_unigram = jTokenize(attrs[index]) 
                for i in word_list_unigram:
                    if i in global_map:
                        count = global_map[i]
                        global_map[i] = count + 1
                    else:
                        global_map[i] = 1       
        print global_map

    def handle_endtag(self, tag):
        return
    def handle_data(self, data):
        print data.encode("UTF-8")

def files_for_extraction(mypath):
    for(dirpath, dirnames, filenames) in walk(mypath):
        files.extend(filenames)
        break

''' Now parse the train filenames 
    for category values'''

def parse_for_category(file):
    category = file.split('.')
    return category[-2]


def run():

    if len(sys.argv)<2:
        print "Usage:feature-extracotr.py <dir-path-of-files>"
        exit(1);

    '''Get the directory path'''
    mypath=str(sys.argv[1])
    print mypath
    files_for_extraction(mypath);
    with open(output_file,"w+") as of: of.close(); 
    for f in files:
        f = "9.jpcasino.org.2.content"
        if '.content' in f:
            print 'Training File'
            category = parse_for_category(f)
            train_file_sequence(mypath+f, category)
            #break
        else:
            print 'Test File'
            test_file_sequence(f)
            #break
    exit;

def train_file_sequence(filename, category):
    print filename
    if USE_DEFAULT == True:
        with open(output_file, "a") as of:
            of.write(category+"\t")
            of.close()
        with open(output_file, "a") as of:
            call([DEFAULT_EXT, filename],stdout = of)
            of.write("\n")
            of.close()
    else:
        parser = BasicParser()
        with open(filename, "r") as inp_f:
            raw_html = inp_f.read().decode("UTF-8")
            parser.feed(raw_html)
            for i in global_map:
                if i in ident_map:
                    print ident_map[i]
                else:
                    uid = uid+1
                    ident_map[i] = uid
                print global_map[i] 
            dummy = input("Press Enter to continue")
        
def test_file_sequence(filename):
    print filename
    if USE_DEFAULT == True:
        with open(output_file, "a") as of:
            call([DEFAULT_EXT, filename],stdout = of)
            of.write("\n")
            of.close()

if __name__ == "__main__":
    run()
