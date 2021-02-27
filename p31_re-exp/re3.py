import re

#p = re.compile( "a[0-9]+")
p = r"rt[0-9]+"

result = p.findall("life is too short1234..")

print(result, "size", len(result))
