import csv

# in general, "handles" to something (like in real life) get you a hold of that something, in programmatic sense

def print_table():
	table_rows = [] # declare an empty list, we'll rows to it as we read
	with open('table.csv') as csv_file: # open the file, call the handle 'csv_file'
		reader = csv.reader(csv_file) # get a handle to the table content inside the csv file, call it 'reader'
		header = next(reader) # get the column headers of the table
		table_rows.append(header) # add the header to our list
		for row in reader: # read a row, one at a time (iterating over Rows)
			table_rows.append(row) # add to our list

			dummy_string = '' # now making this empty string, will use it to print this entire row

			for item in row: # now read an item in row, one at a time (iterating over Columns)
				dummy_string += str(item) # appending the item to our string, item might be a number/list/etc. but str() will make it a string! 
				dummy_string += '\t' # adding a tab after printing each item to make the table look neat
			dummy_string += '\n' # finished printing entire row, for-loop complete, notice the indent is one-less, add newline!

			print(dummy_string) # our line is ready for printing!

			# Next, for-loop moves on to the next row in the table.

		# We just printed the table while reading it

		print('\n\n\n') # seperating the next table by a few more newlines, each \n will add one

		# We will now print it from memory, since we stored the rows of the table while reading it in our list called 'table_rows'. Notice we also print the header this time!

		for row in table_rows: # read a row from our list this time, one at a time (iterating over Rows)

			dummy_string = '' # now making this empty string, will use it to print this entire row

			for item in row: # now read an item in row, one at a time (iterating over Columns)
				dummy_string += str(item) # concatenate/add the item to our string, item might be a number/list/etc. but str() will make it a string! 
				dummy_string += '\t' # adding a tab after printing each item to make the table look neat
			dummy_string += '\n' # finished printing entire row, for-loop complete, notice the indent is one-less, now add a newline!
			
			print(dummy_string) # our line is ready for printing!

			# Next, for-loop moves on to the next row in the table.

print_table()