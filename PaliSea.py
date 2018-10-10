from time import time

def PaliSea (dna):
    D = dna.upper().replace('\n','')
    chnk = {i:list(D[i:n+1] for i in range(0,n+1))[::-1] for i,n in enumerate(range(len(D)))}
    palin = {i:list(n for n in x if n == n[::-1]) for i,x in enumerate(chnk.values()) if }
    
    return '''Input: {} 
palindrome = {}'''.format(D, palin)

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