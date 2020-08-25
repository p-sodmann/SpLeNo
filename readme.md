# SpLeNo
## building lemmatizer dictionaries in a human friendly way

Create Lemmatizer Dictionaries fast in a human readable way.
If you have a lot of domain specific vocabulary like in legal or biomedical text, it can be tricky to add a lot of new lemmas without losing oversight.

I wrote this small script to accomplish this goal. Instead of writing huge dictionaries with mapping all inflections to a lemma, this lets you define a lemma and add all inflections to it.

### Example:


Lemma Snek  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Flex Sneks  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Spel Snake  

### Installation:
clone this repository and install it locally:

```console
git clone https://github.com/theudas/SpLeNo
cd SpLeNo
pip install .
```

then simply use it on your spacy nlp object:

```python
import spacy
import spleno

nlp = spacy.load("de_core_news_sm")
nlp = spleno.load(nlp, "dictionaries/example.dic")
```

have fun.