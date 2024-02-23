"""基于正则提取转换关系"""

import re

RULE_DICT_J2C = {}

# 第一个分组是简体汉字，第二个分组是日文漢字
REG = re.compile(r"(?P<hanzi>\w{1})\t(?P<kanji>\w{1})")

# 加载转换规则
with open("rule.txt", "r", encoding="utf-8") as File:
    RULE_TEXT = File.read()
    for iter_ in REG.finditer(RULE_TEXT):
        # 漢字到汉字的转换规则是一一对应
        RULE_DICT_J2C[iter_.group("kanji")] = iter_.group("hanzi")


def convert_j2c(input_text: str) -> str:
    """将日文漢字转为简体汉字

    Args:
        input_text (_str_): 输入的字符串

    Returns:
        _str_: 转换后的汉字
    """
    output_text_list = []
    for item in input_text:
        output_text_list.append(RULE_DICT_J2C.get(item, item))
    output_text = "".join(output_text_list)
    return output_text


print(convert_j2c("葛飾北斎"))
