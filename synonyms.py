
'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math


#####################################################################
def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)

#####################################################################
def dot(vec1,vec2):
   '''Return dot product of two vectors stored as a dictionary, 
   as described in the handout for Project 3.'''
   sumxy = 0
   for key in vec1:
      if key in vec2:
         x = vec1[key]
         y = vec2[key]
         sumxy += x*y
   return sumxy

#######################################################################
def isEmpty(word):
    '''This function determine if a word is empty or not, return TRUE if is empty'''
    return word =="" or len(word.strip()) == 0

########################################################################

def build_setence_from_a_file(filename):
        # This function build a list of sentence from a given file
        _sentences = []
        empty_str = " "
        _dot = "."
        # access to the file: filenames[i], mode: read, encoding: latin1
        # The open() function returns a file object
        _file = open(filename, "r", encoding="latin1")
        # By default the read() method returns the whole text
        content = _file.read()
        content = content.lower()
        # only the tese punctuation is present in the texts: [",", "-", "--", ":", ";"]'''
        content = content.replace(",", empty_str)
        content = content.replace("-", empty_str)
        content = content.replace("--", empty_str)
        content = content.replace(":", empty_str)
        content = content.replace(";", empty_str)

        #".", "!", "?" is the only punctuation that separates sentences.
        content = content.replace("?", _dot)
        content =  content.replace("!", _dot)
        # The split() method splits a string into a list.
        lis = content.split(_dot)
        for i in range(len(lis)):
           _sentences.append(lis[i].split()) # default separator is any whitespace

        return  _sentences


#######################################################################

def build_test_word_choices_from_file(filename):
    '''build list of choice from a given file such as test.txt
       sample content of the file:

       draw paint walk paint
       duty task task example
       '''
    new_line = "\n"
    empty_string = ""

    _file = open(filename, "r", encoding="latin1")
    # By default the read() method returns the whole text
    content = _file.read()
    content = content.lower()
    #f = f.strip("\ufeff")
    list_content = content.split(new_line)
    list_choice = []
    for i in range(len(list_content)):
        if not isEmpty(list_content[i]):          
           list_choice.append(list_content[i].split())
    
    return list_choice


#######################################################################
#     
def cosine_similarity(vec1, vec2):
 
   '''This function returns the cosine similarity between the sparse 
      vectors vec1 and vec2, stored as dictionaries.'''
   sumxy = dot(vec1,vec2)
   normx = norm(vec1)
   normy = norm(vec2)
  
   cosine_sim = sumxy / (normx * normy)
   print("cosine_sim",cosine_sim)
   return cosine_sim


########################################################################
def build_semantic_descriptors(sentences):
    
    '''Return a semantic description dictionary from the
       given sentence list as described in the handout for Project 3'''
    
    semantic_desc_dictionary= {}
    
    for sentence in sentences:
        # this guarantee the sentence conatin distinct word 
        # only, since set do not allow duplicate values
        _set = set(sentence) 
        if len(_set) > 1:
           for word in _set: 
              if not isEmpty(word):
                 '''We store all words in all-lowercase, since we don’t consider, 
                    for example, “Man” and “man” to be different words.'''
                 _word = word.lower()
                 # if the key: _word not in semantic_desc_dictionary, create it
                 if _word not in semantic_desc_dictionary:
                    dictionary = {}
                    for thisword in _set:
                        if thisword != _word:
                           if thisword in dictionary:
                                dictionary[thisword] += 1
                           else:
                                dictionary[thisword] = 1
                        semantic_desc_dictionary[_word] = dictionary
                 # if the key: _word already in semantic_desc_dictionary, update the value in dictionary
                 else:
                    for thisword in _set:
                        if thisword != _word:
                           if thisword in semantic_desc_dictionary[_word]:
                              semantic_desc_dictionary[_word][thisword] += 1
                           else:
                              semantic_desc_dictionary[_word][thisword] = 1                 
     
    return semantic_desc_dictionary

########################################################################
def build_semantic_descriptors_from_files(filenames):
    

    '''This function takes a list of filenames of strings, which contains the names 
       of files (the first one can be opened using open(filenames[0], "r", encoding="latin1")), 
       and returns the a dictionary of the semantic descriptors of all the words in the files 
       filenames, with the files treated as a single text.'''
    sentences = []
    
    for i in range(len(filenames)):
        _sentences = build_setence_from_a_file(filenames[i])
        sentences += _sentences
    semantic_desc = build_semantic_descriptors(sentences)
    
    return semantic_desc

##########################################################################
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    '''This function takes in a string word, a list of strings choices, and a dictionary 
       semantic_descriptors and returns the element of choices which has the largest 
       semantic similarity to word'''
    
    empty_string = " "
    most_similar_w = empty_string
    max_cosine_similarity = -1
    # We store all words in all-lowercase
    _word = word.lower()

    if _word not in semantic_descriptors:
        return empty_string
    
    for i in range (len(choices)):
        # We store all words in all-lowercase
        choices[i] = choices[i].lower()
        cosine_similarity = 0
        if choices[i] not in semantic_descriptors: 
            '''If the semantic similarity between two words cannot be computed, 
               it is considered to be −1'''
            cosine_similarity = -1
        else:  
            '''compute the similarities of (w, s1), (w, s2), (w, s3), (w, s4) 
                and choose the word whose similarity to w is the highest'''         
            cosine_similarity = similarity_fn(semantic_descriptors[_word], semantic_descriptors[choices[i]])
        if cosine_similarity > max_cosine_similarity:
            max_cosine_similarity = cosine_similarity
            most_similar_w = choices[i]

    return most_similar_w

######################################################################
def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    '''This function takes in a string filename which is the name of a file in the same 
       format as test.txt, and returns the percentage (i.e., float between 0.0 and 100.0)'''
    guess_correct_answer = 0
    list_choice = build_test_word_choices_from_file(filename)
    '''
    file content format:

    draw paint walk paint
    duty task task example
    
    list_choice
    [
      ['draw', 'paint', 'walk', 'paint'], 
      ['duty', 'task', 'task', 'example']
    ]

    '''
    list_choice_length = len (list_choice)
    for i in range (list_choice_length):
        word = list_choice[i][0]
        choices = list_choice[i][2:]
        most_similar_w = most_similar_word(word, choices, semantic_descriptors, similarity_fn)
        if most_similar_w == list_choice[i][1]:
           
           guess_correct_answer +=1

    total_correct_percentage =  (guess_correct_answer / list_choice_length )*100 
        
    return total_correct_percentage

##########Test Functions below#########
def test_cosine_similarity():
    vec1 = {"a": 1, "b": 2, "c": 3}
    vec2 = {"b": 4, "c": 5, "d": 6}
    result = cosine_similarity(vec1, vec2)
    print("cosine_similarity(vec1, vec2)",result)

def test_build_semantic_descriptors():
    sentences = [["i", "am", "a", "sick", "man"],
                 ["i", "am", "a", "spiteful", "man"],
                 ["i", "am", "an", "unattractive", "man"],
                 ["i", "believe", "my", "liver", "is", "diseased"]
                ]
    semantic_descriptors =  build_semantic_descriptors(sentences)
    print("semantic_descriptors:", semantic_descriptors)

def test_build_semantic_descriptors_from_files():
    files =["welcome.txt"]
    semantic_desc = build_semantic_descriptors_from_files(files) 
    print ("semantic_desc:", semantic_desc)

def test_run_similarity_test():
    sem_descriptors = build_semantic_descriptors_from_files(["small_file.txt"])
    res = run_similarity_test("small_test.txt", sem_descriptors, cosine_similarity)
    print("percentage of the guesses were correct", res)


def test_build_test_word_choices_from_file():
    list_choice = build_test_word_choices_from_file("test0.txt")
    print(list_choice)

def test_isEmpty():
    word = " Hello"
    b = isEmpty(word)
    if not b:
        print ("is  Empty:", b)

    else:
        print ("is Empty:", b)

def testABC():
    list = [['draw', 'paint', 'walk', 'paint'], 
            ['duty', 'task', 'task', 'example'], 
            ['earnest', 'serious', 'serious', 'amusing'],
            ['picture', 'painting', 'painting', 'chair']
           ]
    list_choice_length = len (list)
    for i in range (list_choice_length):
        word = list [i][0]
        choices = list [i][2:]
        answer = list [i][1]
        print("set[0]", word) 
        print("set[1]", answer)      
        print("set[2:]", choices) 
        


#test_cosine_similarity()
#test_build_semantic_descriptors()
#test_build_semantic_descriptors_from_files()
#test_isEmpty()
#test_build_test_word_choices_from_file()
#testABC()
test_run_similarity_test()

