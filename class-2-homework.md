#1. The columns in this data set map to:
	**order_id:** a unique identifier for an individual order. An order can have many items, therefore order_id is non-serial for this dataset.

	**quantity:** the count of a specific item in a specific order. For example, if a customer ordered two chicken burritos, the quantity would be "2" rather than adding an additional row for each burrito.

	**item_name:** Simply the descriptive name of the item.

	**choice_decription:** if the item_name has many variants, the choice_description reflects the specific selection. For example, A Nantucket Nectar can have many flavors, and therefore a value would be present in the choice_description field, however for "Chips" there are no choices, therefore the field is null.

	**item_price:** Equal to the price for each specific item, multiplied by quantity.

	The rows in the dataset represent each individual item belonging to a particular order. There is one-to-many relationship between items and orders, such that each individual order can contain many items.

#2. How many orders do there appear to be?

	`tail chipotle.csv`

	By looking at the tail for the dataset, we see the maximum order_id == 1834, which means there are 1834 unique orders in the dataset.

#3. How many lines are in the file?

	`wc -l chipotle.tsv`

	There are 4,623 lines in the file.

#4. Which burrito is more popular, steak or chicken?

	`grep -i "steak" chipotle.tsv | wc -l`
	`grep -i "chicken" chipotle.tsv | wc -l`

	There are 706 steak burritos compared to 1,565 chicken burritos.

#5. Do chicken burritos more often have black beans or pinto beans?
	`grep -i "chicken" chipotle.tsv | grep -i "pinto" chipotle.tsv | wc -l`
	`grep -i "chicken" chipotle.tsv | grep -i "black" chipotle.tsv | wc -l`

	582 chicken burritos have pinto beans versus 1,353 with black beans

#6. Make a list of all of the CSV or TSV files in the DAT7 repo (using a single command). Think about how wildcard characters can help you with this task.
	`find . -name *.*sv`

#7. Count the number of occurrences of the word 'dictionary' (regardless of case) across all files in the DAT7 repo.
	`grep -i "dictionary" ~/DAT7/* | wc -w`