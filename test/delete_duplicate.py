"""
删除rule.txt文件中Unicode码一样的汉字，并按照一定的规律排序
"""

import re

with open("temp.txt", encoding="UTF-8") as input_file, open(
    "save.txt", "w", encoding="utf-8"
) as output_file:
    output_group = set()
    REG = re.compile(r"(\w*)\t(\w*)")
    for iter_ in REG.finditer(input_file.read()):
        # 判断Unicode码是否一致
        if iter_.group(1) != iter_.group(2):
            output_group.add(iter_.group(0) + "\n")
    output_file.writelines(sorted(output_group))
