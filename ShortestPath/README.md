# Shortest Path

Shortest Path is a Python program that utilizes the breadth-first search algorithm and the queue data structure to find the shortest path from the start to the finish in a maze.

## Introduction

Shortest Path is designed to find the shortest path from the start ('O') to the finish ('X') in a maze. It uses the breadth-first search algorithm, which explores all possible paths from the start until it finds the finish. The program visualizes the algorithm's progress in real-time using the curses module.

## Learning Objectives

- Understanding and implementing the breadth-first search algorithm.
- Utilizing the queue data structure in Python.
- Visualizing algorithmic processes using the curses module.

## Features

- Utilizes the breadth-first search algorithm to find the shortest path.
- Visualizes the algorithm's progress in real-time using curses.
- Supports solving mazes of different sizes.
- Provides multiple predefined mazes for testing.

## Usage

1. Run the Python script `main.py`.
2. Follow the instructions displayed in the terminal:
   - Choose the size of the maze you want to solve (small, medium, or large).
   - Watch as the program finds the shortest path from the start to the finish.
   - Press any key to exit after the path is found.

## Mazes

The program includes predefined mazes for testing:

- **smaller_maze**: A smaller maze for testing purposes.
- **maze**: A medium-sized maze.
- **larger_maze**: A larger maze.

You can customize these mazes or define your own mazes in the code.

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/your-username/ShortestPath.git
   ```
Navigate to the correct directory:
   ```bash
   cd ../ShortestPath
   ```
Run the Python file:
   ```bash
   python main.py
   ```
