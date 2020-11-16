from math import inf
import time

result = 0
import matplotlib.pyplot as plt
File_object = open("graphdata.txt", "w")

t0 = time.time()
class MinHeapArrayBased:
    def __init__(self, array=list()):
        self.array = array
        self.nodes = self.populate_nodes()
        self.l = len(self.array)  # length
        self.initial_heapify(self.l // 2)

    def populate_nodes(self):
        temp = {}
        for i, arr in enumerate(self.array):
            # print(arr)
            temp[arr] = i
        return temp

    def initial_heapify(self, l):
        for i in range(l, -1, -1):
            self.heapify(i)

    def heapify(self, parent):
        left_child = 2 * parent + 1
        if left_child >= self.l:  # check for left child, already heapify
            return
        elif left_child + 1 >= self.l or self.array[left_child] < self.array[left_child + 1]:  # check for right child
            child_index = left_child
        else:
            child_index = left_child + 1

        if self.array[child_index] < self.array[parent]:
            self.swap(parent, child_index)
            self.heapify(child_index)  # as array is modified, so again heapify

    def swap(self, a, b):
        self.array[a], self.array[b] = self.array[b], self.array[a]
        self.nodes[self.array[b]], self.nodes[self.array[a]] = self.nodes[self.array[a]], self.nodes[self.array[b]]

    def dec_node(self, child_index, x):
        temp = self.nodes[child_index]
        self.nodes.pop(self.array[temp])
        self.nodes[x], self.array[temp] = temp, x
        self.update(temp)

    def update(self, child_index):
        temp = (child_index - 1) // 2
        while child_index > 0 and self.array[child_index] < self.array[temp]:
            self.swap(temp, child_index)
            child_index -= 1 // 2
            temp = (child_index - 1) // 2

    def remove(self):
        temp = self.array[0]
        self.swap(self.l - 1, 0)
        self.nodes.pop(self.array[-1])
        self.array.pop()  # now remove minimum from the array
        self.l -= 1  # update the length
        self.heapify(0)  # as array is modified, so again heapify
        return temp


class Dijkstra:
    def __init__(self):
        self.graph = self.read_graph()
        self.nodes = []
        self.distances = {}  # smallest distance from a given node
        self.predecessor = {}  # predecessor of each node on smallest route to that node

    def read_graph(self):
        g = {}
        filename = 'graph2.txt'
        try:
            with open(filename, 'r') as graph_data:
                data = graph_data.read().splitlines()  # read all lines and remove ending '\n'

            for i in range(len(data)):
                # create node
                if 'id' in data[i]:
                    id = int(data[i].split()[1])
                    g[id] = []

                # create edge
                elif 'from' in data[i]:
                    start = int(data[i].split()[1])
                    i += 1
                    end = int(data[i].split()[1])
                    i += 1
                    length = int(data[i].split()[1])
                    i += 1
                    g[start].append((end, length))
                    if 'false' == data[i].split()[1]:  # if connection is 2-way
                        g[end].append((start, length))
            return g

        except Exception as ex:
            print('Exception Occurred.\n' + str(ex))

    def main(self):
        start = 1
        self.run(start)
        self.print_stats()
        try:

            pass

        except Exception as ex:
            print('Exception Occured.\n' + str(ex))

    def run(self, start):
        self.initialize_distances(start)
        self.predecessor[start] = None
        priority_queue = MinHeapArrayBased(self.nodes)

        # while queue is not empty
        while priority_queue.array:
            min_node = priority_queue.remove()[1]  # node with minimum distance
            for neighbour in self.graph[min_node]:  # iterate all out going edges and update the distance accordingly
                dist = self.distances[min_node] + neighbour[1]
                neighbour = neighbour[0]  # get neighbour id

                # if less distance edge is found
                # then update all stats of a node i.e smallest route, predecessor etc
                if self.distances[neighbour] > dist:
                    previous_distance = self.distances[neighbour]
                    self.distances[neighbour] = dist
                    priority_queue.dec_node((previous_distance, neighbour), (self.distances[neighbour], neighbour))
                    self.predecessor[neighbour] = min_node

    def initialize_distances(self, start):
        for vertex in self.graph:
            if vertex is not start:
                self.nodes.append((inf, vertex))
                self.distances[vertex] = inf
            else:
                self.nodes.append((0, vertex))
                self.distances[vertex] = 0

    def print_stats(self):
        """
        Prints the cost and predecessor form the given start node
        """
        #print('\n=======\nSummary\n=======\n\nVertex\tCost\tPreceding Vertex')
        #for vertex, distance in self.distances.items():
        #    print("{}\t{}\t{}".format(vertex, distance, self.predecessor[vertex]))
File_object.truncate()
for i in range(1,1001):
    d = Dijkstra()
    d.main()

    t1 = time.time()
    total = t1-t0
    result += total
    total = str(round(total, 4))
    File_object.write(str(total)+" "+str(i)+"\n")
    print(total)

result = result/1000
print("Average of 1000 runs: " + str(result))
time.sleep(2)
