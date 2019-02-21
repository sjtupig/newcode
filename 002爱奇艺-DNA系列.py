s = input().strip()
le = 1
while True:
    child_str_set = set()
    for i in range(len(s)-le):
        child_str_set.add(s[i:i+le])
    if len(child_str_set) != 4**le:
        print(le)
        break
    le += 1