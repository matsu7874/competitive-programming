import re
N = int(input())
HTML = ' '.join([input() for i in range(N)])
HTML =re.sub('(<!--)[\s\S]*?(-->)', '', HTML)
HTML =re.sub('(</)[\s\S]*?(>)', '', HTML)
HTML =re.sub('(/>)', ' >', HTML)
# print(HTML)

def printf(text, level):
    if level == 0:
        print(t)
    elif level == 1:
        print('->',t, end=' ')
    elif level == 2:
        print('>',t, end='\n')


in_tag = False
is_tag_name = False
in_quote = False
t = ''

for c in HTML:
    if c == '<':
        t = ''
        in_tag = True
        is_tag_name = True
    elif c == '>':
        if t != '':
            if is_tag_name:
                printf(t,0)
            else:
                printf(t,1)
            t = ''
        in_tag = False

    if c == '=' or c == ' ':
        if t != '':
            if in_quote:
                printf(t,2)
            elif in_tag:
                if not is_tag_name:
                    printf(t,1)
                else:
                    printf(t,0)
                    is_tag_name = False
            t = ''
    elif c == '"':
        if t != '':
            if in_quote:
                printf(t,2)
            elif in_tag:
                if not is_tag_name:
                    printf(t,1)
                else:
                    printf(t,0)
                    is_tag_name = False
            t = ''
        in_quote = not in_quote

    if c not in '<>"= ':
        t += c
