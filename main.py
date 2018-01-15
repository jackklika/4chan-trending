import basc_py4chan
import nltk
import inspect
import time
from collections import Counter, OrderedDict
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import SpaceTokenizer
from nltk import pos_tag, ne_chunk
import numpy as np

#################################
# CHANGE SOME OF THESE VARIABLES!
board = 'g'
recordsdir = '/opt/4chan-records/'
threadcount = 1000 # Amount of threads to get. Set to "1000" or something for all threads, 10 for testing.

# Graph Variables
title = "/{}/ name frequency {}".format(board, time.time())
ylabel = "Proper Noun Count"
################################

# Download needed files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# nltk config
tokenizer = SpaceTokenizer()
stop = stopwords.words('english')

# 4chan config
txtboard = board
board = basc_py4chan.Board(board)

thread_ids = board.get_all_thread_ids()

n = 0
nnp_list= []
name = ""
namelist = []

for thread_id in thread_ids: # For every thread
    if board.thread_exists(thread_id) and n < threadcount:
        thread = board.get_thread(thread_id)
        postlist = thread.all_posts
        for post in postlist: # For every post in the thread
            dupelist = [] # A list of all the things that will be added to the list.

            for par in nltk.sent_tokenize(post.text_comment):
                tokens = nltk.tokenize.word_tokenize(par)
                tags = nltk.pos_tag(tokens)
                chunked_tag = ne_chunk(tags)
                for c in chunked_tag:
                    name = ""
                    if type(c).__name__ == 'tuple':
                        if c[1] == "PERSON":
                            dupelist.append(c[0])
                    elif type(c).__name__ == 'Tree':
                        if c.label() == "PERSON":
                            nnp_list.append(c)
                            for x in range(0, len(c)):
                                name += c[x][0] + " "
                            dupelist.append(name.strip())
                            print(dupelist[-1])
			
            dupeset = set(dupelist)
            dupelist = list(dupeset)
            namelist.extend(dupelist)	
        n = n+1

c = Counter(namelist)

scorefile = open("{}{}-{}.csv".format(recordsdir, txtboard, time.time()),"w")

for cc in c.most_common(100):
    scorefile.write("{},{},{}\n".format(cc[0], cc[1], time.time()))
