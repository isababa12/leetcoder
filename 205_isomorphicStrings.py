def isIsomorphic(s, t):

    if len(s) != len(t):
        return False

    letter_map_s = {}
    letter_map_d = {}

    for letter_idx in range(len(s)):

        print(letter_map_s)

        if s[letter_idx] not in letter_map_s:
            letter_map_s[s[letter_idx]] = t[letter_idx]

        elif letter_map_s[s[letter_idx]] != t[letter_idx]:
            return False

    for letter_idx in range(len(t)):

        print(letter_map_d)

        if s[letter_idx] not in letter_map_d:
            letter_map_d[t[letter_idx]] = s[letter_idx]

        elif letter_map_d[t[letter_idx]] != s[letter_idx]:
            return False

    if letter_map_s != letter_map_d:
        return False

    return True


print(isIsomorphic('egg', 'add'))
