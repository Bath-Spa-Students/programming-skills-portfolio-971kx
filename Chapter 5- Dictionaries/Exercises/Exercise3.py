# Glossary dictionary with programming words and their meanings

glossary = {
    'Algorithm': 'A set of step-by-step instructions to solve a problem or perform a task.',
    'Variable': 'A symbolic name associated with a value and whose associated value may be changed.',
    'Boolean': 'A data type that can have one of two values, often denoted as true or false.',
    'Array': 'A data structure that stores a collection of elements, each identified by an index.',
    'Recursion': 'A programming technique where a function calls itself to solve a problem.',
     'debugging' : 'the process of detecting and removing of existing and potential errors in a software code that can cause it to behave unexpectedly or crash.',
     'loop' : 'It means repeating something over and over until a particular condition is satisfied.',
     'list' : 'It is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.',
     'syntax': 'The set of rules that defines the combinations of symbols that are considered to be correctly structured programs in a specific programming language.',
     'tuple' : 'An immutable, ordered collection of elements, usually of different data types, enclosed within parentheses.'
     
}

# Printing each word and its meaning using a loop
for word, meaning in glossary.items():
    print(word + ': ' + meaning + '\n')
