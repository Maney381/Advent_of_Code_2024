import regex as re
import numpy as np

with open("14_Day/data.txt", "r") as file:
    positions = []
    velocities = []
    while True:
        line = file.readline()
        if line:
            p, v = line.strip('\n').split(' ')
            p = re.findall(r'(?:p\=)(.+)', p)[0].split(',')
            v = re.findall(r'(?:v\=)(.+)', v)[0].split(',')
            positions.append([int(p[0]), int(p[1])])
            velocities.append([int(v[0]), int(v[1])])
        else:
            break

grid_size = [101,103] # 11 wide and 7 tall!
number_of_seconds = 100

# positve x: robot moves right
# positve y: robot moives down
def make_move(grid_size, positions, velocities):
    new_x = (positions[:,0] + velocities[:,0]) % grid_size[0]
    new_y = (positions[:,1] + velocities[:,1]) % grid_size[1]
    return np.column_stack((new_x, new_y))

def check_quadrants(grid_size, positions):
    # Calculate midpoints
    mid_x = (grid_size[0] - 1) / 2
    mid_y = (grid_size[1] - 1) / 2

    # Identify "in mid" positions
    in_mid = (positions[:, 0] == mid_x) | (positions[:, 1] == mid_y)

    # Calculate quadrants
    i = np.where(positions[:, 0] < mid_x, 0, 1)
    j = np.where(positions[:, 1] < mid_y, 0, 1)

    # Combine i and j into a tuple (quadrant index)
    quadrants = np.column_stack((i, j))

    # Return quadrants, skipping "in mid" positions
    return quadrants[~in_mid]

positions = np.array(positions)
velocities = np.array(velocities)

quadrant_dic = {(0,0):0, (0,1):0, (1,1):0, (1,0):0}
#for i in range(len(positions)):
for _ in range(number_of_seconds):
    positions = make_move(grid_size, positions, velocities)
    

# Get all quadrants for the current positions
quadrants = check_quadrants(grid_size, positions)

    # Count occurrences of each quadrant
for quadrant in quadrants:
    quadrant_dic[tuple(quadrant)] += 1

print(quadrant_dic)
count = 1
for quadrant, occurences in quadrant_dic.items():
    print(occurences)
    count *= occurences

print(count)
