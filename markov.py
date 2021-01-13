"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text_string = open(file_path).read()
    # print(contents)
    return text_string
open_and_read_file('green-eggs.txt')

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()
    chains = {}
    # loop through words, assign i:i+1 to dictionary keys in chains
    
    #     if len(words) is 3, stop at index 2
    # [with a fox]
    # for each index in the range 0 to one less than the length of list words
    for i in range(len(words)-1):
        # set variable "bigram" = a tuple with word[index], word[index +1]
        bigram = (words[i], words[i + 1])
        # if tuple "bigram" is not in dicto 
        if bigram not in chains:
            #add key:value pair bigram:[] to dictionary "chains"
            #if we don't use this if statement, bigrams that occur
            # more than 1x will update value previously added to dict "chains" 
            # with empty list
            chains[bigram] = []
        # {(with, a): []}
        # if index is less than len(words -2), then append the LIST 
        # chains[bigram] (chains[bigram]= the value of the key bigram in dictionary "chains")
        if i < (len(words)-2):
            chains[bigram].append(words[i + 2])

    # your code goes here
    # print(chains.keys())
    return chains
open_and_read_file('green-eggs.txt')    
make_chains('text_string')

def make_text(chains):
    """Return text from chains."""
    
    words = [choice(chains())]
    print(words)
    #for items in chains:
        #print(choice(chains[bigram]))
        #words.append(random.choice())

    # return ' '.join(words)

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)