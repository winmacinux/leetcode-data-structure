import re

txt = "The rain in Spain"
x = re.search("rain", txt)
y = re.findall("rain", txt)
z = re.split("\s", txt)
z2 = re.split("\s", txt, 1)

# Replace all white replacements with 9
a = re.sub("\s", "9", txt)
# Replace the first 2 occurrences:
a2 = re.sub("\s", "9", txt, 2)

if x:
    print(x)
    print(x.span())
if y:
    print(y)
if z:
    print(z)
if z2:
    print(z2)
if a:
    print(a)
if a:
    print(a2)


# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"	
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"