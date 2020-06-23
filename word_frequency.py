STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has',
    'he', 'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to',
    'were', 'will', 'with'
]


class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_contents(self):
        """
        This should read all the contents of the file
        and return them as one string.
        """
        file_list = [line.strip() for line in open(self.filename)]
        return file_list

class WordList:
    punctuation = ['.', '?', '!', '-']
    def __init__(self, text):
        self.text = text
        

    def extract_words(self):
        """
        This should get all words from the text. This method
        is responsible for lowercasing all words and stripping
        them of punctuation.
        """
        words_text = self.text.lower()
        words_text = words_text.split()

        words_nopunct = [word for word in words_text if word not in punctuation]
        return words_nopunct
        
        

    def remove_stop_words(self):
        """
        Removes all stop words from our word list. Expected to
        be run after extract_words.
        """
        poem_wordlist = [item for item in words_nopunct if item not in STOP_WORDS]
        return poem_wordlist
       

    def get_freqs(self):
        """
        Returns a data structure of word frequencies that
        FreqPrinter can handle. Expected to be run after
        extract_words and remove_stop_words. The data structure
        could be a dictionary or another type of object.
        """
        poem_words = {} # makes an empty dictionary
    
    
        for word in poem_wordlist: # loops over each word in the text
            if word in poem_words: # This checks to see if the word is in the dictionary
                poem_words[word] = poem_words[word] + 1 # If the word is in the dictionary increase the count by 1
            else: 
                poem_words[word] = 1 # if the word is not in the dictionary add it.
        


class FreqPrinter:
    def __init__(self, freqs):
        self.freqs = freqs

    def print_freqs(self):
        """
        Prints out a frequency chart of the top 10 items
        in our frequencies data structure.

        Example:
          her | 33   *********************************
        which | 12   ************
          all | 12   ************
         they | 7    *******
        their | 7    *******
          she | 7    *******
         them | 6    ******
         such | 6    ******
       rights | 6    ******
        right | 6    ******
        """
        for key in (poem_words.keys()): 
            print(key.rjust(20), "|", poem_words[key], '*' * poem_words[key] ) 
        


if __name__ == "__main__":
    import argparse
    import sys
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        reader = FileReader(file)
        word_list = WordList(reader.read_contents())
        word_list.extract_words()
        word_list.remove_stop_words()
        printer = FreqPrinter(word_list.get_freqs())
        printer.print_freqs()
    else:
        print(f"{file} does not exist!")
        sys.exit(1)
