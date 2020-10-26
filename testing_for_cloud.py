import time
import datetime
'''
Program that will run y x n x n iterations (basically very inefficient) 
In total there will be 18 points that you can plot on the graph
Appends the Points in a File called VanillaWindows.txt 
Looks like :

Execution Time | Iteration
0               3s 
etc....
@Author: Sebastian Racki
'''

def run(t,n,file):
    text = open(file,"w")
    text.write("Execution Time | Iteration" + '\n')
    text.write("--------------------------" + '\n')
    iteration = 0
    start = time.time()
    for y in range(t):
        for amount in range(n):
            for x in range(n):
                amount * x
        iteration +=1
        this = (time.time() - start).__round__(5)
        text.write(str(this) + '\t' + str(iteration) + '\n')
    text.close()




run(100,2000,"VanillaWindows.txt")
'''
Function run will take three paramaters(t = how many points we would like,n = how many iterations,file)
hours is going to be how many hours the program should run for 
x is going to be the file that we are going to write the points to
#we want the output of the file to look like this v

Execution Time | Iteration
___________________________
20                   1
30                   2

'''


'''
Function 2 is going to be the graph
So we will have two files one from the Virtual Machine with all the points
and one from the normal machine without the Virtual one and we are going to read the
points and put them on a graph and get the line of best fit and see how they compare based on that
'''
def graph(file1,file2):
    pass

'''
Function 3 will evalute the results and return a conclusion for us
So it will return which one is more efficient and it will be based on these points
1. How much memory the system used
2. How much time it took for each execution
3. How much of the CPU was in use
4. How many threads we used in the process
@return this will all be logged inside another txt file and returned in a nice format
'''
