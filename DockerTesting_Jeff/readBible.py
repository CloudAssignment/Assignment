import time
infile = open("bible.txt",'r')

counter = 0
counter2 = 0
timestamp1 = time.time()

for line in infile:
    for word in line.split():
        counter2 +=1
        if word.lower() == "god":
            counter +=1

timestamp2 = time.time()

print("There are "+str(counter)+" occurences of the word \"Jesus\" in the bible"+"\n"+
      "there are "+str(counter2)+" words in this text file"+"\n"
      "this computation took: "+str(timestamp2-timestamp1))


