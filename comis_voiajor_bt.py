import sys

class ComisVoiajor:
    def __init__(self, mat_cost) -> None:
        self.n = len(mat_cost)
        self.visited = [False for x in range(self.n)]
        self.solution = []
        self.min_path_cost = sys.maxsize
        self.path = []
        self.mat_cost = mat_cost
    
    #find the minimum weight cycle
    def comis_voiajor(self, position, count, cost, path):
        if (count == self.n and self.mat_cost[position][0]):
            self.min_path_cost = min(self.min_path_cost, cost + self.mat_cost[position][0])
            self.path = path + [0]
            return
        #backtracking step
        #traverseaza matricea de adiacenta incepand de la position
        for i in range(self.n):
            if (self.visited[i] == False and self.mat_cost[position][i]):
                #vizitat
                self.visited[i] = True
                self.comis_voiajor(i, count + 1, cost + self.mat_cost[position][i], path + [i])
                
                #marcheaza ca nevizitat
                self.visited[i] = False
                
    def find_min_cost_path(self):
        #start from the first node
        """Returneaza cea mai scurta cale si costul ei"""
        self.visited[0] = True
        self.comis_voiajor(0, 1, 0, [0])
        return self.min_path_cost, self.path
    
    @staticmethod
    def read_graph_from_file(nume_fis):
        f = open(nume_fis, 'r')
        lines = f.readlines()
        f.close()
        new_graph = [[0 for x in range(int(lines[0].strip()))] for y in range(int(lines[0].strip()))]
        lines.pop(0)
        for i in range(len(lines)):
            temp = lines[i].strip().split()
            new_graph[i] = [int(x) for x in temp]
        return ComisVoiajor(new_graph)
                
#testing
# graph = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

# cv = ComisVoiajor.read_graph_from_file('graf.txt')
# min_cost, path = cv.find_min_cost_path()

# print(f"Min cost: {min_cost}")
# print(f"Path: {path}")
