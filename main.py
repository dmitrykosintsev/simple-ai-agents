import numpy as np


class VacuumCleaner:
  """This class implements a vacuum-cleaner that visits given locations and removes dust

    CS4408 - Artificial Intelligence - Programming Assignment 2
    @author: Dmitrii Kosintsev
    @date:   14 February 2024
    
    Since there is no discreet list of actions that should require energy,
    I used energy for the following actions:
    - Move to a new location (once per function call)
    - Clean a location (once per function call)
    - Mark the location as visited (once per function call)
    """
  """Create a VacuumCleaner object with the following instances:
    - map: 2D array that represents the map of the place
    - dirt: 2D array that shows whether each location is clean or dirty
    - visited: 2D array to keep track of the visited locations
    - curLocX: current row in 2D array
    - curLocY: current column in 2D array
    - currentEnergy: keeps track of the remaining energy
    - bagCapacity: keeps track of the free space in the bag
    - currentDirection: keeps track of the directions (right, left, down, up)
    """

  def __init__(self, map, dirt, visited, curLocX, curLocY, currentEnergy,
               bagCapacity, currentDirection):
    self.map = map
    self.dirt = dirt
    self.visited = visited
    self.curLocX = curLocX
    self.curLocY = curLocY
    self.currentEnergy = currentEnergy
    self.bagCapacity = bagCapacity
    self.currentDirection = currentDirection

  """Defines a list of methods to call for each move"""

  def move(self):

    # Continue moving as long as there are unvisited locations
    while not np.all(self.visited == 1):
      if self.dirt[self.curLocX, self.curLocY] == 1:
        self.clean_current_location()
        if self.bagCapacity <= 0:
          print("Warning! The bag is full. Going home.")
          self.go_home()
          return
      else:
        print(self.map[self.curLocX, self.curLocY], "is clean")
      self.mark_current_location_visited()
      self.move_to_next_location()

    # Return when the goal is achieved
    return

  """This method cleans the current location and marks it as cleaned.
    It also checks the capacity of the bag and returns to A if it is full"""

  def clean_current_location(self):
    print(self.map[self.curLocX, self.curLocY], "is dirty. Cleaning.")
    self.dirt[self.curLocX, self.curLocY] = 0
    self.bagCapacity -= 1
    print(
        self.map[self.curLocX, self.curLocY],
        "is now clean. Moving on. Current bag capacity "
        "is {}".format(self.bagCapacity))

    # Cleaning costs 1 energy
    self.currentEnergy -= 1

  """Marks the current location as visited"""

  def mark_current_location_visited(self):

    # Marking location as visited costs 1 energy
    self.currentEnergy -= 1
    if self.visited[self.curLocX, self.curLocY] == 0:
      self.visited[self.curLocX, self.curLocY] = 1
      print(self.map[self.curLocX, self.curLocY], "has been marked as visited")

  """Moves to the next location based on the current direction.
    If it is not possible to move in the current direction, it rotates the movements clockwise."""

  def move_to_next_location(self):

    # Moving costs 1 energy
    self.currentEnergy -= 1
    if self.currentDirection == "right":
      if self.curLocY < self.map.shape[1] - 1 and self.visited[self.curLocX,
                                                               self.curLocY +
                                                               1] == 0:
        self.curLocY += 1
      else:
        self.currentDirection = "down"
    elif self.currentDirection == "down":
      if self.curLocX < self.map.shape[0] - 1 and self.visited[
          self.curLocX + 1, self.curLocY] == 0:
        self.curLocX += 1
      else:
        self.currentDirection = "left"
    elif self.currentDirection == "left":
      if self.curLocY > 0 and self.visited[self.curLocX,
                                           self.curLocY - 1] == 0:
        self.curLocY -= 1
      else:
        self.currentDirection = "up"
    elif self.currentDirection == "up":
      if self.curLocX > 0 and self.visited[self.curLocX - 1,
                                           self.curLocY] == 0:
        self.curLocX -= 1
      else:
        self.currentDirection = "right"

  """Moves the vacuum cleaner to the home location when the bag is full to restart
    or when the task is completed"""

  def go_home(self):

    # Each step home costs 1 energy
    self.currentEnergy -= 1

    if self.curLocX == 0 and self.curLocY == 0:
      return

    # Every move costs one energy
    while (curLocX > 0):
      self.currentEnergy -= 1
      self.curLocX -= 1
      break

    while (curLocY > 0):
      self.currentEnergy -= 1
      self.curLocY -= 1
      break

    if self.bagCapacity == 0:
      # Emptying the bag costs 1 energy
      self.currentEnergy -= 1
      print("Bag emptied. Back to work!")
      self.bagCapacity = 10
      self.move()
    return

  """Prints the final statistics when the work is done"""

  def print_stats(self):

    # Sending the final message costs 1 energy
    self.currentEnergy -= 1
    print("\n=====================")
    print("Job is done! Printing the results")
    print("=====================")
    print("Map:\n", self.map)
    print("Visited:\n", self.visited)
    print("Dirty:\n", self.dirt)
    print("Empty space in the bag:", self.bagCapacity)
    print("Energy left:", self.currentEnergy)
    print("\nCreated on 14 Feb 2024")


# Main part
# A variable to represent the map of the world
map = np.array([["A", "B", "C", "D"], ["E", "F", "G", "H"],
                ["I", "J", "K", "L"], ["M", "N", "O", "P"]])

# A variable to represent the state of the world
# 1 - dirty; 0 - clean
dirt = np.array([[0, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0], [1, 0, 1, 0]])

visited = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

# Set the current location to A
curLocX = 0
curLocY = 0
# Set the initial energy
currentEnergy = 100
# Set the current bag capacity
bagCapacity = 10
# Set the current direction
currentDirection = "right"

# Create an instance of the object and run move() to clean the room and go_home() after that
cleaner = VacuumCleaner(map, dirt, visited, curLocX, curLocY, currentEnergy,
                        bagCapacity, currentDirection)
cleaner.move()
cleaner.go_home()
cleaner.print_stats()
