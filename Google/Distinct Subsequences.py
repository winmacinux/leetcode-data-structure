# Python3 program for above approach

# Returns count of distinct
# subsequences of str.


def countSub(s):

    Map = {}

    # Iterate from 0 to length of s
    for i in range(len(s)):
        Map[s[i]] = -1

    allCount = 0
    levelCount = 0

    # Iterate from 0 to length of s
    for i in range(len(s)):
        c = s[i]

        # Check if i equal to 0
        if (i == 0):
            allCount = 1
            Map = 1
            levelCount = 1
            continue

        # Replace levelCount with
        # allCount + 1
        levelCount = allCount + 1

        # If map is less than 0
        if (Map < 0):
            allCount = allCount + levelCount
        else:
            allCount = allCount + levelCount - Map

        Map = levelCount

    # Return answer
    return allCount


# Driver Code
List = ["abab", "gfg"]

for s in List:
    cnt = countSub(s)
    withEmptyString = cnt + 1

    print("With empty string count for",
          s, "is", withEmptyString)
    print("Without empty string count for",
          s, "is", cnt)

# This code is contributed by rag2127
