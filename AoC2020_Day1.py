#Aoc Day 1

#part 1
my_list = list(open('aoc2020_d1_data.txt'))

alpha = 0

def round1(a):
    b = 0
    while b < len(my_list):
        if int(my_list[a])+int(my_list[b]) == 2020:
            print('a*b is ', (int(my_list[a]))*int((my_list[b])))
            print('a = ', my_list[a], 'b = ', my_list[b])
            b+=1

        else:
            b +=1


while alpha < len(my_list):
    round1(alpha)
    alpha +=1

#Known issue:
#prints the solution twice; dunno why

#Answer:
#902451


#part 2

cedric = 0

def round2(c, d):
    e = 0
    while e < len(my_list):
        if int(my_list[c])+int(my_list[d])+int(my_list[e]) == 2020:
            print('c*d*e is ', (int(my_list[c]))*int(my_list[d])*int(my_list[e]))
            print('c = ', my_list[c], 'd = ', my_list[d], 'e = ', my_list[e])
            e+=1
        else:
            e +=1

def round3(cornelius):
    digger = 0
    while digger < len(my_list):
        round2(cornelius, digger)
        digger +=1

while cedric < len(my_list):
    round3(cedric)
    cedric +=1

#Known issue:
#prints the solution 6 times

#Answer:
#85555470
    
