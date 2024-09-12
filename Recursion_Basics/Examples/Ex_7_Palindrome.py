def is_pali(txt: str, i: int, j: int) -> bool:
    if i >= j:
        return True
    return txt[i] == txt[j] and is_pali(txt, i + 1, j - 1)


if __name__ == '__main__':
    inputs = ["abbcbba", "abba", "sidangore", "racexcar"]
    for i in inputs:
        print(i, " = ", is_pali(i, 0, len(i) - 1))