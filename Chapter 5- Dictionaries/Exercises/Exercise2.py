#Creating a Dictionary/Glossary with the programming words along with their meaning

glossary = {
     'Algorithm': 'A set of step-by-step instructions to solve a problem or perform a task.',
    'Variable': 'A symbolic name associated with a value and whose associated value may be changed.',
    'Boolean': 'A data type that can have one of two values, often denoted as true or false.',
    'Array': 'A data structure that stores a collection of elements, each identified by an index.',
    'Recursion': 'A programming technique where a function calls itself to solve a problem.',
}

#Printing the words & their meanings from the dictionary/glossary above
for word, meaning in glossary.items():
    print(word + ':')
    print(meaning +  '\n')
