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
import matplotlib.pyplot as plt

#################################
# CHANGE SOME OF THESE VARIABLES!
board = 'g'
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

m_wordlist = []
m_neslist = []
n = 0
nnp_list= []
name = ""
namelist = []

for thread_id in thread_ids:
    if board.thread_exists(thread_id) and n < threadcount:
        thread = board.get_thread(thread_id)
        #print("Thread:", thread.url)
        postlist = thread.all_posts
        for post in postlist: # post is a paragraph

            for par in nltk.sent_tokenize(post.text_comment):
                tokens = nltk.tokenize.word_tokenize(par)
                tags = nltk.pos_tag(tokens)
                chunked_tag = ne_chunk(tags)
                for c in chunked_tag:
                    name = ""
                    if type(c).__name__ == 'tuple':
                        if c[1] == "PERSON":
                            nnp_list.append(c[0])
                    elif type(c).__name__ == 'Tree':
                        if c.label() == "PERSON":
                            nnp_list.append(c)
                            for x in range(0, len(c)):
                                #print("%s" % c[x][0], end=' ')
                                name += c[x][0] + " "
                            namelist.append(name.strip())
                            print(namelist[-1])
        n = n+1

c = Counter(namelist)

scorefile = open("records/{}-{}.csv".format(txtboard, time.time()),"w")

for cc in c.most_common(200):
    scorefile.write("{},{}\n".format(cc[0],cc[1]))
cordered = OrderedDict(c.most_common(30))
labels, values = zip(*cordered.items())

indexes = np.arange(len(labels))
width = 1

# For the graph. Currently disabled.
plt.title(title)
plt.ylabel(ylabel)
plt.bar(indexes, values, width, color=["#d6daf0", "#d0d0f0"])
plt.xticks(indexes, labels, rotation=90)

#plt.savefig('{}.png'.format(int(time.time())))
#plt.show()
