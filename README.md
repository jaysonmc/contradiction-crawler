# ContradictionDetection

Contradiction Detection System made using NLTK, spaCy and WordNet in python for Natural Language Processing Project

University project aimed to detect contradicting statements in text with possible application like detecting the integrity of a politician by analyzing his speeches.

Can detect contradicting statements based on the use of verbs which are the antonyms of each other and also for the mismatch in numeric values in the statements.

## To Run

To crawl the site (the raw output is stored in the output folder) type ...

```
python main.py crawl
```

To process the crawled content (which will be stored in the processed folder)

```
python main.py process
```

To analyze the crawled content (will output contradictions to console)

```
python main.py analyze
```

# Local Config

Run

```
pip3 install -r requirements.txt
python3 -m spacy download en
mkdir nltk_data
python3 -m nltk.downloader
    -> install 'all'
```
