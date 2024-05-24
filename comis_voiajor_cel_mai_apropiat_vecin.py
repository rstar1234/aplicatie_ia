class NComisVoiajor:
    def __init__(self, mat_cost) -> None:
        self.mat_cost = mat_cost
        self.n = len(mat_cost)
        self.visited = [False for x in range(self.n)]
        self.path = []
        self.min_cost = 0
    def comis_voiajor_cal_mai_apropiat_vecin(self):
        """Returneaza drumul cel mai scurt si costul sau"""
        current_node = 0
        self.path.append(current_node)
        self.visited[current_node] = True
        
        #pentru fiecare nod, vizitam toate nodurile vecine pana toate nodurile sunt vizitate
        #daca distanta de la acest nod este mai mica decat cea mai mica distanta o salvam
        for _ in range(self.n - 1):
            nearest_distance = float('inf')
            for node in range(self.n):
                if not self.visited[node] and self.mat_cost[current_node][node] < nearest_distance:
                    nearest_distance = self.mat_cost[current_node][node]
                    nearest_node = node
            self.path.append(nearest_node)
            self.min_cost += nearest_distance
            self.visited[nearest_node] = True
            current_node = nearest_node
        #return to the starting node
        self.min_cost += self.mat_cost[current_node][self.path[0]]
        self.path.append(self.path[0])
        
        return self.min_cost, self.path
    
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
        return NComisVoiajor(new_graph)
    
#testing
# graph = [
#     [0, 2, 9, 10],
#     [1, 0, 6, 4],
#     [15, 7, 0, 8],
#     [6, 3, 12, 0]
# ]
# ncv = NComisVoiajor(graph)
# route, total_distance = ncv.comis_voiajor_cal_mai_apropiat_vecin()
# print(route)
# print(total_distance)