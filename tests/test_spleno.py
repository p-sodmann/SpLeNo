from spleno.spleno import Spleno
import numpy as np
import spacy

def test_mri():
    spleno = Spleno()
    nlp = spacy.load("de_core_news_sm")

    nlp = spleno.load(nlp, "tests/test_data/dictionary.dic")

    doc = nlp("Gadse")
    
    assert doc[0].lemma_ == "Katze"