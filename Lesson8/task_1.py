from collections import Counter, deque


def haffman_tree(string):
    characters = Counter(string)
    sorted_char = deque(sorted(characters.items(), key=lambda item: item[1]))

    if len(sorted_char) != 1:
        while len(sorted_char) > 1:
            repeat_sum = sorted_char[0][1] + sorted_char[1][1]
            union_elem = {0: sorted_char.popleft()[0], 1: sorted_char.popleft()[0]}

            for i, _count in enumerate(sorted_char):
                if repeat_sum > _count[1]:
                    continue
                else:
                    sorted_char.insert(i, (union_elem, repeat_sum))
                    break
            else:
                sorted_char.append((union_elem, repeat_sum))

    else:
        repeat_sum = sorted_char[0][1]
        union_elem = {0: sorted_char.popleft()[0], 1: None}
        sorted_char.append((union_elem, repeat_sum))

    return sorted_char[0][0]


code = {}


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code[tree] = path
    else:
        haffman_code(tree[0], f'{path}0')
        haffman_code(tree[1], f'{path}1')


s = 'abcaaab'
haffman_code(haffman_tree(s))
print(code)

for i in s:
    print(code[i], end='')


