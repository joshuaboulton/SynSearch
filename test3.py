# Import the nltk library and download the wordnet corpus
import nltk
nltk.download('wordnet')

dic = []

# Open the text file in read mode
file = open("Processed_Works.txt", "r", errors="ignore")

animal = nltk.corpus.wordnet.synset("animal.n.01")

# Loop through each line in the file
for line in file:
  # Split the line into words
  words = line.split()
  # Loop through each word in the line
  for word in words:
    # Get the wordnet synsets for the word
    synsets = nltk.corpus.wordnet.synsets(word)
    # Loop through each synset
    for synset in synsets:
      # Get the lexical name of the synset
      """lexname = synset.lexname()
      # Check if the lexical name is "noun.animal"
      if lexname == "noun.animal":"""
        # If word is new, print the word and add to dictionary
      if animal in synset.closure(lambda s: s.hypernyms()):
        if word not in dic:
          dic.append(word)
          #print(word)

# Close the file
file.close()

for i in dic:
  print(i)
