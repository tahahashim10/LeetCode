# Placeholder for a deleted element
DELETED = "DELETED"


# Element in the HashTable
class Node(object):
    def __init__(self, city: str, dependencies: list[str]) -> None:
        self.city = city
        self.dependencies = dependencies
        self.started = False
        self.finished = False


class HashTable:
    def __init__(self, num_of_vertices: int) -> None:
        self.size = 0
        self.capacity = num_of_vertices
        self.array = [None] * self.capacity

    def hash(self, city: str, capacity=None) -> int:
        A = 0.45352364758429879433234
        if capacity is None:
            capacity = self.capacity
        return int((capacity * (hash(city) * A % 1)) // 1)

    def insert_with_dependency(self, city: str, dependent: str) -> None:
        index = self.search_index(city)

        if index is not None:
            self.array[index].dependencies.append(dependent)
            return

        special_nodes = [None, DELETED]
        index = self.hash(city)
        count = 0

        while not self.array[index] in special_nodes and count < self.capacity:
            index = (index + 1) % self.capacity
            count += 1

        if count == self.capacity:
            return

        self.array[index] = Node(city, [dependent])
        self.size += 1

    def insert_without_dependency(self, city: str) -> None:
        index = self.search_index(city)

        if index is not None:
            return

        special_nodes = [None, DELETED]
        index = self.hash(city)
        count = 0

        while not self.array[index] in special_nodes and count < self.capacity:
            index = (index + 1) % self.capacity
            count += 1

        if count == self.capacity:
            return

        self.array[index] = Node(city, [])
        self.size += 1

    def search(self, city: str) -> list[str]:
        search_index = self.search_index(city)
        if search_index is None:
            return None
        else:
            return self.array[search_index].dependencies

    def search_index(self, city: str) -> int:

        to_search = [None]
        index = self.hash(city)
        count = 0

        while self.array[index] not in to_search and count < self.capacity: 
            if self.array[index] != DELETED and self.array[index].city == city:
                return index
            index = (index + 1) % self.capacity
            count += 1
        return None


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:  # no dependencies will mean that we can visit any city
            return True

        graph = HashTable(numCourses)
        # Set up adjacency hash table
        for city_x, city_y in prerequisites: 
            graph.insert_with_dependency(city_x, city_y)  # each hash table key contains a list of all cities we must visit before it
            graph.insert_without_dependency(city_y)

        # make sure no vertex/city in the graph is unvisited
        for node in graph.array: 
            if node is not None and not node.started:
                if not self.dfs_visit(graph, node):
                    return False
        return True

    def dfs_visit(self, graph: HashTable, v: Node) -> bool:
    # algorithm from course notes page 77. Used to check for cycles 
        v.started = True 
        
        for key in v.dependencies:
            u = graph.array[graph.search_index(key)]
            if not u.started:
                if not self.dfs_visit(graph, u):
                    return False
            elif not u.finished:  # check for cycle and report
                return False
            
        v.finished = True
        return True
        