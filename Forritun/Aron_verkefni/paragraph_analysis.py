import operator
import string

def open_file():
    '''Prompts and opens a filname, returns false if not found'''
    filename = input('Enter filename: ')
    try:
        filestream = open(filename,'r')
        return filestream
    except FileNotFoundError:
        print('Filename {} not found!'.format(filename))
        return False

def file_to_list(filestream):
    '''Takes filestream and places lines in a file 
    into elements of a list'''
    if filestream:
        lines_in_file = []
        for line in filestream:
            line = line.strip()
            lines_in_file.append(line)

        lines_in_file.append('') #to indicate the end of the file
    return lines_in_file

def sort_list(lines_in_file):
    '''Takes lines of a file and returns the paragraphs in a file,
    a set and list with all words '''
    paragraphs_in_file = []
    words_in_paragraph = []
    all_words = []
    for line in lines_in_file:
        word_list = line.split()

        for word in word_list:
            word = word.strip(string.punctuation)
            word = word.lower()
            words_in_paragraph.append(word)
            all_words.append(word)
            all_words.sort()

        if line == '':
            paragraphs_in_file.append(words_in_paragraph)
            words_in_paragraph = []
            
    unique_words = sorted(set(all_words), reverse=False)

    return paragraphs_in_file, unique_words, all_words

def paragraph_index(paragraph_list, word_set):
    '''Assigns a paragraph index to every word in a set, 
    returns information in a dict'''
    first_paragraph = paragraph_list[0]
    paragraph_index = 1
    word_library = {}

    for paragraph in paragraph_list:   
        for word in word_set:
            # First round
            if paragraph == first_paragraph:
                word_library[word] = []
            if word in paragraph:
                word_library[word].append(paragraph_index)           
        paragraph_index += 1
    return word_library       

def count_words(word_list):
    '''Counts frequency of a word in a list and 
    returns 10 and 20 most frequent words'''
    
    word_counter = {}
    for word in word_list:
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    value_sorted = sorted(word_counter.items(),\
        key = operator.itemgetter(1), reverse = True)
    top_10 = [value_sorted[num] for num in range(0,10)] #creates a list of tuples
    top_20 = [value_sorted[num] for num in range(0,20)] #creates a list of tuples
    return top_10,top_20

def print_results(word_library,top_10,top_20):
    '''Prints information of three lists''' 
    WORD_INDEX = 0
    NUMBER_INDEX = 1
    
    print('The paragraph index:')
    for key,values in word_library.items():
        paragraph_indexes = ", ".join(str(num) for num in values)
        print('{} {}'.format(key,paragraph_indexes))
    print('\n''The highest 10 counts:')
    for element in top_10:
        print('{}: {}'.format(element[WORD_INDEX], element[NUMBER_INDEX]))
    print('\n''The highest 20 counts:')
    for element in top_20:
        print('{}: {}'.format(element[WORD_INDEX], element[NUMBER_INDEX]))

def main():
    '''The main code'''
    filestream = open_file()

    if filestream:
        lines_in_file = file_to_list(filestream)
        paragraphs_in_file, unique_words, all_words = sort_list(lines_in_file)
        word_library = paragraph_index(paragraphs_in_file,unique_words)
        top_10,top_20 = count_words(all_words)
        print_results(word_library, top_10, top_20)
        filestream.close

main()