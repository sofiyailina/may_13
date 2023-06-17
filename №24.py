with open('zadanie24_1.txt') as f:
    text = f.readline()
text = text.replace('B', '_')
text = text.replace('C', '_')
text=text.split('_')
print(text)
print(len(max(text, key=len)))
