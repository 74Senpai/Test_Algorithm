class V1:
    def minimumDeletions(self, word: str, k: int) -> int:
        map_ch = {}
        for ch in word:
            if ch in map_ch:
                map_ch[ch] += 1
            else:
                map_ch[ch] = 1
        del_ = 10**5
        for x in map_ch:
            delete = 0
            for key in map_ch:
                if map_ch[key] < map_ch[x]:
                    delete += map_ch[key]
                elif map_ch[key] > map_ch[x] + k:
                    delete += map_ch[key] - map_ch[x] - k
            del_ = min(del_, delete)
        return del_

