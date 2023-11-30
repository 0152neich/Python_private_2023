import math
def read_file(file_path):
    res = {'A': (), 'B': ()}

    with open(file_path, 'r') as file:
            
            line = file.readline().split()

            index_a = line.index('A')
            index_b = line.index('B')
            
            res['A'] = (float(line[index_a + 1]), float(line[index_a + 2]))
            res['B'] = (float(line[index_b + 1]), float(line[index_b + 2]))

    return res


def distance(A, B):
    return math.hypot(B[0] - A[0], B[1] - A[1])
    
file_path = 'input.txt'
res = read_file(file_path)

output_file_path = 'output.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write('A{} B{} AB = {:.2f}'.format(res['A'], res['B'], distance(res['A'], res['B'])))
