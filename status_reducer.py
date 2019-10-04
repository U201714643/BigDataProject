import sys

current_word=None
current_count=0
word=None
while True:
    try:
        line=sys.stdin.readline().strip()
        word,count=line.split()
        try:
            count =int(count)
        except ValueError:
                continue
        if(current_word==word):
            current_count+=count
        else:
            if(current_word):
                print('{}   {}'.format(current_word, current_count))
            current_count=count
            current_word=word
    except:
        break

if(current_word==word):
    print('{}   {}'.format(current_word, current_count))

        

