import numpy as np
import csv
import random
from collections import deque
import math

# Define the state space

def buildGrid():
    # Create a 26 x 32 array filled with None values
    grid = np.full((26, 32), None)
    
    # Add 'Truck' at the center of the middle row of the left column of the grid
    grid[13, 0] = 'Truck'
    
    # Add 'Collect' at the center of the middle row of the right column of the grid
    grid[13, -1] = 'Collect'

    # Return the completed grid
    return grid

def populateGrid(grid):
    # Open the CSV file and read the data into a list of dictionaries
    rows = []
    with open('data/article_data_with_correlations.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)

    # Shuffle the list of rows randomly
    random.shuffle(rows)

    # Calculate the number of rows and columns based on the size of the grid
    num_rows, num_cols = grid.shape
    num_articles = min(len(rows), num_rows*num_cols-2)  # Limit the number of articles to the available grid space

    # Iterate through the shuffled list of rows and add each article to a unique location in the grid
    for i in range(num_articles):
        row_index = i // num_cols  # Calculate the row index based on the current index and number of columns
        col_index = i % num_cols   # Calculate the column index based on the current index and number of columns
        if row_index+1 < num_rows-1 and col_index+1 < num_cols-1:  # Check that the location is within the bounds of the grid
            grid[row_index+1, col_index+1] = rows[i]  # Add the current article to the grid at the calculated location
    
    return grid

# Define the action space

def swap(grid, row1, col1, row2, col2):
    # Store the articles in the given locations
    article1 = grid[row1, col1]
    article2 = grid[row2, col2]

    # Swap the locations of the articles
    grid[row1, col1] = article2
    grid[row2, col2] = article1

    return grid

# Pathfinding

def find_location(grid, artno_val):
    for i, row in enumerate(grid):
        for j, obj in enumerate(row):
            if isinstance(obj, dict) and obj.get('ARTNO') == artno_val:
                return (i, j)
    return None

def shortestPath(grid, artno1, artno2):
    loc1 = getArticleLocation(grid, artno1)
    loc2 = getArticleLocation(grid, artno2)

    if loc1 is not None and loc2 is not None:  # Ensure that loc1 and loc2 are not None
        return math.sqrt(((loc1[0] - loc2[0]) ** 2) + ((loc1[1] - loc2[1]) ** 2))
    else:
        return None

def getArticleLocation(grid, article):
    article += '.0'

    for i, column in enumerate(grid):
        for j, row in enumerate(column):
            if (row is not None and row != 'Truck' and row != 'Collect'):
                if(row['ARTNO'] == article):
                    return (i, j)

def createDistanceMatrix(pick):
    locations = {}

    print(pick)

    for article in pick:
        locations.update({article: getArticleLocation(article)})

    print(locations)

grid = buildGrid()
grid = populateGrid(grid)

distance = shortestPath(grid, '10056770', '10178601')


artno_val = '40499002.0'
location = find_location(grid, artno_val)
print(location)

# pick = ['10056770', '10178601']

# createDistanceMatrix(pick)



# # Print out the resulting grid for debugging purposes
# print('pre swap grid', grid[0])
# grid = swap(grid, 0, 1, 2, 3)
# print('post swap grid', grid[0])



