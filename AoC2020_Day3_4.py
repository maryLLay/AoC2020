#Day 3

#data setup
forest = list(open('aoc2020_d3_data.txt'))


#determine destination number
line_num = 0
tree = 0



for line in forest:
    line = line.strip()#Why is this required?
    destination_num = (line_num*3)%len(line)
    if line[destination_num] == '#':
        tree += 1
    line_num +=1

a = tree
print (tree)


#Part 2, 1x1

#use this to get whatever slopes you need
def trfor(r, d):  #r is how many spots right, d = how many spots down
    forest = list(open('aoc2020_d3_data.txt'))
    line_num = 0
    tree = 0
    while line_num < len(forest):
        line = forest[line_num]
        line = line.strip()
        destination_num = (line_num*r)%len(line)
        if line[destination_num] == '#':
            tree +=1
        line_num +=d
    print(tree)


