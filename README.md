This somewhat works.

This is bad code.

I'm trying to identify the trends of authors based on /lit/ posts.

Goals:
- Collect data every hour of the proper nouns used in /lit/. This would include words like "The Bible" or "Nietzsche". 
- Take this data and store it somewhere stable, like postgresql or something like that.
- Visualize the data on a webpage

Issues:
- Misspelled/uncapatalized names
- Normalization: what if someone posts a paragraph of 100 instances of the phrase "John Green"? Should we group "Stallman" and "Richard Stallman" under one key?

# Installing
1. Install some packages via your favorite package manager: `sudo apt install python3 python3-pip python3-tk`
2. Install some packages via pip3: `pip3 install basc_py4chan nltk numpy`
	- As I update the code, I may forget to document which packages need to be installed.
3. Clone this repo: `git clone https://github.com/jackklika/4chan-trending`
4. Read the code! There's some constants such as the board you would want to scrape that you may want to set.
5. Run the code: `python3 main.py`
	- This will install a bunch of nltk data
