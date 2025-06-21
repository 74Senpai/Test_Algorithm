def minimumDeletions(self, word: str, k: int) -> int:
    map_ch = {}
    for ch in word:
        if ch in map_ch:
            map_ch[ch] += 1
        else:
            map_ch[ch] = 1
    if len(map_ch) == 1 or k >= len(word):
        return 0
    k_word = word[k]
    delete = 0
    for key in map_ch:
        if map_ch[key] < map_ch[k_word]:
            delete += map_ch[key]
        elif map_ch[key] > map_ch[k_word] + k:
            delete += map_ch[key] - map_ch[k_word] - k
        
    return delete

print(minimumDeletions(None, "dabdcbdcdcd", 2))