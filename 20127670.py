
#read file text

readFile = open(".\\GAUSS_JORDAN\\input.txt", "r")
matrix = [[float(num) for num in line.split()] for line in readFile.readlines()]


"""LIST_INPUT EXAMPLE:
A. ==> CO MATRAN NGHICH DAO
1 2 1
3 7 3
2 3 4

B. ==> CO MATRAN NGHICH DAO
1 -1 2
1 1 -2
1 1 4

C. ==> CO MATRAN NGHICH DAO
1 2 3
2 5 3 
1 0 8

D. ==> KHONG CO MATRAN NGHICH DAO
-1 3 -4
2 4 1
-4 2 -9

"""


# HAM NHAN HE SO TREN DONG
def multiply_scalar_matrix(matrix, scalar):
    for j in range(len(matrix)):
        matrix[j] = matrix[j] * scalar
    return matrix

#HAM PRINT MATRIX
def printMatrix(matrix):
    for num in range(len(matrix)):
        print(matrix[num])


# HAM KIEM TRA 1 DONG CO FULL ZERO HAY KO
def checkZeroRow(matrix):
    total = 0
    n = int(len(matrix)/2)
    for i in range(n):
        if (matrix[i] == float(-0.0) or matrix[i] == float(0.0)):
            total = total + 1

    return True if total == n else False


# HAM KIEM TRA FLOATING POINT NHAN HAY CHIA CO RA SO TAO` LAO HAY KO :V()
def checkOutOfNumber(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if abs(matrix[i][j]) > 2000000000000:
                return True
    return False


# HAM BIEN DOI SO CAP TREN DONG 
def rowTransition(index, current, scalar):
    scalar = float(scalar)
    for col in range(len(index)):
        current[col] = current[col] - scalar * index[col]
    return current

###
def inverse(matrix):
    n = len(matrix)

    #MO RONG MA TRAN THAY VI PHAI TAO. MATRIX IDENTIFY KHAC 
    for rows in range(n):
        matrix[rows].extend([float(1) if cols == rows else float(0) for cols in range(n)])
    

    print("========ORIGIN MATRIX INPUT========")
    printMatrix(matrix)

    for i in range(n):
        #KIEM TRA XEM CO HANG NAO FULLZERO SAU KHI CHUYEN VI HAY KHONG 
        if checkZeroRow(matrix[i]):
            print("Ma tran khong kha nghich")
            return None


        #neu leading == 0 thi se tim dong khac co leading khac 0 de swap
        if matrix[i][i] == float(0):
            for k in range(i +1,n):
                if matrix[k][i] != float(0):
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break
            # khong tim dc leading nao != 0 ==> khong co ma tran kha nghich
            else:
                print("Ma tran khong kha nghich")
                return None

        if matrix[i][i] != float(1):
            # Bien leading thanh 1 (hang ngang)
            scalar_leading = 1 / matrix[i][i]
            matrix[i] = multiply_scalar_matrix(matrix[i], scalar_leading)
        
        
        # bien doi so cap tren dong
        for j in range(i + 1, n):
            next_leading = matrix[j][i]
            matrix[j] = rowTransition(matrix[i], matrix[j], next_leading)
    
            #KIEM TRA XEM CO HANG NAO FULLZERO SAU KHI CHUYEN VI HAY KHONG 
            if checkZeroRow(matrix[j]):
                print("Ma tran khong kha nghich")
                return None

    # NEU TON TAI 1 PHAN TU TRONG MANG CO SO VUOT QUA NGUONG~ CHO PHEP ==> LOI~ FLOATING POINT ==> KHONG TON TAI MA TRAN
    if checkOutOfNumber(matrix):
        print("Ma tran khong kha nghich")
        return None

    print("========MATRIX AFTER GAUSS_ELIMINATION========")
    printMatrix(matrix)

    # BIEN DOI BAC THANG PHIA TREN
    for i in range(n - 1, 0, -1): # chay nguoc 1 < n-1
        for j in range(i):
            current_leading = matrix[j][i]
            matrix[j] = rowTransition(matrix[i],matrix[j],current_leading)
            


    print("========MATRIX AFTER GAUSS_JORDAN========")
    printMatrix(matrix)
    inverse = matrix.copy()

    # TACH MA TRAN SAU RA ==>
    for row in range(n):
        inverse[row] = inverse[row][n:]
    return inverse



#### main <==
inverse = inverse(matrix)
print("========MA TRAN NGHICH DAO CUA MATRIX LA========")
if inverse != None:
    for lines in inverse:
        print(lines)