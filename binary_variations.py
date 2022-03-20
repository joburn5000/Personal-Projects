"""
Generate the number of possible binary combinations
given n bits.

Example: n = 3 bits
Variations possible:

000
001
010
011
100
101
110
111

Completed: 3/20/2022
"""

def generate_variations(n):
    variations = 2**n
    arr = [""]*variations
    for i in range(variations):
        for j in range(1,n+1):
            if int(i * 2**j / variations ) % 2:
                arr[i]+="1"
            else:
                arr[i]+="0"
    
    for variation in arr:
        print(variation)

n = 8
generate_variations(n)
