import sys
from random import choice
from string import punctuation


class SimpleMarkovGenerator(object):
    filename = sys.argv[1]
    corpus = open(filename).read()


    def make_chains(self):
        """Given a list of files, make chains from them."""
        """Takes input text as string; stores chains."""
        #Make a dictionary and split a text file into a list of words
        chains = {}
        words = self.corpus.split()

        #MAKE THE DICTIONARY
        ##ake a key/value pair, check if it's in the dictionary, and if not, add it.
        ##If it's in there, append the value to the value list stored at the key.
        for i in range(len(words) - 2):
            key = (words[i], words[i + 1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

        ##MAKE THE MARKOV CHAIN
        #Pick a random key from the dictionary
        key = choice(chains.keys())
        #Make sure it starts with an upper case letter before proceeding.
        while key[0][0].isupper() == False:
            key = choice(chains.keys())

        #Split the key into two words
        words = [key[0], key[1]]

        #Choose a random value associated with the key
        while key in chains:
            word = choice(chains[key])
            #If the value word's last character isn't punctuation, pick a new value 
            if word[-1] not in punctuation:
                word = choice(chains[key])

            words.append(word)
            key = (key[1], word)

        print " ".join(words)







# class Tweet(SimpleMarkovGenerator, StartOnUppercaseMixin, EndsOnPunctuationMixin):

    # while characters < 140




if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    pass