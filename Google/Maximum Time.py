def maximumTime(s):
    s = list(s)
    if s[0] == "?":
        if s[1] == "?":
            s[0] = "2"
            s[1] = "3"
        elif int(s[1]) >= 0 and int(s[1]) < 4:
            s[0] = "2"
        elif int(s[1]) >= 0 and int(s[1]) <= 9:
            s[0] = "1"
    elif int(s[0]) == 2:
        if int(s[1]) == "?":
            s[1] = "3"
    elif int(s[0]) >= 0 and int(s[0]) < 2:
        if s[1] == "?":
            s[1] = "9"

    if s[3] == "?":
        s[3] = "5"
    if s[4] == "?":
        s[4] = "9"

    s = "".join(s)

    print(s)


if __name__ == "__main__":
    s = "??:5?"
    maximumTime(s)
