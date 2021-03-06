import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        letter_map = {}
        letters = VOWELS_UPPER + CONSONANTS_UPPER + VOWELS_LOWER + CONSONANTS_LOWER
        for letter in letters:
            if letter in vowels_permutation.upper():
                letter_map[letter] = vowels_permutation[VOWELS_UPPER.find(letter)].upper()
            elif letter in vowels_permutation:
                letter_map[letter] = vowels_permutation[VOWELS_LOWER.find(letter)]
            
        return letter_map
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        encrypted_msg = ''  
        for letter in self.message_text:
            if letter in transpose_dict:
                encrypted_msg += transpose_dict[letter]
            else:
                encrypted_msg += letter
        return encrypted_msg
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        valid_words = []        
        decrypted_message = []
        sentences = {}
        perms = get_permutations(VOWELS_LOWER) # Get each permutation of vowels
        
        for i, perm in enumerate(perms): # Loop through each vowel permutaion)
            transpose_dict = self.build_transpose_dict(perm) # Get transpose dict for each vowel permutaion
            transposed_msg = self.apply_transpose(transpose_dict) # Get possible decrypted message
            decrypted_message.append(transposed_msg.split()) # Split the possible decrypted message into a list and store each in a list 
            for word in transposed_msg.split(): # Loop through each possible decrypted message
                if is_word(self.valid_words, word): # Check for valid words in each possible decrypted message
                    valid_words.append(word) # Store each valid word 
            sentences[len(valid_words)] = i # Store group of valid words for each vowel permutation in a dictionary (for faster access)
            valid_words = [] # Restore valid words list back to empty list to store valid words for next vowel permutation
        
        # Return the original string if no good permutations are found 
        if sum(sentences.keys()) < 1:
            return self.message_text
        
        # Use the 'keys' method to get the index of the sentence with the highest number of valid words
        decrypted_msg_index = sentences[max(sentences.keys())]         
            
        # Join the words in the list and return
        return " ".join(decrypted_message[decrypted_msg_index])      
        
                  
if __name__ == '__main__':

    # Example test case
    msg1 = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = msg1.build_transpose_dict(permutation)
    print("Original message:", msg1.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", msg1.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(msg1.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    msg2 = SubMessage("The Third")
    permutation = "oaeui"
    enc_dict = msg2.build_transpose_dict(permutation)
    print("\nOriginal message:", msg2.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Tha Therd")
    print("Actual encryption:", msg2.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(msg2.apply_transpose(enc_dict))
    print("Decrypted message:", "Lupin", enc_message.decrypt_message())
    
    msg3 = SubMessage("One of the greatest!")
    permutation = "iuaeo"
    enc_dict = msg3.build_transpose_dict(permutation)
    print("\nOriginal message:", msg3.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Enu ef thu gruitust!")
    print("Actual encryption:", msg3.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(msg3.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
    
    
     
    
