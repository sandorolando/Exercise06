# import argv

from sys import argv

script, filename = argv

f = open(filename)
text = f.read()

def string_splitter(text):
    remove_dashes = text.replace('--', ' ')
    word_list = remove_dashes.split()

    # print word_list

    clean_words = []
    for item in word_list:
        lowercase = item.lower()
        clean_words.append(lowercase.strip('!.?_()*[]#,:;-\\/\'\"'))
    
    return clean_words

def wordcount(clean_words):
    occurrence_dict = {}
    for item in clean_words:
        if item in occurrence_dict:
            occurrence_dict[item] += 1
        else:
            occurrence_dict.setdefault(item)
            occurrence_dict[item] = 1
    return occurrence_dict
    
def print_wordcount(occurrence_dict):
    for key, value in occurrence_dict.iteritems():
        print "%s %r" % (key, value)

# def sort_by_frequency(occurrence_dict):
#    sorted_values = occurrence_dict.values()
#    print sorted(sorted_values)

# def alphabetize():

def main():

    # sort_by_frequency(wordcount(string_splitter(text)))
    print_wordcount(wordcount(string_splitter(text)))

main()