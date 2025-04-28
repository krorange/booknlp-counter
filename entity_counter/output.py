# This is a program that outputs the number of animal/plant/human subjects (nsubj)

#paragraph_ID	sentence_ID	token_ID_within_sentence	token_ID_within_document	word	lemma	byte_onset	byte_offset	POS_tag	fine_POS_tag	dependency_relation	syntactic_head_ID	event	supersense_category
#1	0	2	2	Illustration	illustration	4	16	NOUN	NN	nmod	4	O	noun.communication
def entity_counter():
	first = True
	current_sentence_id = 0
	current_sentence = []

	# Set file path for the concatenated file
	fd = open('../output/joyce2003.complete')
	line = fd.readline()

	# Default number of supersense tags
	num_ani = 0
	num_pla = 0
	num_hum = 0

	while line:
		if first:
			first = False
			line = fd.readline()
		row = line.strip().split('\t')

		sentence_id = int(row[1])
		if sentence_id != current_sentence_id:
			for sentence_row in current_sentence:
				lemma = sentence_row[13].lower()
				dep = sentence_row[10]
				if lemma in ['noun.animal'] and dep in ['nsubj']:
					print(current_sentence_id, ':::',' '.join([i[4] for i in current_sentence]))
					num_ani += 1
					break
				if lemma in ['noun.plant'] and dep in ['nsubj']:
					#print(current_sentence_id,';;;',' '.join([i[4] for i in current_sentence]))
					num_pla += 1
					break
				if lemma in ['noun.person'] and dep in ['nsubj']:
					#print(current_sentence_id,'!!!',' '.join([i[4] for i in current_sentence]))
					num_hum += 1
					break
			current_sentence_id = int(row[1])
			current_sentence = []
		current_sentence.append(row)		
		line = fd.readline()
	
	#print("Animal counts:", num_ani)
	#print("Plant counts:", num_pla)
	#print("Human counts:", num_hum)

if __name__ == "__main__":
	entity_counter()