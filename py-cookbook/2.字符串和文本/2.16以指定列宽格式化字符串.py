import textwrap

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

#1代表宽带，换行符也算
print(textwrap.fill(s, 10))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))

print(textwrap.fill(s, 40, subsequent_indent='    '))