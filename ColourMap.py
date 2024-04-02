import os


class ColourMap:
    """This class implements a CSP algorithm that colours a given map using the minimum number of colours possible.
    The algorithm works with maps that contain from 2 to 20 separate regions that should be coloured.
    There are maximum 7 colours that can be used. If it is not possible to cover the map, it will print
    a respective message
    @author: Dmitrii Kosintsev
    @date:   28 February 2024
    """

    """Initialising the object with an empty dictionary and a list of available colours"""

    def __init__(self):
        self.map = {}
        self.coloured_map = {}
        self.map_list = []
        self.colours = ["Red", "Green", "Blue", "Yellow", "Violet", "Gray", "Orange"]

    """"The method read the file and creates a graph using a dictionary"""

    def read_map_from_file(self, filename):
        f = open(filename, "r")
        num_vertices = int(f.readline())  # The number of vertices is in the first line
        # print("Number of vertices: ", num_vertices)  # For debugging purposes

        # Return if there are more than 20 vertices in the graph
        if num_vertices > 20 or num_vertices < 2:
            print("Please provide a map that has between 2 and 20 regions")
            return

        # Adding items to the graph
        for x in f:
            x = x.split()  # Splitting the line into a list of items

            # Adding the first value on the list as the vertex
            self.addVertex(x[0])
            # print("Adding vertex", x[0]) # For debugging purposes

            # Adding the rest of the values on the list as edges
            for i in range(1, len(x)):
                self.map[x[0]].append(x[i])
                # print("Adding edge", x[i])  # For debugging purposes

        # Creating a list for easier iteration
        self.map_list = list(self.map)

    """"The method adds a new vertex to a dictionary"""

    def addVertex(self, vertex):
        if vertex not in self.map:
            self.map[vertex] = []

    """The method implements backtracking to assign colours to each vertex"""

    def backtracking(self, n):

        # When all vertices are coloured, return coloured_map
        if n == len(self.map_list):
            return self.coloured_map

        # Start from n-th vertex
        cur_vertex = self.map_list[n]

        # Iterate through colours
        for cur_colour in self.colours:

            # Check if it is possible to assign the current colour to the chosen vertex
            if self.check(cur_vertex, cur_colour):
                self.coloured_map[cur_vertex] = cur_colour

                # Try to assign the same colour to the next vertex
                result = self.backtracking(n + 1)
                if result is not None:
                    return result

                # Backtrack when the colour cannot be applied
                self.coloured_map[cur_vertex] = None

        # If it is not possible to use 7 colours, return None and inform the user
        print("Not possible with 7 colors")
        return None

    """The method checks whether any neighbour has the same colour"""

    def check(self, cur_vertex, cur_colour):

        # Check every neighbour of the chosen vertex
        for neighbour in self.map[cur_vertex]:

            # If any neighbour has the current colour, return False
            if self.coloured_map.get(neighbour) == cur_colour:
                return False

        # If the if-statement was skipped, it is safe to assign the current colour
        return True

    """The printing method to format the output"""

    def print_colours(self, dictionary):
        print("Output:")
        for key, value in dictionary.items():
            print(key, value)


# Creating the object and running the algorithm
filename = "graph.txt"  # Change the path if needed
colouring = ColourMap()
colouring.read_map_from_file(filename)

# Uncomment to print the graph
# print(colouring.map)

colouring.backtracking(0)
colouring.print_colours(colouring.coloured_map)
