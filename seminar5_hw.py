# Задача 3.
# Sample Input
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output
# [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
# Т.е. сгруппировать слова по "общим буквам ".

def group_words_with_same_letters(words: list):
    groups = {}
    set_list = []
    for i in words:
        tmp = set(i)
        if tmp not in set_list:
            set_list.append(tmp)
            groups[set_list.index(set(i))] = []
    for i in words:
        groups[set_list.index(set(i))].append(i)
    groups = list(groups.values())
    return groups


input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_words_with_same_letters(input_list))


# Задача 6.
# Дана строка (возможно,пустая),состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def compress_str(string):
    validation = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    if not set(string).issubset(validation):
        return "невалидная строка"
    result = ""
    count = 0
    last_index = len(string) - 1
    for i in range(len(string)):
        current_char = string[i]
        if i != last_index and current_char != string[i + 1]:
            result += current_char
            if count != 0:
                result += str(count + 1)
                count = 0
        else:
            count += 1
            if i == last_index:
                result += current_char + str(count)
    return result


input_str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
print(compress_str(input_str))
