import string
import operator

def get_word_list(filename):
    total_words = []
    try:
        the_file = open(filename, 'r')
        for line in the_file:	
            line = line.strip() 
            word_list = line.split()
            for word in word_list:
                word = word.lower()
                word = word.strip(string.punctuation)
                total_words.append(word)
    
        the_file.close
    except FileNotFoundError:
        pass
    return total_words

def get_bigrams(word_list):

    bigrams = {}
    previous_word = ''
    for word in word_list:
        if previous_word != '':
            bigram = (previous_word, word)
            if bigram in bigrams:
                bigrams[bigram] += 1
            else:
                bigrams[bigram] = 1
        previous_word = word
    return bigrams

filename = input("Enter name of file: ")
all_words = get_word_list(filename)
if all_words:
    bigrams = get_bigrams(all_words)
    sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1,0), reverse=True)
    bigrams_top_10 = [ sorted_bigrams[i] for i in range(0,10)]
    print(bigrams_top_10)