import re

txt="“Sea”, “seashore”, “Seashell”, “nausea”, “inseam”, “sea”, “resea1”, “earth4sea”, “deepSea”, “Sea2Sea”, “seas”"
res=re.findall('sea',txt)
print(res)