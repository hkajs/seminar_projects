# Prime Number Game with AI
# Anthony Schalhoub & Charles Zhang
# Problem Solving
# Dr. Shasha
from random import randint

playerMove = 1
gameround = 1
pp = 0
grid = []
cpup = 0
print('These are the possible spots to place your prime numbers')
print('1' + ' ' + '2' + ' ' + '3')
print('4' + ' ' + '5' + ' ' + '6')
print('7' + ' ' + '8' + ' ' + '9'+'\n')
print('This is what the grid actually currently is (x means the spot is open):')

for x in range(1,10):
        grid.append('x')
aitest = list(grid)


def print_grid():
        print(str(grid[0]) + ' ' + str(grid[1]) + ' ' + str(grid[2]))
        print(str(grid[3]) + ' ' + str(grid[4]) + ' ' + str(grid[5]))
        print(str(grid[6]) + ' ' + str(grid[7]) + ' ' + str(grid[8]))

primes = [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
        157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 233, 239,
        241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
        317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
        401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
        479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
        571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
        647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
        739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
        827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
        919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

prime_list = list(map(str, primes))

def makes_prime(a):
        counter = 0
        if a in prime_list:
                counter += 1
        return counter
                
                
        

def player_turn(array):
        x = int(input('what number from 0-9 would you like to place? '))
        y = int(input('where do you want to place this number (1 to 9)? '))-1
        points = 0
        while array[y] != 'x':
                y = int(input('please choose an open spot: '))-1
                while y < 0 or y > 8:
                        y = int(input('please choose a legal spot: '))-1
        while x == 0 and (y != 4):
                y = int(input("0's must be in the center choose another spot: "))-1
                while y < 0 or y > 8:
                        y = int(input('please choose a legal spot: '))-1
        while y < 0 or y > 8:
                y = int(input('please choose a legal spot: '))-1
        while x < 0 or x > 9:
                x = int(input('please choose a single digit number from 0-9: '))

        array[y] = str(x)
        if y == 0:
                points = makes_prime(array[0] + array[3] + array[6])
                points += makes_prime(array[0] + array[4] + array[8])
                points += makes_prime(array[0] + array[1] + array[2])
                points += makes_prime(array[6] + array[3] + array[0])
                points += makes_prime(array[8] + array[4] + array[0])
                points += makes_prime(array[2] + array[1] + array[0])
        elif y == 1:
                points = makes_prime(array[0] + array[1] + array[2])
                points += makes_prime(array[1] + array[4] + array[7])
                points += makes_prime(array[2] + array[1] + array[0])
                points += makes_prime(array[7] + array[4] + array[1])
        elif y == 2:
                points = makes_prime(array[0] + array[1] + array[2])
                points += makes_prime(array[6] + array[4] + array[2])
                points += makes_prime(array[2] + array[5] + array[8])
                points += makes_prime(array[2] + array[1] + array[0])
                points += makes_prime(array[2] + array[4] + array[6])
                points += makes_prime(array[8] + array[5] + array[2])
        elif y == 3:
                points = makes_prime(array[0] + array[3] + array[6])
                points += makes_prime(array[6] + array[3] + array[0])
                points += makes_prime(array[3] + array[4] + array[5])
                points += makes_prime(array[5] + array[4] + array[3])
        elif y == 4:
                points = makes_prime(array[0] + array[4] + array[8])
                points += makes_prime(array[8] + array[4] + array[0])
                points += makes_prime(array[3] + array[4] + array[5])
                points += makes_prime(array[5] + array[4] + array[3])
                points += makes_prime(array[6] + array[4] + array[2])
                points += makes_prime(array[2] + array[4] + array[6])
                points += makes_prime(array[1] + array[4] + array[7])
                points += makes_prime(array[7] + array[4] + array[1])
        elif y == 5:
                points = makes_prime(array[3] + array[4] + array[5])
                points += makes_prime(array[5] + array[4] + array[3])
                points += makes_prime(array[2] + array[5] + array[8])
                points += makes_prime(array[8] + array[5] + array[2])
        elif y == 6:
                points = makes_prime(array[0] + array[3] + array[6])
                points += makes_prime(array[6] + array[3] + array[0])
                points += makes_prime(array[6] + array[7] + array[8])
                points += makes_prime(array[8] + array[7] + array[6])
                points += makes_prime(array[6] + array[4] + array[2])
                points += makes_prime(array[2] + array[4] + array[6])
        elif y == 7:
                points = makes_prime(array[1] + array[4] + array[7])
                points += makes_prime(array[7] + array[4] + array[1])
                points += makes_prime(array[6] + array[7] + array[8])
                points += makes_prime(array[8] + array[7] + array[6])
        elif y == 8:
                points = makes_prime(array[6] + array[7] + array[8])
                points += makes_prime(array[8] + array[7] + array[6])
                points += makes_prime(array[2] + array[5] + array[8])
                points += makes_prime(array[8] + array[5] + array[2])
                points += makes_prime(array[0] + array[4] + array[8])
                points += makes_prime(array[8] + array[4] + array[0])
        return points


def cpu_turn(array):
        points = 0
        mem = array
        decide = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
        if gameround > 2:
                for y in range(0,8):
                        if y == 0 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[0] = x
                                        points = makes_prime(array[0] + array[3] + array[6])
                                        points += makes_prime(array[0] + array[4] + array[8])
                                        points += makes_prime(array[0] + array[1] + array[2])
                                        points += makes_prime(array[6] + array[3] + array[0])
                                        points += makes_prime(array[8] + array[4] + array[0])
                                        points += makes_prime(array[2] + array[1] + array[0])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['0'] = int(store)                             
                        elif y == 1 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[1] = x
                                        points = makes_prime(array[0] + array[1] + array[2])
                                        points += makes_prime(array[1] + array[4] + array[7])
                                        points += makes_prime(array[2] + array[1] + array[0])
                                        points += makes_prime(array[7] + array[4] + array[1])                                                                   
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['1'] = int(store) 
                        elif y == 2 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[2] = x
                                        points = makes_prime(array[0] + array[1] + array[2])
                                        points += makes_prime(array[6] + array[4] + array[2])
                                        points += makes_prime(array[2] + array[5] + array[8])
                                        points += makes_prime(array[2] + array[1] + array[0])
                                        points += makes_prime(array[2] + array[4] + array[6])
                                        points += makes_prime(array[8] + array[5] + array[2])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['2'] = int(store) 
                        elif y == 3 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[3] = x
                                        points = makes_prime(array[0] + array[3] + array[6])
                                        points += makes_prime(array[6] + array[3] + array[0])
                                        points += makes_prime(array[3] + array[4] + array[5])
                                        points += makes_prime(array[5] + array[4] + array[3])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['3'] = int(store) 
                        elif y == 4 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[4] = x
                                        points = makes_prime(array[0] + array[4] + array[8])
                                        points += makes_prime(array[8] + array[4] + array[0])
                                        points += makes_prime(array[3] + array[4] + array[5])
                                        points += makes_prime(array[5] + array[4] + array[3])
                                        points += makes_prime(array[6] + array[4] + array[2])
                                        points += makes_prime(array[2] + array[4] + array[6])
                                        points += makes_prime(array[1] + array[4] + array[7])
                                        points += makes_prime(array[7] + array[4] + array[1])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['4'] = int(store) 
                        elif y == 5 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[5] = x
                                        points = makes_prime(array[3] + array[4] + array[5])
                                        points += makes_prime(array[5] + array[4] + array[3])
                                        points += makes_prime(array[2] + array[5] + array[8])
                                        points += makes_prime(array[8] + array[5] + array[2])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['5'] = int(store) 
                        elif y == 6 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[6] = x
                                        points = makes_prime(array[0] + array[3] + array[6])
                                        points += makes_prime(array[6] + array[3] + array[0])
                                        points += makes_prime(array[6] + array[7] + array[8])
                                        points += makes_prime(array[8] + array[7] + array[6])
                                        points += makes_prime(array[6] + array[4] + array[2])
                                        points += makes_prime(array[2] + array[4] + array[6])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['6'] = int(store) 
                        elif y == 7 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[7] = x
                                        points = makes_prime(array[1] + array[4] + array[7])
                                        points += makes_prime(array[7] + array[4] + array[1])
                                        points += makes_prime(array[6] + array[7] + array[8])
                                        points += makes_prime(array[8] + array[7] + array[6])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['7'] = int(store) 
                        elif y == 8 and array[y] == 'x':
                                test = 0
                                store = '0'
                                for x in range(1,10):
                                        array = list(mem)
                                        x = str(x)
                                        array[8] = x
                                        points = makes_prime(array[6] + array[7] + array[8])
                                        points += makes_prime(array[8] + array[7] + array[6])
                                        points += makes_prime(array[2] + array[5] + array[8])
                                        points += makes_prime(array[8] + array[5] + array[2])
                                        points += makes_prime(array[0] + array[4] + array[8])
                                        points += makes_prime(array[8] + array[4] + array[0])
                                        if x == 1:
                                                test = points
                                                store = x
                                        elif points > test:
                                                test = points
                                                store = x
                                        points = 0
                                decide['8'] = int(store)
                #print(decide)
                z = max(decide.items(), key=lambda k: k[1])
                if z[1] == 0:
                        z = list(z)
                        z[1] = 1
                        z = tuple(z)
                print('ai move (location and number):')
                print(int(z[0])+1,z[1])
                grid[int(z[0])] = str(z[1])
                if z[0] == '0':
                        points += makes_prime(grid[0] + grid[3] + grid[6])
                        points += makes_prime(grid[0] + grid[4] + grid[8])
                        points += makes_prime(grid[0] + grid[1] + grid[2])
                        points += makes_prime(grid[6] + grid[3] + grid[0])
                        points += makes_prime(grid[8] + grid[4] + grid[0])
                        points += makes_prime(grid[2] + grid[1] + grid[0])
                elif z[0] == '1':
                        points += makes_prime(grid[0] + grid[1] + grid[2])
                        points += makes_prime(grid[1] + grid[4] + grid[7])
                        points += makes_prime(grid[2] + grid[1] + grid[0])
                        points += makes_prime(grid[7] + grid[4] + grid[1])
                elif z[0] == '2':
                        points += makes_prime(grid[0] + grid[1] + grid[2])
                        points += makes_prime(grid[6] + grid[4] + grid[2])
                        points += makes_prime(grid[2] + grid[5] + grid[8])
                        points += makes_prime(grid[2] + grid[1] + grid[0])
                        points += makes_prime(grid[2] + grid[4] + grid[6])
                        points += makes_prime(grid[8] + grid[5] + grid[2])
                elif z[0] == '3':
                        points += makes_prime(grid[0] + grid[3] + grid[6])
                        points += makes_prime(grid[6] + grid[3] + grid[0])
                        points += makes_prime(grid[3] + grid[4] + grid[5])
                        points += makes_prime(grid[5] + grid[4] + grid[3])
                elif z[0] == '4':
                        points += makes_prime(grid[0] + grid[4] + grid[8])
                        points += makes_prime(grid[8] + grid[4] + grid[0])
                        points += makes_prime(grid[3] + grid[4] + grid[5])
                        points += makes_prime(grid[5] + grid[4] + grid[3])
                        points += makes_prime(grid[6] + grid[4] + grid[2])
                        points += makes_prime(grid[2] + grid[4] + grid[6])
                        points += makes_prime(grid[1] + grid[4] + grid[7])
                        points += makes_prime(grid[7] + grid[4] + grid[1])
                elif z[0] == '5':
                        points += makes_prime(grid[3] + grid[4] + grid[5])
                        points += makes_prime(grid[5] + grid[4] + grid[3])
                        points += makes_prime(grid[2] + grid[5] + grid[8])
                        points += makes_prime(grid[8] + grid[5] + grid[2])
                elif z[0] == '6':
                        points += makes_prime(grid[0] + grid[3] + grid[6])
                        points += makes_prime(grid[6] + grid[3] + grid[0])
                        points += makes_prime(grid[6] + grid[7] + grid[8])
                        points += makes_prime(grid[8] + grid[7] + grid[6])
                        points += makes_prime(grid[6] + grid[4] + grid[2])
                        points += makes_prime(grid[2] + grid[4] + grid[6])
                elif z[0] == '7':
                        points += makes_prime(grid[1] + grid[4] + grid[7])
                        points += makes_prime(grid[7] + grid[4] + grid[1])
                        points += makes_prime(grid[6] + grid[7] + grid[8])
                        points += makes_prime(grid[8] + grid[7] + grid[6])
                elif z[0] == '8':
                        points += makes_prime(grid[6] + grid[7] + grid[8])
                        points += makes_prime(grid[8] + grid[7] + grid[6])
                        points += makes_prime(grid[2] + grid[5] + grid[8])
                        points += makes_prime(grid[8] + grid[5] + grid[2])
                        points += makes_prime(grid[0] + grid[4] + grid[8])
                        points += makes_prime(grid[8] + grid[4] + grid[0])
                return points
        else:
                p = randint(0,8)
                while grid[p] != 'x':
                        p = randint(0,8)
                grid[p] = '1'
                return 0

while gameround <= 9:
        print('current round: ' + str(gameround-1))
        print_grid()
        print('\n')
        aitest = list(grid)
        if gameround == 9:
                cpup += cpu_turn(aitest)
        elif gameround%2 == 0:
                cpup += cpu_turn(aitest)
        else:
                pp += player_turn(grid)
        print('human has ' + str(pp) + ' points')
        print('cpu has ' + str(cpup) + ' points')
        print('\n')
        gameround += 1

if gameround > 9:
        print_grid()
        print('\n')
        print('human ended with ' + str(pp) + ' points')
        print('cpu ended with ' + str(cpup) + ' points')
        print('\n')
        if pp > cpup:
                print('the human has won')
        elif cpup > pp:
                print('the cpu has won')
        else:
                print('it was a tie')

