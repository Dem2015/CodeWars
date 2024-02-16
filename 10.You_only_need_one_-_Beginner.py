# Вам будет предоставлен массив aи значение x. Все, что вам нужно сделать, это проверить, содержит ли предоставленный массив значение.

# Массив может содержать числа или строки. Х может быть любым.

# Возврат, trueесли массив содержит значение, falseесли нет.


def check(seq, elem):
    # return seq.count(elem)
    return elem in seq


tests = [
    ([66, 101], 66, True),
    ([78, 117, 110, 99, 104, 117, 107, 115], 8, False),
    ([101, 45, 75, 105, 99, 107], 107, True),
    ([80, 117, 115, 104, 45, 85, 112, 115], 45, True),
    (['t', 'e', 's', 't'], 'e', True),
    (["what", "a", "great", "kata"], "kat", False),
    ([66, "codewars", 11, "alex loves pushups"], "alex loves pushups", True),
    (["come", "on", 110, "2500", 10, '!', 7, 15], "Come", False),
    (["when's", "the", "next", "Katathon?", 9, 7], "Katathon?", True),
    ([8, 7, 5, "bored", "of", "writing", "tests", 115], 45, False),
    (["anyone", "want", "to", "hire", "me?"], "me?", True),
]

for seq, elem, expected in tests:
    result = check(seq, elem)
    assert result == expected, f"For {seq}, expected: {expected}, but got: {result}"

print("All tests passed successfully!")