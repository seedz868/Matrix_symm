def create_symm(MATRIX):
    #global result_rows
    #global result_cols
    result_rows = []
    result_cols = []
    
    # Find point of symmetry for Rows: Use recursive binary search to find all possible ways to make rows symmetric.
    # t: We insert the row in the upper half into the lower half (the b index)
    # b: We insert the row in the lower half into the upper half (the t index)
    # d: Duplicates at t and b index, no insertions.
    def find_sym_R(mat, t,b, seq=''):

        if t>=b:
            result_rows.append(seq)
            return
        elif mat[t] == mat[b]:
            find_sym_R(mat, t+1, b-1, seq +'d')
        else:
            find_sym_R(mat,t+1,b,seq + 't')
            find_sym_R(mat,t,b-1,seq + 'b')

        return result_rows

    # Find point of symmetry for Cols: Use recursive binary search to find all possible ways to make cols symmetric.
    # l: We insert the col in the left half into the lower half (the r index)
    # r: We insert the col in the right half into the left half (the l index)
    # d: Duplicates at l and r index, no insertions.
    def find_sym_C(mat, l,r, seq=''):

        if l>=r:
            result_cols.append(seq)
            return
        elif [col[l] for col in mat] == [col[r] for col in mat]:
            find_sym_C(mat, l+1, r-1, seq +'d')
        else:
            find_sym_C(mat,l+1,r,seq +'l')
            find_sym_C(mat,l,r-1,seq + 'r')

        return result_cols
    
    ## Find ideal sequence for each row and col: Find the insertion sequence (seq) with the fewest inserts. 
    def find_ideal(array):
        ideal = array[0]
        for k in array:
            temp1 = k.replace('d','')
            temp2 = ideal.replace('d','')
            if len(temp1) < len(temp2):
                ideal = k
        return ideal
    
    
    find_sym_R(MATRIX,0, len(MATRIX)-1)
    find_sym_C(MATRIX,0, len(MATRIX[0])-1)
   
    ideal_R = find_ideal(result_rows)
    ideal_C = find_ideal(result_cols)
    
    # Insert ROWS
    t,b = 0, len(MATRIX) - 1
    i = 0
    while t<b and i < len(ideal_R):
        if ideal_R[i] == 'd':
            t+=1
            b-=1
        elif ideal_R[i] == 'b':
            MATRIX=MATRIX[:t] + [MATRIX[b]] + MATRIX[t:]
            t+=1
        else:
            MATRIX=MATRIX[:b] + [MATRIX[b]] + [MATRIX[t]] + MATRIX[b+1:]
            t+=1
        i+=1
    
    # insert COLS
    for k, row in enumerate(MATRIX):
        l,r = 0, len(row)-1
        i=0
        temp=row
        while l<r and i < len(ideal_C):
            if ideal_C[i] == 'd':
                l+=1
                r-=1
            elif ideal_C[i] == 'r':
                temp=temp[:l] + [temp[r]] + temp[l:]
                l+=1
            else:
                temp=temp[:r] + [temp[r]] + [temp[l]] + temp[r+1:]
                l+=1
            i+=1
        
        MATRIX[k] = temp
    return MATRIX



# Checks
def check_sym(mat):
    #cols
    for row in mat:
        if row != row[::-1]:
            return False
    
    #rows:
    for k, row in enumerate(mat):
        q = (-1)*(k+1)
        if row != mat[q]:
            return False
    
    return True

def print_mat(mat):
    for row in mat:
        print (row)



#Tests

#mat = [[0,0,1,0,0],  [0,1,1,1,0],  [1,0,0,0,1],   [0,0,1,0,0],  [0,1,0,0,0] ]
#mat = [[0,1,0,0],  [1,1,1,0],  [1,0,0,1],   [0,0,0,0],  [0,1,0,0] ]
mat = [[0,0,0],  [1,1,0],  [0,0,1],   [0,1,0],  [0,1,0] ]
#mat = [[0]]
#mat = [[11111]]

print_mat(mat)
rez = create_symm(mat)
print_mat(rez)
check_sym(rez)
