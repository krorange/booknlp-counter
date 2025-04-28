# booknlp-counter

This module is a python library that provides a way of searching for sentences in text annotated by [BookNLP](https://github.com/booknlp/booknlp). BookNLP is a set of tools for running natural language processing (NLP) on literary texts that annotates them according to linguistic features such as lemma, part-of-speech, syntactic function (e.g. subject, object) and semantic categorisation (e.g. animal, cognition, body). The module allows you to search for any combination of the above features and outputs and counts the matched sentences.

## Worked example
<!-- give an example sentence, a short one, where you can see the value of the annotation: e.g. with animal subject --> 
- Input:
```
paragraph_ID	sentence_ID	token_ID_within_sentence	token_ID_within_document	word	lemma	byte_onset	byte_offset	POS_tag	fine_POS_tag	dependency_relation	syntactic_head_ID	event	supersense_category  
695	1938	0	22043	The	the	99219	99222	DET	DT	det	22044	O	_  
695	1938	1	22044	cat	cat	99223	99226	NOUN	NN	nsubj	22045	O	noun.animal  
695	1938	2	22045	walked	walk	99227	99233	VERB	VBD	ROOT	22045	O	verb.motion  
695	1938	3	22046	stiffly	stiffly	99234	99241	ADV	RB	advmod	22047	O	_  
695	1938	4	22047	round	round	99242	99247	VERB	VB	prep	22045	O	_  
695	1938	5	22048	a	a	99248	99249	DET	DT	det	22049	O	_  
695	1938	6	22049	leg	leg	99250	99253	NOUN	NN	dobj	22047	O	noun.body  
695	1938	7	22050	of	of	99254	99256	ADP	IN	prep	22049	O	_  
695	1938	8	22051	the	the	99257	99260	DET	DT	det	22052	O	_  
695	1938	9	22052	table	table	99261	99266	NOUN	NN	pobj	22050	O	noun.artifact  
695	1938	10	22053	with	with	99267	99271	ADP	IN	prep	22047	O	_  
695	1938	11	22054	tail	tail	99272	99276	NOUN	NN	pobj	22053	O	noun.animal  
695	1938	12	22055	on	on	99277	99279	ADP	IN	prep	22054	O	_  
695	1938	13	22056	high	high	99280	99284	ADJ	JJ	pobj	22055	O	_  
695	1938	14	22057	.	.	99284	99285	PUNCT	.	punct	22045	O	_  

696	1939	0	22058	—	—	99287	99288	PUNCT	:	punct	22059	O	_  
696	1939	1	22059	Mkgnao	Mkgnao	99288	99294	PROPN	NNP	nsubj	22070	O	_  
696	1939	2	22060	!	!	99294	99295	PUNCT	.	punct	22059	O	_  
697	1939	3	22061	—	—	99297	99298	PUNCT	:	punct	22070	O	_  
697	1939	4	22062	O	o	99298	99299	INTJ	UH	meta	22061	O	_  
697	1939	5	22063	,	,	99299	99300	PUNCT	,	punct	22066	O	_  
697	1939	6	22064	there	there	99301	99306	ADV	RB	advmod	22066	O	_
697	1939	7	22065	you	you	99307	99310	PRON	PRP	nsubj	22066	O	_
697	1939	8	22066	are	be	99311	99314	AUX	VBP	ccomp	22070	O	verb.stative
697	1939	9	22067	,	,	99314	99315	PUNCT	,	punct	22070	O	_
697	1939	10	22068	Mr	Mr	99316	99318	PROPN	NNP	compound	22069	O	noun.person
697	1939	11	22069	Bloom	Bloom	99319	99324	PROPN	NNP	nsubj	22070	O	noun.person
697	1939	12	22070	said	say	99325	99329	VERB	VBD	ROOT	22070	O	verb.communication
697	1939	13	22071	,	,	99329	99330	PUNCT	,	punct	22070	O	_
697	1939	14	22072	turning	turn	99331	99338	VERB	VBG	advcl	22070	O	verb.motion
697	1939	15	22073	from	from	99339	99343	ADP	IN	prep	22072	O	_
697	1939	16	22074	the	the	99344	99347	DET	DT	det	22075	O	_
697	1939	17	22075	fire	fire	99348	99352	NOUN	NN	pobj	22073	O	_
697	1939	18	22076	.	.	99352	99353	PUNCT	.	punct	22070	O	_
```
- Output:
```
1938 ::: The cat walked stiffly round a leg of the table with tail on high .  
1939 !!! — Mkgnao ! — O , there you are , Mr Bloom said , turning from the fire .
```

# Usage instructions

1. Run `tagger.py`. This runs only some elements (entity and supersense) of the pipeline. The original script can be found at https://github.com/booknlp/booknlp/blob/main/examples/run_booknlp.py
2. Run `concatenate.py > output/joyce2003.complete`. This concatenates the some files (.tokens and .supersense) from the BookNLP output. You can replace the output directory.
3. Run `output.py`. This outputs

# Acknowledgements


