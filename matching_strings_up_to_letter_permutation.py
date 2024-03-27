# Matching strings up to letter permutation
# Дан текст T и строка S. Требуется найти подстроку S' в T такую, что она совпадает с S с точностью до перестановки букв.
# В качестве ответа стоит вернуть индекс первого вхождения, или -1, если такая подстрока S' не нашлась.
# ("reebok", "bee") -> 1

class Solution:
    def matchSubstring(self, input_str: str, substring: str) -> int:
        match_len = len(substring)
        inp_len = len(input_str)
        if inp_len < match_len:
            return -1
        def dfs(where: str) -> bool:
            # print('where',where)
            stack_a = list(substring)
            # print('stack_a',stack_a)
            for i, c in enumerate(where):
                if c in stack_a:
                    stack_a.remove(c)
                else:
                    return False
            return True
        for i in range(inp_len - match_len + 1):
            if dfs(input_str[i:i+match_len]):
                return i
        return -1

print(Solution().matchSubstring('reebokee', 'bee'))
# Output: 1
print(Solution().matchSubstring('colorados', 'dosar'))
# Output: 4
