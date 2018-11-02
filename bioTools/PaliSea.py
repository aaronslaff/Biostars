from time import time

def PaliSea (dna):
    # create a copy of the string that is uppercased and removes all '\n' characters with ''
    # if the string isn't standardized and '\n' characters are left, the length of the input
    # will be misrepresented
    D = dna.upper().replace('\n','') 
    
    # create a dictionary where:
    # key represents the index of the input 
    # values represent all sequences leading up to the index
    # input = '12345'
    ## if key = 5, dict[key] = ['12345', '2345', '345', '45', '5']) 
    chnk = {i:list(D[i:n+1] for i in range(0,n+1))[::-1] for i,n in enumerate(range(len(D)))}
    
    # create a dictionary where:
    # key represents the index of the input
    # values represent all palindromes that are at least 3 bases long and end at the index
    # input = 'babd'
    ## if key = 2, dict[key] = ['bab']
    ## if key = 1, dict[key] = []
    palin = {i:list(n for n in x if n == n[::-1] and len(n) > 2) for (i,x) in chnk.items()}
    
    # create a dictionary where:
    # key represents the index of the input
    # values represent only palindromes at least 3 bases long
    palincln = {i:n for (i,n) in palin.items() if n != []}

    # create a dictionary where:
    # key represents the name of Restriction enzyme
    # values represent the target 
    return '''Input: {} 
palindrome = {}'''.format(D, palincln)

input = '''GTGCTGAGAGTGTCCTGCCTGGTCCTCTGTGCCTGGTGGGGTGGGGGTGCCAGGTGTGTCCAGAGGAGCCCATTTGGTAGTGAGGCAGGTATGGGGCTAGAAGCACTGGTGCCCCTGGCCGTGATAGTGGCCATCTTCCT
GCTCCTGGTGGACCTGATGCACCGGCGCCAACGCTGGGCTGCACGCTACCCACCAGGCCCCCTGCCACTGCCCGGGCTGGGCAACCTGCT'''
iterations = 1

t1 = time()
longest1 = ''
for x in range(iterations):
    longest1 = PaliSea(input)
t2 = time()
tt = t2 - t1
print('''First iteration output: 
{0} 
time: {1} '''.format(longest1, tt))