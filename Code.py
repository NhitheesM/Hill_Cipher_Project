import math
def getDetA(A,dim):
    if dim==2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    elif dim==3:
        return A[0][0]*(A[2][2]*A[1][1] - A[1][2]*A[2][1]) - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0]) + A[0][2]*(A[1][0]*A[2][1] - A[2][0]*A[1][1])

def getAdjA(A,dim):
    CoFactor = []
    if dim == 2:
        CoFactor = [[A[1][1],-A[0][1]],[-A[1][0],A[0][0]]]
    else:
        CoFactor = [[A[1][1]*A[2][2] - A[1][2]*A[2][1], -(A[1][0]*A[2][2] - A[1][2]*A[2][0]), A[1][0]*A[2][1] - A[2][0]*A[1][1]],
                    [-(A[0][1]*A[2][2] - A[0][2]*A[2][1]), A[0][0]*A[2][2] - A[0][2]*A[2][0], -(A[0][0]*A[2][1] - A[2][0]*A[0][1])],
                    [A[0][1]*A[1][2] - A[1][1]*A[0][2], -(A[0][0]*A[1][2] - A[0][2]*A[1][0]), A[0][0]*A[1][1] - A[1][0]*A[0][1]],
                   ]
    return CoFactor

def getTransposeA(A,dim):
    Atrans = []
    for i in range(dim):
        lst = []
        for j in range(dim):
            lst.append(A[j][i])
        Atrans.append(lst)

    return Atrans

def getAinv(A,dim):
    inv_det = modInverse(getDetA(A,dim),26)
    AdjA = getAdjA(A,dim)
    if dim == 3:
        AdjA = getTransposeA(AdjA,dim)
    
    for i in range(dim):
        for j in range(dim):
            AdjA[i][j] = mod(AdjA[i][j]*inv_det,26)
    return AdjA

def modInverse(a, m):
    g = math.gcd(a, m)
    if (g != 1):
        print("Inverse doesn't exist")

    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1
    
def mod(a,b):
    if a<0:
        x = a//b
        return (1-x)*b + a
    else:
        return a%b

def multiply_matrix_vec_encrypt(A,vec,dim):
    string =''
    for i in range(dim):
        temp = 0
        for j in range(dim):
            temp += (ord(vec[j]) - 97)*A[j][i]
        temp = mod(temp,26)
        string += chr(65 + temp)
    return string

def multiply_matrix_vec_decrypt(A,vec,dim):
    string =''
    for i in range(dim):
        temp = 0
        for j in range(dim):
            temp += (ord(vec[j]) - 65)*A[j][i]
        temp = mod(temp,26)
        string += chr(97 + temp)
    return string


def encryption(msg,A,dim):
    if len(msg)%dim != 0:
        msg += (dim - len(msg)%dim)*"x"
    msg = msg.lower()
    i=0
    temp = ""
    temp_list = []
    cipher_list = []
    c = 0
    while i<len(msg):
        temp +=msg[i]
        c+=1
        if c == dim:
            temp_list.append(temp)
            temp=""
            c=0
        i+=1
    
    for i in temp_list:
        cipher_list.append(multiply_matrix_vec_encrypt(A,i,dim))
    
    return cipher_list

def decryption(A,dim,cipher_list):
    Ainv = getAinv(A,dim)
    plain = []
    for i in cipher_list:
        plain.append(multiply_matrix_vec_decrypt(Ainv,i,dim))
    return plain


if __name__=="__main__":
    print("---------------------------------------------------")
    dim = int(input("Enter your Key Matrix Dimension (2 or 3):"))
    A = []
    print("-----Enter the values of Key Matrix row-wise-----")
    for i in range(dim):
        inp = input("Enter row " + str(i) + ": ").strip().split()
        A.append([int(x) for x in inp])

    #print(getAdjA(A,dim))
    
    for i in range(dim):
            for j in range(dim):
                A[i][j] = mod(A[i][j],26)

    x = getDetA(A,dim)
    #print(getAdjA(A,dim))
    if x==0 or modInverse(x,26)==-1:
        print("Can't proceed for encryption with the given key matrix try again...")
        exit()
    elif x<0:
        for i in range(dim):
            for j in range(dim):
                A[i][j] = mod(-A[i][j],26)
    choice=int(input(print("Enter 1 for Encryption\n      2 for Decryption")))
    if(choice==1):
        msg = input("Enter plain text: ")
        msg = msg.lower()
        cipher_list = encryption(msg,A,dim)
        cipher = "".join(cipher_list)
        print("Cipher text is:",cipher)
    elif(choice==2):
        msg = input("Enter Cipher text")
        msg = msg.upper()
        cipher_list=[]
        if(dim==2):
            for i in range(0,len(msg),2):
                cipher_list.append(msg[i:i+2])
        elif(dim==3):
            for i in range(0,len(msg),3):
                cipher_list.append(msg[i:i+3])
        print("Plain text is:","".join(decryption(A,dim,cipher_list)))

        
    

    

    