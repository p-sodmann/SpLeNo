"""
    This Module can load nicely and human readable formated dictionaries.

    Lemma Katze
        Flex Katzen
        Spel Gadse

    Lemma Word <-- this is the word, that will be used as the lemma later
        Flex Words <-- inflection for the Lemma Word
        Spel Wort <-- spelling variant / correction

    It can be used with Tags if your language supports them
    Lemma Noun Word
        Flex Words
        Spel Wort
"""


class Spleno():
    def __init__(self):
        pass

    def load(self, nlp, path):
        last_lemma = None
        last_type = None
        
        lemma_table = nlp.vocab.lookups.get_table("lemma_lookup")

        # load data from dictionary
        with open(path, "r", encoding="utf-8") as file:
            l = file.readlines()

        l = [l.strip() for l in l]
        

        # go lne by line over the file we just loaded
        for line_index, line in enumerate(l):
            # check if empty:
            if line:

                # ignore comments
                if line[0] == "#":
                    continue
                
                # split by spaces, what could go wrong ;D
                elements = line.split(" ")

                # check if we actually have content:
                if elements:

                    # this is our new base word
                    if line.startswith("Lemma"):
                        last_lemma = elements[-1]

                        if len(elements) == 2:
                            last_type = None
                        elif len(elements) == 3:
                            last_type = elements[1]
                        else:
                            raise Exception('Error in Parsing Lemma File', f'There is an issue in reading file {path} line: {line_index} is malformed.')
                
                    
                    else:
                        # you forgot to set a lemma first
                        if last_lemma is None:                    
                            print(f"There is an Error in file {path}, you tried to add a new f{elements[0]} but didn't set a base word before. \n\nLine: {line_index}")
                        
                        # we found a new entry for the base word, lets append this to our lookup table 
                        else:
                            # in case of Lemma Words
                            if last_type is None:
                                flexion = elements[-1]
                                lemma_table[flexion] = last_lemma   
                            
                            # This list needs to be populated
                            elif last_type in ["Noun"]:
                                flexion = elements[-1]
                                lemma_table[last_type.lower()][flexion] = last_lemma   

        return nlp
    