input_file = open('input.txt', encoding='utf-8')
content_input = input_file.read()
print(content_input)

# Counting Lines
def number_lines(): 
    with open('input.txt', encoding='utf-8') as input_file:
        count_lines = 0
        for line in input_file: 
            count_lines += 1
    return count_lines

# Counting Words (splitting the lines into words first)
def number_words(): 
    with open('input.txt', encoding='utf-8') as input_file:
        count_words = 0
        for line in input_file: 
            words = line.split()
            count_words += len(words)
    return count_words

# Counting Characters (splitting the lines into characters first)
def number_characters(): 
    with open('input.txt', encoding='utf-8') as input_file:
        count_characters= 0
        for line in input_file: 
            count_characters += len(line)  
    return count_characters
            
# Getting the counts 
count_lines = number_lines()
count_words = number_words()
count_characters = number_characters()


# Write the results to output.txt
with open('output.txt', mode='w', encoding='utf-8') as output_file:
    output_file.write(f"Number of lines in input: {count_lines}.\n")
    output_file.write(f"Number of words in input: {count_words}.\n")
    output_file.write(f"Number of characters in input: {count_characters}.\n")

# Read and print the content of output.txt
with open('output.txt', encoding='utf-8') as output_file:
    content_output = output_file.read()
    print(content_output)

