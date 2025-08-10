# BFS Maze Solver
## 📌 Description

This project implements a Breadth-First Search (BFS) algorithm to find the shortest path in a maze.
The maze is represented as a 2D grid, where:
0 = open space
1 = wall
The program:
-  Takes a maze, start point, and end point
-  Finds the shortest path using BFS
-  Displays the maze in the console (with * marking the path)
-  Shows a simple visual representation of the maze and path using matplotlib.

## 🛠 Features

-  Shortest Path Guarantee: BFS always finds the shortest path in an unweighted grid.
-  Console Output: Prints the maze with path marked by *.
-  Basic Visualization: Black-and-white maze display with a red line for the path.
-  Customizable Colors: Maze wall colors can be changed easily.

## 📜 How It Works

BFS Algorithm

-  A queue is used to explore cells layer by layer.
-  Each step moves up, down, left, right (no diagonals).
-  Stops when the end is reached.

Path Tracking

-  Each position stores the path taken so far.
-  Once the end is found, the path is returned.

Display
-  Console display: * marks the shortest path

Visual display:

-  White = open path
-  Black = wall
-  Red = shortest path
