
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    res=min(dict.key=dict.get())        
    
print(str(res))

