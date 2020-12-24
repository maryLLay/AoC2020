#AoC Day 4, part 1- WORKS (kind of)

#separate entries by new lines

my_data = list(open('aoc2020_d4_data.txt'))
new_data = []
for alpha in my_data:
    new_data.append(alpha.split())


#obtaining an entry
n = 0
valid = 0



def isvalid(n, new_datay):
    counter = 0 #need 8 counters to = 1 validy
    while new_datay[n]!=[]:
        entry = new_datay[n]
        counter_list = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
        for x in entry:
            for y in counter_list:
                if y in x:
                    counter+=1
                if counter == 7:
                    validy =1
                else:
                    validy = 0
            
        n+=1
    return validy, n

while True:
    while new_data[n]!=[]:
        vent, nan = isvalid(n, new_data)
        n = nan
        valid = valid + vent
        
    if new_data[n] == []:
        n+=1

    print('valid entries = ', valid)



#This currently gives 205, but the correct answer is 206.
#Probably something to do with 'n' getting out of range.



    
