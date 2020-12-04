#Aoc Day 2, version 2

#should be able to simplify this with list comprehensions (see notes)
#part 1

#setup
line_num = 0
good_psswrd = 0
goody_psswrd = 0

my_list = list(open('aoc2020_d2_data.txt'))

def func1(n): 
    #obtaining the range of numbers:
    #For a given line:
    lisa = str(my_list[n])
    inda = lisa.index('-')
    indb = lisa.index(' ')
    lw_bnd = int(lisa[0:inda])
    up_bnd = int(lisa[(inda+1):indb])

    #obtaining the letter of interest:
    indc = lisa.index(':')
    letter = lisa[indc-1]

    #isolating the password:
    length = len(lisa)
    psswrd = lisa[indc+2:length]

    return lw_bnd, up_bnd, letter, psswrd

def func2(lw_bnd, up_bnd, letter, psswrd):
    #counting number of times letter of interest appears:
    times = psswrd.count(letter)
    if times in range(lw_bnd, up_bnd+1):
        b = 1   
    else:
        b = 0
    return b

#part 2
#a = opta, b = optb, c = desired letter, d = password
def func3(opta, optb, letter, psswrd):
    if ((psswrd[(opta-1)]==letter) or (psswrd[(optb-1)]==letter)) and ((psswrd[int(opta-1)]!=letter) or (psswrd[int(optb-1)]!= letter)):
        good = 1
    else:
        good = 0
    return good

    
while line_num < len(my_list):
    a, b, c, d = func1(line_num)
    #a = lwbnd, b = upbnd, c = desired letter, d = password
    good_num = int(func2(a, b, c, d))
    goody_num = int(func3(a, b, c, d))
    line_num +=1
    good_psswrd = good_psswrd + good_num
    goody_psswrd = goody_psswrd + goody_num


print('good_psswrd round 1 = ', good_psswrd)
print('goody_psswrd round 2 = ', goody_psswrd)



    
            

        #if both 'or' statements are true, then b = 1
    
    

