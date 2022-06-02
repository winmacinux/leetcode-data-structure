NO_OF_CHARS = 256


def search(pat, txt, q):
    M = len(pat)
    N = len(txt)

    i = 0  # index for pattern
    j = 0  # index for text

    p = 0  # hash value for pattern
    t = 0  # hash value for text

    h = 1  #

    for i in range(M-1):
        h = (h*NO_OF_CHARS) % q

    # Calculate the has value of pattern and text
    for i in range(M):
        p = (NO_OF_CHARS*p + ord(pat[i])) % q
        t = (NO_OF_CHARS*t + ord(txt[i])) % q

    for i in range(N-M+1):

        if p == t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1

            if j == M:
                print("Pattern found at index", i)

        if i < N - M:
            t = (NO_OF_CHARS*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

            if t < 0:
                t = t + q


# Driver Code
if __name__ == "__main__":
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"

    # A prime number
    q = 101

    search(pat, txt, q)
