import basc_py4chan
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from nltk.tokenize import SpaceTokenizer
from nltk import pos_tag, ne_chunk

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

m_wordlist = ['']
m_neslist = ['']
n = 0

for thread_id in thread_ids:
    if board.thread_exists(thread_id) and n < 2:
        thread = board.get_thread(thread_id)
        print("Thread:", thread.url)
        postlist = thread.all_posts
        for post in postlist: # post is a paragraph

            toks = tokenizer.tokenize(post.text_comment)
            try:
                pos = pos_tag(toks)
            except:
                print("Error")
                pass

            chunked_nes = ne_chunk(pos)
            m_neslist.append(chunked_nes)
        n += 1

poslist = ['']

for sublist in m_neslist:
    for item in sublist:
        poslist.append(item)

for p in poslist:
    if p.node == 'PERSON':
        print(p, "Person")
