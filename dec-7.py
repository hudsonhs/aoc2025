from utils import getTodayInputFile
from collections import deque

USE_TEST_INPUT = False

def main():
    graph = getSerializedInput()
    start = (1, graph[0].index('S'))
    graph[start[0]][start[1]] = 1
    return bfsMarkPaths(graph, start)

def getSerializedInput() -> list:
    with getTodayInputFile(USE_TEST_INPUT) as file:
        return [[int(x) if x.isnumeric() else x for x in list(line.strip().replace('.', '0'))] for line in file.readlines()]

def bfs(graph: list, start: tuple) -> int:
    numSplits = 0
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if not node in visited:
            visited.add(node)
            # check we aren't at the bottom
            if node[0] < len(graph) - 1:
                # check if node below is a splitter
                belowIndex = (node[0] + 1, node[1])
                belowValue = graph[belowIndex[0]][belowIndex[1]]
                if belowValue == '^':
                    numSplits += 1
                    belowLeft = (belowIndex[0], belowIndex[1] - 1)
                    belowRight = (belowIndex[0], belowIndex[1] + 1)
                    queue.append(belowLeft)
                    queue.append(belowRight)
                else:
                    queue.append(belowIndex)
    return numSplits

def bfsMarkPaths(graph: list, start: tuple) -> int:
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # check we aren't at the bottom
            if node[0] < len(graph) - 1:
                nodeValue = graph[node[0]][node[1]]
                belowIndex = (node[0] + 1, node[1])
                belowValue = graph[belowIndex[0]][belowIndex[1]]
                if belowValue == '^':
                    belowLeft = (belowIndex[0], belowIndex[1] - 1)
                    belowRight = (belowIndex[0], belowIndex[1] + 1)
                    graph[belowLeft[0]][belowLeft[1]] += nodeValue
                    graph[belowRight[0]][belowRight[1]] += nodeValue
                    queue.append(belowLeft)
                    queue.append(belowRight)
                else:
                    graph[belowIndex[0]][belowIndex[1]] += nodeValue
                    queue.append(belowIndex)
    return sum(graph[-1])

print(main())
