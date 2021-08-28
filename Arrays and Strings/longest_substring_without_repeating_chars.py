

def longest_substring(string):
    if (len(string) == 1):
        return 1
    m = []
    i = 0
    j = 0
    maxi = 0
    n = len(string)

    while (j < n):
        if (string[j] not in m):
            m.append (string[j])
            j+=1
            maxi = max(len(m), maxi)
        else:
             m.remove(string[i])
             i+=1
    return maxi



string = "abcdabdfghijkla"

result = longest_substring(string)

print(
    f"In the string {string}, the longest substring without repeating characters is \n {result} \n")

string2 = "pwwkew"

result2 = longest_substring(string2)

print(
    f"In the string {string2}, the longest substring without repeating characters is \n {result2}")

string3 = "bbbbb"

result3 = longest_substring(string3)

print(
    f"In the string {string3}, the longest substring without repeating characters is \n {result3}")
