x = '10465136163'
for i in range(len(x)):
    x = x.replace('0', '0', 1)
    x = x.replace('1', '1', 1)
    x = x.replace('2', '2', 1)
    x = x.replace('3', '10', 1)
    x = x.replace('4', '11', 1)
    x = x.replace('5', '12', 1)
    x = x.replace('6', '20', 1)
    x = x.replace('7', '21', 1)
    x = x.replace('8', '22', 1)
    x = x.replace('9', '100', 1)
    x = x.replace('10', '101', 1)
print(x)