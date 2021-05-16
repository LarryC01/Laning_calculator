# short porgram for new jayce players
def helper(s1, s2):
    if(len(s1)==len(s2)):
        for i in range(0,len(s1)):
            if(s1[i]!=s2[i]):
                print("Not Equal")
                break
            else:
                return True
    else:
        return False


print("Jayce abilities: Q > W > E\n\nWLOG flash on F button in the following steps<3\n")

print("What mode are you in?\n")

str = input().lower()

if (helper(str, "long") == False) and (helper(str, "short") == False):
    print("\nInvalid input, try again QwQ<3\n")
else:
    if (helper(str, "short") == True):
        print("\n3 combos in short mode, i.e. cannon:\n")
        print("EA,\nQW,\nQWAERAEWAAAQ\n")
    else:
        print("\n6 combos in long mode, i.e. hammer:\n")
        print("EQ,\nQE,\nAW,\nQFE,\nAQEWRQWAAEA,\nWQERFQWEA\n")
