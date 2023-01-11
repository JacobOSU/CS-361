# Name: Jacob Summers
# Date: 10.12.22
# Class: CS325 Section 400
# Assignment 3: Dynamic Programming - DNAMatch
# Description: Program contains methods for finding the length of the largest subsequence between 2 strands of DNA using
#           Dynamic programming via both the topdown and bottomup approaches.

def dna_match_topdown(DNA1, DNA2):
    """Function takes 2 DNA strings as parameters and returns the character count of the largest subsequence between the
    2 DNA strings. Uses dynamic programming topdown approach."""
    comp_array = [[-1 for i in range(len(DNA2) + 1)] for j in range(len(DNA1) + 1)]
    return dna_topdown_helper(DNA1, DNA2, len(DNA1), len(DNA2), comp_array)


def dna_topdown_helper(DNA1, DNA2, m, n, comp_array):
    """Helper function to dna_match_topdown method."""
    if m == 0 or n == 0:
        return 0
    if comp_array[m][n] != -1:
        return comp_array[m][n]
    if DNA1[m-1] == DNA2[n-1]:
        comp_array[m][n] = 1 + dna_topdown_helper(DNA1, DNA2, m-1, n-1, comp_array)
        return comp_array[m][n]
    else:
        comp_array[m][n] = max(dna_topdown_helper(DNA1, DNA2, m-1, n, comp_array), dna_topdown_helper(DNA1, DNA2, m, n-1, comp_array))
        return comp_array[m][n]




def dna_match_bottomup(DNA1, DNA2):
    """Function takes 2 DNA strings as parameters and returns the character count of the largest subsequence between the
        2 DNA strings. Uses dynamic programming bottomup approach."""
    cache = [[0 for x in range(len(DNA1) + 1)] for y in range(len(DNA2) + 1)]
    for i in range(len(DNA2)+1):
        for j in range(len(DNA1)+1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif DNA1[j-1] == DNA2[i-1]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])
    return cache[len(DNA2)][len(DNA1)]










#DNA1 = "ATAGTTCCGTCAAA"
DNA2 = "GTGTTCCCGTCAAA"
DNA3 = ''
DNA4 = 'AB'
#DNA5 = 'A'


#print(dna_match_topdown(DNA4, DNA5))
print(dna_match_bottomup(DNA2,DNA4))