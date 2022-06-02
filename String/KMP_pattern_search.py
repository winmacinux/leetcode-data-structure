def computeLPSArray(pat, pattern_len, lps):
    # length of the previous longest predix suffix
    len = 0

    # lps[0] is always 0
    lps[0]
    i = 1

    while i < pattern_len:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def KMPSearch(pat, text):
    pattern_len = len(pat)
    text_len = len(text)

    # create lps (longest prefix suffix)
    lps = [0]*pattern_len

    # index for the pattern
    j = 0

    # preprocess the pattern
    computeLPSArray(pat, pattern_len, lps)

    # index of text
    i = 0

    while i < text_len:
        if pat[j] == text[i]:
            i += 1
            j += 1

        if j == pattern_len:
            print("Found pattern at index", str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < text_len and pat[j] != text[i]:
            # Do not match lps[0...lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1


if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    KMPSearch(pat, text)
