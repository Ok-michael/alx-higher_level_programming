#!/usr/bin/python3
if __name__ == "__main__":
    '''print all names defined by hidden_4 module.'''
    import hidden_4
    for item in dir(hidden_4):
        if item[0] != '_' and item[1] != '_':
            print(item)
