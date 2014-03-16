choices = [1,2,5,10,20,50,100,200]
combinations = {1:1, 2:2}
def factors (n, index):
    """Factors: not actually called anywhere, but I wanted to prove I could do this.
    factors takes in an ints n and an index
    n is the number we are trying to determine the greatest factor of
    index is the index of n in choices.
    This program iterates through all coins in choices from index of n to 0
    returns a tuple where...
    tuple[0] is a number in choices, tuple[1] is some number x where tuple[0]*x = n
    Phew.  Hopefully that makes sense!""" 
    global choices
    #determines if one of the numbers is a factor of n
    #if so, a tuple of that number and the factor one would need to multiply by it is returned
    for i in xrange (index, 0, -1):
        if (n%(choices[i])==0):
            return (choices[i], n/choices[i])
    return None

def greedy_change(n, index):
    """Greedy_change is actually implemented in my code.
    As there are numbers like 5 and 50 in this list where one can only add to acchieve n (2+2+1 for instance)
    The factors method above cannot cover all cases, even if it is hypothetically slightly faster)
    takes in ints n and index (function in the same way as in factors)
    outputs a list of numbers that sum to n"""
    global choices
    c = choices[0:index]
    operands = []
    total = 0
    while len(c) is not 0:
        total = total + c[len(c)-1]
        operands.append(c[len(c)-1])
        if total >n:
            total = total - c[len(c)-1]
            del c[len(c)-1:]
            del operands[len(operands)-1:]
        if total == n:
            return operands
    return operands
        
def find_combinations_of(n):
    """Determines the total number of possible ways to create n from the coins avalable in global list choices.
takes in n (the change due essentially) uses global list choices (the available coin values) to generate the total number of
ways to create n with the coins available (assuming an infinate number of each coin in choices is avalable."""
    #Figure out the way to create n using the fewest number of numbers that aren't n
    fact = greedy_change (n, choices.index(n))
    total = 1
    for f in fact:
        print "f is: " + str(f)
        if f is 1 or f is 2:
            total+=1
            continue
        if f in combinations.keys():
            total *= combinations[f]
            continue
        else:
            combos = find_combinations_of(f)
            total*= combos

    combinations[n]=total
    return total 

print find_combinations_of(200)
print combinations


# Time complexity: O(n^2)
