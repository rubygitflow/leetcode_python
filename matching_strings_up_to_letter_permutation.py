# Matching strings up to letter permutation
# Дан текст T и строка S. Требуется найти подстроку S' в T такую, что она совпадает с S с точностью до перестановки букв.
# В качестве ответа стоит вернуть индекс первого вхождения, или -1, если такая подстрока S' не нашлась.
# ("reebok", "bee") -> 1

class Solution:
    def matchSubstring(self, hoststring: str, substring: str) -> int:
        match_len = len(substring)
        inp_len = len(hoststring)
        if inp_len < match_len:
            return -1
        def dfs(where: str) -> bool:
            stack_a = list(substring)
            for _i, c in enumerate(where):
                if c in stack_a:
                    stack_a.remove(c)
                else:
                    return False
            return True
        for i in range(inp_len - match_len + 1):
            if dfs(hoststring[i:i+match_len]):
                return i
        return -1

print(Solution().matchSubstring('reebokee', 'bee'))
# Output: 1
print(Solution().matchSubstring('colorados', 'dosar'))
# Output: 4
