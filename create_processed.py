import re

file = open("Collected_Works.txt", "r", errors="ignore")

new_file = open("Processed_Works.txt", "w")

for line in file:

    result = re.sub("[^a-zA-Z ]", "", line, flags=re.IGNORECASE)

    result += " " # add a space at the end of each line

    new_file.write(result)

file.close()

new_file.close()