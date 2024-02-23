"""
删除rule.txt文件中Unicode码一样的汉字，并按照一定的规律排序
"""

with open("temp.txt", encoding="UTF-8") as input_file, open(
    "save.txt", "w", encoding="utf-8"
) as output_file:
    output_group = set()
    for line in input_file:
        columns = line.strip().split(" ")
        if len(columns) >= 2 and columns[0] != columns[1]:
            output_group.add(line)
        else:
            print(f"{line} 没有空格作为分隔符，请注意检查！")
    output_file.writelines(sorted(output_group))
