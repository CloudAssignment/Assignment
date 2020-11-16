
import time
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

timestamp0 = time.time()

for i in range(100):
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

    print("Iteration"+str(i)+"\n"+"There are "+str(counter)+" occurences of the word \"Jesus\" in the bible"+"\n"+
          "there are "+str(counter2)+" words in this text file"+"\n"
          "this computation took: "+str(timestamp2-timestamp1))
    infile.close()


timestamp3 = time.time()
time = timestamp3 - timestamp0
print("100 iterations of this program took: " + str(time)+" seconds")

plat = input("please input platform you are using: ")

outfile = open("results.txt","a")
outfile.write(plat.lower()+" "+str(time)+"\n")
outfile.close()

times = {
    "ubuntu" :0,
    "windows":0,
    "virtualbox":0,
    "docker":0
    }

infile1 = open("results.txt","r")


for line in infile1:
    words = line.split(" ")

    if words[0] == "ubuntu":
        time1 = words[1]
        times["ubuntu"] = (float(time1))
    if words[0] == "windows":
        time1 = words[1]
        times["windows"] = (float(time1))
    if words[0] == "virtualbox":
        time1 = words[1]
        times["virtualbox"] = (float(time1))
    if words[0] == "docker":
        time1 = words[1]
        times["docker"] = (float(time1))

y_pos = np.arange(len(times))
plt.bar(y_pos,times.values(),align='center',alpha=0.5)
plt.xticks(y_pos, times.keys())
plt.ylabel('Computation Time(second)')
plt.title("Platforms")

plt.show()
infile1.close()