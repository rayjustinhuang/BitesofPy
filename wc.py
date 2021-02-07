def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        text = f.read()
        filename = f.name
        lines = len(text.splitlines())
        words = len(text.replace('\n', ' ').strip().split(' '))
        chars = len(text)
        
    #print(lines, words, chars)
        
    return f'{lines}\t{words}\t{chars}\t{filename}'
    pass


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))