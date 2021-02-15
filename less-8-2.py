# Закодируйте любую строку из трех слов по алгоритму Хаффмана.дополнительно: использовать Collections

from collections import Counter


def binary_tree(some_phrase):
    tree = Counter(some_phrase).most_common()
    while True:
        buffer = ({0: tree[-1][0], 1: tree[-2][0]},
                  tree.pop()[1] + tree.pop()[1])
        if len(tree) != 0:
            for idx, el in enumerate(tree):
                if el[1] >= buffer[1] and idx != len(tree) - 1:
                    continue
                elif el[1] < buffer[1]:
                    tree.insert(idx, buffer)
                    break
                else:
                    tree.append(buffer)
                    break
        else:
            tree = buffer
            break
    return tree[0]


def research_tree(tree, code=''):
    if not isinstance(tree, dict):
        CODE_TABLE[tree] = code
    else:
        research_tree(tree[0], code=f'{code}0')
        research_tree(tree[1], code=f'{code}1')


CODE_TABLE = {}
S = input("Введите строку из трех слов:\n")
research_tree(binary_tree(S))
for i in S:
    print(CODE_TABLE[i], end=' ')