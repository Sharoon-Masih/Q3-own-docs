with open('G:/python/chap-9/poem.txt') as f: # if file is not at sibling level so provide absolute path.
    data = f.read()
    if('twinkle' in data):
        print('the word twinkle is in file'); 
    else:
        print('the word twinkle is not in file')
# we can do above functionality through loop but it is not good way bcuz it require more code.