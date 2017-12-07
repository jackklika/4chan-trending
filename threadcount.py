import basc_py4chan
import nltk
import inspect
from collections import Counter
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import SpaceTokenizer
from nltk import pos_tag, ne_chunk
import numpy as np
import matplotlib.pyplot as plt


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
board = basc_py4chan.Board('lit')

thread_ids = board.get_all_thread_ids()

m_wordlist = []
m_neslist = []
n = 0
nnp_list= []
name = ""
namelist = []

for thread_id in thread_ids:
    if board.thread_exists(thread_id) and n < 2:
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

c = sorted(Counter(namelist).items())
labels, values = zip(*c)

indexes = np.arange(len(labels))
width = 1

plt.bar(indexes, values, width)
plt.xticks(indexes + width, labels)
plt.show()

