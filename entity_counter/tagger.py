# This is a program that runs BookNLP's supersense tagger

from booknlp.booknlp import BookNLP

model_params={
		"pipeline":"entity,supersense", 
		"model":"small"
	}
	
booknlp=BookNLP("en", model_params)

# Input file to process
input_file="pg4300.txt"

# Output directory to store resulting files in
output_directory="output"

# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id="joyce2003"

booknlp.process(input_file, output_directory, book_id)

