import regex as re

with open("14_Day/sample_data.txt", "r") as file:
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

grid_size = [11,7] # 11 wide and 7 tall!
number_of_seconds = 100

# positve x: robot moves right
# positv y: robot moives down
def make_move(grid_size, position, velocity):
    new_x = (position[0] + velocity[0]) % grid_size[0]
    new_y = (position[1] + velocity[1]) % grid_size[1]
    return new_x, new_y

for i in range(len(positions)):
    for _ in range(number_of_seconds):
        positions[i] = make_move(grid_size, positions[i], velocities[i])

print(positions)

