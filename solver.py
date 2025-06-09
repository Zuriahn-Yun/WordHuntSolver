from itertools import permutations
import io
import sys
import time

"""
Load all english words
"""
def load_dictionary(filepath):
    dictionary = {}
    with open(filepath, 'r') as file:
        for line in file:
            word = line.strip()
            word.lower()
            dictionary[word] = True 
    return dictionary


"""
Create the Word Hunt Matrix
"""
def convertToMatrix(input):
    res = []
    i = 0
    while i < len(input):
        if i % 4 == 0:
            if i != 0:
                res.append(curr)
            curr = []
            curr.append(input[i].lower())
        else:
            curr.append(input[i].lower())
            if i == len(input) - 1:
                res.append(curr)
        i +=1
    return res     

"""
This will print the table in Word Hunt Format
"""
def printWordHunt(table):
    for row in table:
        print(row)


"""
Depth-For-Search, not quite fast enough but it currently works
"""
def dfs(board, visited, i, j, path, dictionary,resDict):
    
    # Check bounds
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
        return
    
    # Check if already visited in this path
    if visited[i][j]:
        return
    
    # Add current letter 
    current_path = path + board[i][j]
    
    # Check if current path forms a valid word (minimum 3 letters)
    if len(current_path) >= 3 and current_path in dictionary:
        resDict[current_path] = [i+1,j+1]
    
    # Don't continue if path is getting too long
    if len(current_path) >= 15:
        return
    
    # Mark current cell as visited for this path
    visited[i][j] = True
    
    # Explore all 8 adjacent cells (including diagonals)
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        # Continue building the word
        dfs(board, visited, ni, nj, current_path, dictionary,resDict)
    
    # Unmark current cell so other paths can use it
    visited[i][j] = False
    
def main():
    # Loading Dictionary, any language can be used here, words.txt is just the english dictionary
    dictionary = load_dictionary('words.txt')
    
    # Load Input
    this = input()
    table = convertToMatrix(this)

    resDict = {}
    visited = [[False] * 4 for _ in range(4)]
    # Traverse the table 
    for i in range(len(table)):
        for j in range(len(table[i])):
            dfs(table,visited,i,j,"",dictionary,resDict)
        
    # Sort the Dictionary from shortest to longest
    sorted_dict = {k: resDict[k] for k in sorted(resDict, key=lambda k: len(k))}
    for key,value in sorted_dict.items():
        print("Word: " , key , " End Index:" ,  value)
    
"""
#   Example Word Hunt

    N A F Q 
    H I E G 
    M Y M E 
    A O D V
    
"""

if __name__ == "__main__":
    # Test Input
    # sys.stdin = io.StringIO("DATHSOETWMYNENIL")
    main()