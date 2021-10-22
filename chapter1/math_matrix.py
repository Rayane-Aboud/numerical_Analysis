#define wheater A is a matrix or no
def isMatrix(A):
    if len(A)==0:
        return False
    nbr_col=len(A[0])
    for l in A:
        if len(l)!=nbr_col:
            return False
    return True

def isMatrixSquare(A):#must use isMatrix
    nbr_rows=len(A)
    return nbr_rows==len(A[0])

#multiply two matrix A and B
def matrix_mul(A,B):
    if isMatrix(A)==False or isMatrix(B)==False:
        return []
    nbrRowA=len(A)
    nbrColA=len(A[0])
    nbrRowB=len(B)
    nbrColB=len(B[0])
    C=[]
    cRow=[]
    c=0
    if nbrColA!=nbrRowB:
        return []
    else:
        for i in range(nbrRowA):
            for j in range(nbrColB):
                for k in range(nbrColA):
                    c+=A[i][k]*B[k][j]
                cRow.append(c)
                c=0
            C.append(cRow)
            cRow=[]
        return C


def isNullVector(vector):
    lenvect=len(vector)
    for i in range(lenvect):
        if vector[i]!=0:
            return False
        return True


def sum2vectors(v1,v2):
    lenv1= len(v1)
    lenv2= len(v2)
    if lenv1==lenv2:
        return [[],False]
    v3=[]
    for i in range(lenv1):
        v3.append(v1[i]+v2[i])
    return v3
#v1=v1+v2
def add2vectors(v1,v2):
    lenv1= len(v1)
    lenv2= len(v2)
    if lenv1!=lenv2:
        return [[],False]
    
    for i in range(lenv1):
        v1[i]+=v2[i]
    


#multiply a real scalar and a vector
def mulScalVect(scal,vect):
    lenvect=len(vect)
    vectfunc=[]
    for i in range(lenvect):
        vectfunc.append(scal*vect[i])
    return vectfunc
                        
#swap two rows in the matrix A
def swap2rowsMat(A,i1,i2):#must use isMatrix first
    nbrRowA=len(A)
    if i1>=nbrRowA or i2>=nbrRowA:
        return False 
    rowLen=len(A[i1])
    for i in range(rowLen):
        tmp=A[i1][i]
        A[i1][i]=A[i2][i]
        A[i2][i]=tmp
    return True
#swap 2 colomns in the matrix A
def swap2colsMat(A,i1,i2):#must use isMatrix first
    nbrRowA=len(A)
    if i1>=nbrRowA or i2>=nbrRowA:
        return False 
    rowLen=len(A[i1])
    for i in range(rowLen):
        tmp=A[i][i1]
        A[i][i1]=A[i][i2]
        A[i][i2]=tmp
    return True
#generate an Id matrix of n degree
def idMatrix(n):
    I=[]
    Irow=[]
    for i in range(n):
        for j in range(n):
            if (i==j):
                Irow.append(1)
            else:
                Irow.append(0)
        I.append(Irow)
        Irow=[]
    return I

#generate a swap matrix
def SwapMatrix(n,i1,i2):
    I=idMatrix(n)
    swap2rowsMat(I,i1,i2)
    
    return I

def searchPivotLine(A,pivot):
    lenA=len(A)
    for i in range(pivot,lenA):
        if A[i][pivot]!=0:
            return [i,True]
    return [0,False]


#the general case of plu
def plu(A):
    
    
    if isMatrix(A)==False:
        return []
    
    nbrows=len(A)
    nbrCol=len(A[0])#because we have proven it was a matrix
    P=idMatrix(nbrows)
    L=idMatrix(nbrows)
    
    if nbrows>nbrCol:
        n=nbrCol
    else:
        n=nbrows
    
    for i in range(n):
        pivot=i
        if A[pivot][pivot]==0:
            srchp=searchPivotLine(A,pivot)

            if srchp[1]==True:
                swap2rowsMat(A,srchp[0],pivot)
                P=matrix_mul(P,SwapMatrix(nbrows,srchp[0],pivot))
                swap2rowsMat(L,srchp[0],pivot)
                swap2colsMat(L,srchp[0],pivot)
        if i==3:
            print("hello",A[i][i])
        for j in range (pivot+1,n):
            if A[pivot][pivot]!=0:
                L[j][pivot]=A[j][pivot]/A[pivot][pivot]
                add2vectors(A[j],mulScalVect(-1*A[j][pivot]/A[pivot][pivot],A[pivot]))
        
    return [P,L,A]

def abs(a):
    if a<0:
        return -1*a
    else:
        return a

def searchPivotPar(A,pivot):
    lenA=len(A)
    val=abs(A[pivot][pivot])
    r=pivot
    for i in range(pivot,lenA):
        if A[i][pivot]!=0:
            if abs(A[i][pivot])>val:
                r=i
    if val==0:
        return [0,False]
    else:
        return [r,True]

def pluPivPar(A):
    if isMatrix(A)==False:
        return []
    
    nbrows=len(A)
    nbrCol=len(A[0])#because we have proven it was a matrix
    P=idMatrix(nbrows)
    L=idMatrix(nbrows)
    
    if nbrows>nbrCol:
        n=nbrCol
    else:
        n=nbrows
    
    for i in range(n):
        pivot=i
        
        srchp=searchPivotPar(A,pivot)

        if srchp[1]==True:
            swap2rowsMat(A,srchp[0],pivot)
            P=matrix_mul(P,SwapMatrix(nbrows,srchp[0],pivot))
            swap2rowsMat(L,srchp[0],pivot)
            swap2colsMat(L,srchp[0],pivot)
            
        for j in range (pivot+1,n):
            if A[pivot][pivot]!=0:
                L[j][pivot]=A[j][pivot]/A[pivot][pivot]
                add2vectors(A[j],mulScalVect(-1*A[j][pivot]/A[pivot][pivot],A[pivot]))
        
    return [P,L,A]


