import re
import os
import sys
import tkinter.filedialog


def GetProcessFiles():
    global FileName
    FileName = tkinter.filedialog.askopenfilename(
        filetypes=[("txt", ".txt")])
    if len(FileName) != 0:
        return FileName
    else:
        sys.exit()


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
    OutputTextList = []  # 储存转换结果
    for item in InputText:
        OutputTextList.append(J2CRuleDict.get(item, item))
    OutputText = "".join(OutputTextList)
    return OutputText


def ProcessFile(FileNames):
    with open(FileNames, "r", encoding="utf-8") as InputFile, open("save.txt", "w", encoding="utf-8")as OutputFile:
        InputFileTextList = InputFile.readlines()
        InputFileTextSet = set()
        for line in InputFileTextList:
            if "【"not in line:  # 删除无实际意义的词条
                InputFileTextSet.add(line)
        OutputFileTextSet = set()
        for InputFileTextLine in InputFileTextSet:
            InputFileTextLine = InputFileTextLine.replace("\n", "")
            OutputFileTextLine = ConvertJ2C(InputFileTextLine)
            if OutputFileTextLine != InputFileTextLine:
                OutputFileTextLine = OutputFileTextLine+'\n<section class="description"><a href="entry://' + \
                    InputFileTextLine+'#description">'+InputFileTextLine+'</a></section>\n</>\n'
                OutputFileTextSet.add(OutputFileTextLine)
        OutputFile.writelines(sorted(OutputFileTextSet))
        print("处理完成")


FileName = GetProcessFiles()
ProcessFile(FileName)
