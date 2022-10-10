#non overlapping


sb = str(input("Introdu primul sir: ")) 
s = str(input("Introdu al doilea sir: "))

res = 0
sub_len = len(sb)
for i in range(len(s)):
    print(s[i:i+sub_len])
    if s[i:i+sub_len] == sb:
        res += 1
print(res)
