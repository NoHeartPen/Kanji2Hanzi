'''
删除rule.txt文件中Unicode码一样的汉字，并按照一定的规律排序
'''

import re
with open("temp.txt", encoding="UTF-8") as InputFile, open("save.txt", "w", encoding="utf-8")as OutputFile:
    OutputTextGroup = set()
    Reg = re.compile(r"(\w*)\t(\w*)")
    for iter in Reg.finditer(InputFile.read()):
        print(iter.group(1))
        if iter.group(1) != iter.group(2):  # 判断Unicode码是否一致
            OutputTextGroup.add(iter.group(0)+'\n')
    OutputFile.writelines(sorted(OutputTextGroup))
