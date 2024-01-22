def transform_letter(letter):
    # Define multiple replacements
    replacements = {'ě': 'e', 'š': 's', 'č': 'c', 'ř': 'r', 'ž': 'z', 'ý': 'y', 'á': 'a', 'í': 'i', 'é': 'e', 'ú': 'u', 'ů': 'u', 'ť': 't', 'ď': 'd', 'ň': 'n'}
    
    # Apply replacements if the letter is in the dictionary
    return replacements.get(letter.lower(), letter)

def transform_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            transformed_line = ''.join(transform_letter(letter) for letter in line)
            outfile.write(transformed_line)

# Example usage: Transform letters in 'input.txt' and save the result in 'output.txt'
transform_file(r"C:\Users\uživatel pc\Downloads\The Whale.srt", r"C:\Users\uživatel pc\Downloads\titulky.srt")