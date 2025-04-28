# booknlp-counter

This is a module that processes BookNLP output based on the supersense tags.
The BookNLP output is formatted in a tab separated file:
#paragraph_ID	sentence_ID	token_ID_within_sentence	token_ID_within_document	word	lemma	byte_onset	byte_offset	POS_tag	fine_POS_tag	dependency_relation	syntactic_head_ID	event	supersense_category
#1	0	2	2	Illustration	illustration	4	16	NOUN	NN	nmod	4	O	noun.communication

There are different types of supersense categories: e.g., "animal", "artifact", "body", "cognition", etc.

This module is a python library that provides a way of searching for sentences in text annotated by [BookNLP](https://github.com/booknlp/booknlp). BookNLP is a set of tools for 
running natural language processing (NLP) on literary texts that annotates them according to linguistic features such as lemma, part-of-speech,
syntactic function (e.g. subject, object) and semantic categorisation (e.g. animal, cognition, body). The module allows you to search for any combination of the above features and outputs and counts the matched sentences.

## Worked example
<!-- give an example sentence, a short one, where you can see the value of the annotation: e.g. with animal subject --> 

# Usage instructions

1. run `tagger.py`. The original script can be found at https://github.com/booknlp/booknlp/blob/main/examples/run_booknlp.py
2. run `concatenate.py > output/joyce2003.complete`
3. run `output.py`


# Acknowledgements


