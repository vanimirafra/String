def char_frequency(str1):
    dict = {}
    for i in str1:
        keys = dict.keys()
        if i in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

