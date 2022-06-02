def moveZeros(A):
    l = len(A)
    read = l - 1
    write = l - 1
    
    while(read >= 0):
        print("read", read, A[read])
        if A[read] != 0:
            print("write", write, A[write])
            temp = A[write]
            A[write] = A[read]
            A[read] = temp
            write -= 1
        read -=1
    # return A


if __name__ == "__main__":
    v = [1, 10, 20, 0, 59, 88, 0, 63, 0]
    moveZeros(v)
    print(v)
