import re

str_input = input('Введите строку:\n')
src = re.compile("Uncle Styopa", re.IGNORECASE)
str_replaced = src.sub("Yan", str_input)
src = re.compile("Uncle", re.IGNORECASE)
str_replaced =src.sub("Yan", str_replaced)
src = re.compile("Styopa", re.IGNORECASE)
str_replaced =src.sub("Yan", str_replaced)

print(str_replaced)

