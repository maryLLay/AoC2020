#This version works by turning the string into a binary number
#and finding the largest number


my_list = list(open('aoc2020_d5_data.txt'))
biggest = 0
boarding_pass = 0

#Changes boarding pass into binary code
for item in my_list:
    number = []
    for n,x  in enumerate(item):
        if x == "B" or x == "R":
            number.append('1')
        else:
            number.append('0')
    number = int("".join(number))
    if int(number) > biggest:
        biggest = number
        boarding_pass = item

print(biggest)
print(boarding_pass)

#Converts biggest to a seat ID
#AoC Day 5 part 1, 2020


#my_range = (0, 127)  #at the end, subtract 1 for accurate results?


low_bound = 0
up_bound = 127
left_bnd = 0
right_bnd = 7

my_code = boarding_pass

def F(low, up, n):
    #return upper bound
    return low + (128 / 2**(n+1)) -1       
    
def B(low, up, n):
    #return low_bound
    return up - (128 / 2**(n+1)) +1

def R(left, right, x):
    #returns left bound
    x = x - 6
    return left + (8 / 2**(x))

def L(left, right, x):
    #returns right bound
    x = x - 6
    return right - (8 / 2**(x))




for key, letter in enumerate(my_code):
    if key == 6:
        if letter == 'F':
            row = low_bound
        else:
            row = up_bound
    elif key == 9:
        if letter == 'R':
            seat = right_bnd
        else:
            seat = left_bnd
            
    elif letter == 'F':
        up_bound = F(low_bound, up_bound, key)

    elif letter == 'B':
        low_bound = B(low_bound, up_bound, key)
    elif letter == 'R':
        left_bnd = R(left_bnd, right_bnd, key)
    elif letter == 'L':
        right_bnd = L(left_bnd, right_bnd, key)



print (row)
print(seat)

seat_id = row*8+seat
print(seat_id)


#987 is too low
#1031 is highest possible, and we don't have anything that high

#990 is too low
#1006 is too high



#By Hand:
#BBBBFBBRRR
#B = 64 - 127    64
#B = 96 - 127    32
#B = 112 - 127    16
#B = 120 - 127     8
#F = 120 - 123     4
#B = 122 - 123     2
#B = 123





#Changes binary back to boarding pass
#Doesn't work for some reason
biggest = str(biggest)
for y, z in enumerate(biggest):
    boarding_pass = []
    if y in range(0, 6):
        if z == "0":
            boarding_pass.append("F")
            print(boarding_pass)
        else:
            boarding_pass.append("B")
    if y in range (8, 10):
        if z == '0':
            boarding_pass.append("L")
        else:
            boarding_pass.append("R")

boarding_pass = "".join(boarding_pass)
print(boarding_pass)

            
