import basc_py4chan
import nltk
from nltk.corpus import stopwords
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('stopwords')


board = basc_py4chan.Board('lit')

thread_ids = board.get_all_thread_ids()

m_wordlist = ['']
n = 0

for thread_id in thread_ids:
    if board.thread_exists(thread_id) and n < 5:
        thread = board.get_thread(thread_id)
        print("Thread:", thread.url)
        postlist = thread.all_posts
        for post in postlist:
            for w in nltk.word_tokenize(post.text_comment):
                m_wordlist.append(w)
        n += 1

stop_words = set(stopwords.words('english'))
filtered = [w for w in m_wordlist if not w in stop_words]
print(filtered)

fdist = nltk.FreqDist(filtered)
print(fdist.most_common(50))
