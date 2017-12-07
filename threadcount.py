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
    if board.thread_exists(thread_id) and n < 4:
        thread = board.get_thread(thread_id)
        print("Thread:", thread.url)
        postlist = thread.all_posts
        for post in postlist: # post is a paragraph

            for par in nltk.sent_tokenize(post.text_comment):
                tokens = nltk.tokenize.word_tokenize(par)
                tags = nltk.pos_tag(tokens)
                chunked_tag = ne_chunk(tags)
                print(chunked_tag)
        n+= 1
