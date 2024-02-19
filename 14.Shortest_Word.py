# def find_short(s):
#     l = 100
#     words = s.split()
#     for word in words:
#         if len(word) < l:  
#             l = len(word)
#     return l # l: shortest word length


def find_short(s):
    return len(min(s.split(), key=len))



print(find_short("bitcoin take over the world maybe who knows perhaps"))