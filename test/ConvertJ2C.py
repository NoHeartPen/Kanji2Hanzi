import re


# 加载转换规则
with open("rule.txt", "r", encoding="utf-8") as File:
    RuleText = File.read()
    # 第一个分组是简体，第二个分组是日语
    Reg = re.compile(r"(?P<Hanzi>\w{1})\t(?P<Kanji>\w{1})")
    global J2CRuleDict
    J2CRuleDict = {}
    for iter in Reg.finditer(RuleText):
        J2CRuleDict[iter.group("Kanji")] = iter.group(
            "Hanzi")  # 漢字到汉字的转换规则是一一对应


def ConvertJ2C(InputText):  # 漢字转汉字
    OutputTextList = []  # 储存
    for item in InputText:
        OutputTextList.append(J2CRuleDict.get(item, item))
    OutputText = "".join(OutputTextList)
    return OutputText


print(ConvertJ2C("葛飾北斎"))
