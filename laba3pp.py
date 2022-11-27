import re

with open('zzz.txt', 'r') as f:
    data = f.read()
pattern = r".*z.{3}z[^\n]*"
result = re.findall(pattern, data)
print(result)
