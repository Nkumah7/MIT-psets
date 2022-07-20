import string
# def permutations(word):
#     if len(word) == 1:
#         return [word]
    
#     # get all permutations of length N-1
#     perms = permutations(word[1:])
#     char = word[0]
#     result = [] # a list of all permutations of word
#     for perm in perms:
#         for i in range(len(perm) + 1):
#             result.append(perm[:i] + char + perm[i:])
#     return result
# print(permutations('abc'))
def shift_dict(shift):
    mp = {}
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    
    for letter in uppercase_letters:
        letter_index = uppercase_letters.find(letter)
        shifted_letter_index = letter_index + shift
        
        if shifted_letter_index >= len(uppercase_letters):
            shifted_letter_index -= len(uppercase_letters)
        elif shifted_letter_index < 0:
            shifted_letter_index += len(uppercase_letters)
        
        mp[letter] = uppercase_letters[shifted_letter_index]
    
    for letter in lowercase_letters:
        letter_index = lowercase_letters.find(letter)
        shifted_letter_index = letter_index + shift            
            
        if shifted_letter_index >= len(lowercase_letters):
            shifted_letter_index -= len(lowercase_letters)
        elif shifted_letter_index < 0:
            shifted_letter_index += len(lowercase_letters)
            
        mp[letter] = lowercase_letters[shifted_letter_index]
            
         
        
        
    print(mp)
    # print(letter, shifted_letter)
    # print(int(len(letters)/2))
        
    
    
shift_dict(2)

