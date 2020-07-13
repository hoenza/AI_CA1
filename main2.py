from sys import stdin
from math import sqrt



tableD = []
for line in stdin:
    if line == "":
        break
    if line[-1] == '\n':
        tableD.append(list(line[:-1]))
    else:
        tableD.append(list(line))


class Table():
    def __init__(self, table):
        self.table = table
        self.amb = (-1, -1)
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == 'A':
                    self.amb = (i, j)
        
        self.table[self.amb[0]][self.amb[1]] = ' '
    
    @classmethod
    def find(char):
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == chr:
                    return (i, j)
    
    def print(self):
        print('>>>>>>>>>>>')
        for line in self.table:
            print(line)
        print('amb ', self.amb)
    
    def check_host(self, loc):
        return ord('0') < ord(self.table[loc[0]][loc[1]]) < ord('4')

    def BFS(self, chr):
        cur = self.amb
        frontier = []
        visited = [[False for i in self.table[0]] for j in self.table]
        frontier.append(cur)
        steps = 0
        while(len(frontier)):
            cur = frontier.pop(0)

            if self.table[cur[0]-1][cur[1]] == chr or (chr == 'H' and self.check_host([cur[0]-1, cur[1]])):
                visited[cur[0]-1][cur[1]] = cur
                return cur, [cur[0]-1, cur[1]], steps
            elif self.table[cur[0]-1][cur[1]] != '#'  and visited[cur[0]-1][cur[1]] == False:
                visited[cur[0]-1][cur[1]] = cur
                frontier.append([cur[0]-1, cur[1]])
            
            if self.table[cur[0]+1][cur[1]] == chr or (chr == 'H' and self.check_host([cur[0]+1, cur[1]])):
                visited[cur[0]+1][cur[1]] = cur
                return cur, [cur[0]+1, cur[1]], steps
            elif self.table[cur[0]+1][cur[1]] != '#' and visited[cur[0]+1][cur[1]] == False:
                visited[cur[0]+1][cur[1]] = cur
                frontier.append([cur[0]+1, cur[1]])
            
            if self.table[cur[0]][cur[1]-1] == chr or (chr == 'H' and self.check_host([cur[0], cur[1]-1])):
                visited[cur[0]][cur[1]-1] = cur
                return cur, [cur[0], cur[1]-1], steps
            elif self.table[cur[0]][cur[1]-1] != '#' and visited[cur[0]][cur[1]-1] == False:
                visited[cur[0]][cur[1]-1] = cur
                frontier.append([cur[0], cur[1]-1])
            
            if self.table[cur[0]][cur[1]+1] == chr or (chr == 'H' and self.check_host([cur[0], cur[1]-1])):
                visited[cur[0]][cur[1]-1] = cur
                return cur, [cur[0], cur[1]+1], steps
            elif self.table[cur[0]][cur[1]+1] != '#' and visited[cur[0]][cur[1]+1] == False:
                visited[cur[0]][cur[1]+1] = cur
                frontier.append([cur[0], cur[1]+1])

            steps = steps + 1
        return [-1, -1], [-1, -1], -1

    def dec_host(self, loc):
        self.table[loc[0]][loc[1]] = chr(ord(self.table[loc[0]][loc[1]]) -1)

    def runBFS(self):
        stepsAns = []
        while(True):
            newAmb, target, steps = self.BFS('P')
            stepsAns.append(steps)
            self.table[target[0]][target[1]] = ' '
            self.amb = newAmb
            self.print()
            if steps == -1:
                break

            newAmb, target, steps = self.BFS('H')
            stepsAns.append(steps)
            self.dec_host(target)
            self.amb = newAmb
            self.print()
            if steps == -1:
                break
        
        print(stepsAns)

    def IDS(self, chr, max):
        cur = self.amb
        for depth in range(0, max):
            visited = [[False for i in self.table[0]] for j in self.table]
            newAmb, target, steps = self.DFS(visited, cur, chr, depth)
            if steps > -1:
                return newAmb, target, depth
        
        return [-1, -1], [-1, -1], -1
    
    def DFS(self, visited, cur, chr, max):
        if max < 0:
            return [-1, -1], [-1, -1], -1
        
        if self.table[cur[0]-1][cur[1]] == chr or (chr == 'H' and self.check_host([cur[0]-1, cur[1]])):
            return cur, [cur[0]-1, cur[1]], 0
        
        if self.table[cur[0]+1][cur[1]] == chr or (chr == 'H' and self.check_host([cur[0]+1, cur[1]])):
            return cur, [cur[0]+1, cur[1]], 0
        
        if self.table[cur[0]][cur[1]-1] == chr or (chr == 'H' and self.check_host([cur[0], cur[1]-1])):
            return cur, [cur[0], cur[1]-1], 0
        
        if self.table[cur[0]][cur[1]+1] == chr or (chr == 'H' and self.check_host([cur[0], cur[1]+1])):
            return cur, [cur[0], cur[1]+1], 0

        if self.table[cur[0]-1][cur[1]] != '#' and visited[cur[0]-1][cur[1]] == False :
            visited[cur[0]-1][cur[1]] = True
            newAmb, target, steps = self.DFS(visited, [cur[0]-1, cur[1]], chr, max-1)
            if steps != -1:
                return newAmb, target, steps+1
        
        if self.table[cur[0]+1][cur[1]] != '#' and visited[cur[0]+1][cur[1]] == False:
            visited[cur[0]+1][cur[1]] = True
            newAmb, target, steps = self.DFS(visited, [cur[0]+1, cur[1]], chr, max-1)
            if steps != -1:
                return newAmb, target, steps+1

        if self.table[cur[0]][cur[1]-1] != '#' and visited[cur[0]][cur[1]-1] == False:
            visited[cur[0]][cur[1]-1] = True
            newAmb, target, steps = self.DFS(visited, [cur[0], cur[1]-1], chr, max-1)
            if steps != -1:
                return newAmb, target, steps+1
            
        if self.table[cur[0]][cur[1]+1] != '#' and visited[cur[0]][cur[1]+1] == False:
            visited[cur[0]][cur[1]+1] = True
            newAmb, target, steps = self.DFS(visited, [cur[0], cur[1]+1], chr, max-1)
            if steps != -1:
                return newAmb, target, steps+1
        
        return [-1, -1], [-1, -1], -1
    
    def runIDS(self, max):
        stepsAns = []
        while(True):
            newAmb, target, steps = self.IDS('P', max)
            stepsAns.append(steps)
            self.table[target[0]][target[1]] = ' '
            self.amb = newAmb
            self.print()
            if steps == -1:
                break

            newAmb, target, steps = self.IDS('H', max)
            stepsAns.append(steps)
            self.dec_host(target)
            self.amb = newAmb
            self.print()
            if steps == -1:
                break

        print(stepsAns)

    def find_near(self, loc, chr):
        for depth in range(1, max(len(self.table), len(self.table[0]))):
            for i in range(-depth, depth+1):
                for j in range(-depth, depth+1):
                    if not (0 <= loc[0]+i < len(self.table) and 0 <= loc[1]+j < len(self.table[0])):
                        continue
                    if self.table[loc[0]+i][loc[1]+j] == chr or (chr == 'H' and self.check_host([loc[0]+i, loc[1]+j])):
                        if 0 < sqrt(i**2 + j**2) <= depth:
                            return [loc[0]+i, loc[1]+j]
        
        return [-1, -1]

    def get_min(self, frontier, heur_tbl, cost_tbl):
        minInd = -1
        minVal = 1000000

        for i in range(len(frontier)):
            if heur_tbl[frontier[i][0]][frontier[i][1]] + cost_tbl[frontier[i][0]][frontier[i][1]] < minVal:
                minVal = heur_tbl[frontier[i][0]][frontier[i][1]] + cost_tbl[frontier[i][0]][frontier[i][1]]
                minInd = i
        
        return minInd

    def A1(self, heur_tbl, dist):
        cur = self.amb
        cost_tbl = [[-1 for i in self.table[0]] for i in self.table]
        visited = [[False for i in self.table[0]] for i in self.table]
        parent = [[[-1, -1] for i in self.table[0]] for i in self.table]
        
        frontier = []
        frontier.append(cur)
        cost_tbl[cur[0]][cur[1]] = 0


        while(len(frontier)):
            minInd = self.get_min(frontier, heur_tbl, cost_tbl)
            minFrontier = frontier.pop(minInd)
            if minFrontier == dist:
                return parent[dist[0]][dist[1]], dist, cost_tbl[dist[0]][dist[1]]
            visited[minFrontier[0]][minFrontier[1]] = True

            i = minFrontier[0]
            j = minFrontier[1]

            if self.table[i-1][j] != '#' and visited[i-1][j] == False:
                searchInd = self.search(frontier, [i-1, j])
                if searchInd == -1:
                    frontier.append([i-1, j])
                    parent[i-1][j] = [i, j]
                    cost_tbl[i-1][j] = cost_tbl[i][j] + 1
                elif cost_tbl[i-1][j] > cost_tbl[i][j] + 1:
                    parent[i-1][j] = [i, j]
                    cost_tbl[i-1][j] = cost_tbl[i][j] + 1

            if self.table[i+1][j] != '#' and visited[i+1][j] == False:
                searchInd = self.search(frontier, [i+1, j])
                if searchInd == -1:
                    frontier.append([i+1, j])
                    parent[i+1][j] = [i, j]
                    cost_tbl[i+1][j] = cost_tbl[i][j] + 1
                elif cost_tbl[i+1][j] > cost_tbl[i][j] + 1:
                    parent[i+1][j] = [i, j]
                    cost_tbl[i+1][j] = cost_tbl[i][j] + 1

            if self.table[i][j-1] != '#' and visited[i][j-1] == False:
                searchInd = self.search(frontier, [i, j-1])
                if searchInd == -1:
                    frontier.append([i, j-1])
                    parent[i][j-1] = [i, j]
                    cost_tbl[i][j-1] = cost_tbl[i][j] + 1
                elif cost_tbl[i][j-1] > cost_tbl[i][j] + 1:
                    parent[i][j-1] = [i, j]
                    cost_tbl[i][j-1] = cost_tbl[i][j] + 1
                
            if self.table[i][j+1] != '#' and visited[i][j+1] == False:
                searchInd = self.search(frontier, [i, j+1])
                if searchInd == -1:
                    frontier.append([i, j+1])
                    parent[i][j+1] = [i, j]
                    cost_tbl[i][j+1] = cost_tbl[i][j] + 1
                elif cost_tbl[i][j+1] > cost_tbl[i][j] + 1:
                    parent[i][j+1] = [i, j]
                    cost_tbl[i][j+1] = cost_tbl[i][j] + 1
            
    def runA1(self):
        stepsAns = []
        while(True):
            dist = self.find_near(self.amb, 'P')
            if dist == [-1, -1]:
                break
            heur_tbl = self.heur1(dist)

            newAmb, target, steps = self.A1(heur_tbl, dist)
            stepsAns.append(steps)
            self.table[target[0]][target[1]] = ' '
            self.amb = newAmb
            self.print()
            if steps == -1:
                break
            

            dist = self.find_near(self.amb, 'H')
            if dist == [-1, -1]:
                break
            heur_tbl = self.heur1(dist)

            newAmb, target, steps = self.A1(heur_tbl, dist)
            stepsAns.append(steps)
            self.dec_host(target)
            self.amb = newAmb
            self.print()
            if steps == -1:
                break
    
    def search(self, frontier, element):
        for i in range(len(frontier)):
            if frontier[i] == element:
                return i
        return -1

    def heur2(self, chr):
        heur_tbl = [[-1 for i in self.table[0]] for i in self.table]

        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                near = self.find_near([i, j], chr)
                if near == -1:
                    return -1
                heur_tbl[i][j] = sqrt((near[0] - i)**2 + (near[1]- j)**2)
        return heur_tbl

    def A2(self,heur_tbl, chr):
        cur = self.amb

        cost_tbl = [[-1 for i in self.table[0]] for i in self.table]
        visited = [[False for i in self.table[0]] for i in self.table]
        parent = [[[-1, -1] for i in self.table[0]] for i in self.table]
        
        frontier = []
        frontier.append(cur)
        cost_tbl[cur[0]][cur[1]] = 0

        while(len(frontier)):
            minInd = self.get_min(frontier, heur_tbl, cost_tbl)
            minFrontier = frontier.pop(minInd)
            if self.table[minFrontier[0]][minFrontier[1]] == chr or (chr == "H" and self.check_host(minFrontier)):
                return parent[minFrontier[0]][minFrontier[1]], minFrontier, cost_tbl[minFrontier[0]][minFrontier[1]]
            visited[minFrontier[0]][minFrontier[1]] = True

            i = minFrontier[0]
            j = minFrontier[1]

            if self.table[i-1][j] != '#' and visited[i-1][j] == False:
                searchInd = self.search(frontier, [i-1, j])
                if searchInd == -1:
                    frontier.append([i-1, j])
                    parent[i-1][j] = [i, j]
                    cost_tbl[i-1][j] = cost_tbl[i][j] + 1
                elif cost_tbl[i-1][j] > cost_tbl[i][j] + 1:
                    parent[i-1][j] = [i, j]
                    cost_tbl[i-1][j] = cost_tbl[i][j] + 1

            if self.table[i+1][j] != '#' and visited[i+1][j] == False:
                searchInd = self.search(frontier, [i+1, j])
                if searchInd == -1:
                    frontier.append([i+1, j])
                    parent[i+1][j] = [i, j]
                    cost_tbl[i+1][j] = cost_tbl[i][j] + 1
                elif cost_tbl[i+1][j] > cost_tbl[i][j] + 1:
                    parent[i+1][j] = [i, j]
                    cost_tbl[i+1][j] = cost_tbl[i][j] + 1

            if self.table[i][j-1] != '#' and visited[i][j-1] == False:
                searchInd = self.search(frontier, [i, j-1])
                if searchInd == -1:
                    frontier.append([i, j-1])
                    parent[i][j-1] = [i, j]
                    cost_tbl[i][j-1] = cost_tbl[i][j] + 1
                elif cost_tbl[i][j-1] > cost_tbl[i][j] + 1:
                    parent[i][j-1] = [i, j]
                    cost_tbl[i][j-1] = cost_tbl[i][j] + 1
                
            if self.table[i][j+1] != '#' and visited[i][j+1] == False:
                searchInd = self.search(frontier, [i, j+1])
                if searchInd == -1:
                    frontier.append([i, j+1])
                    parent[i][j+1] = [i, j]
                    cost_tbl[i][j+1] = cost_tbl[i][j] + 1
                elif cost_tbl[i][j+1] > cost_tbl[i][j] + 1:
                    parent[i][j+1] = [i, j]
                    cost_tbl[i][j+1] = cost_tbl[i][j] + 1

        return [-1, -1], [-1, -1], -1

    def runA2(self):
        stepsAns = []
        while(True):
            heur_tbl = self.heur2('P')
            if heur_tbl == -1:
                break
            newAmb, target, steps = self.A2(heur_tbl, 'P')
            print('p', newAmb, target, steps)
            stepsAns.append(steps)
            self.table[target[0]][target[1]] = ' '
            self.amb = newAmb
            self.print()
            if steps == -1:
                break

            heur_tbl = self.heur2('H')
            if heur_tbl == -1:
                break
            newAmb, target, steps = self.A2(heur_tbl, 'H')
            print('h', newAmb, target, steps)
            stepsAns.append(steps)
            self.dec_host(target)
            self.amb = newAmb
            self.print()
            if steps == -1:
                break

    def heur1(self, dist):
        heur_tbl = [[-1 for i in self.table[0]] for i in self.table]

        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                heur_tbl[i][j] = sqrt((dist[0]-i)**2 + (dist[1]-j)**2)
        return heur_tbl


table = Table(tableD)
table.print()
# table.runBFS()
# table.runA1()
table.runA2()
# print("IDS>>>>>>>>>>>>")
# table = Table(tableD)
# table.print()
# table.runIDS(10)

    




        