'''
本脚本用于将rule.txt中记录的规则转换为Goldendict的Hunspell的MAP规则
转换完成后将save.txt文件中的内容添加到Hunspell文件的即可：
注意，如果此前没有MAP规则，直接复制到Hunspell文件即可；
如果已经添加过MAP规则，请将新规则添加到旧规则末尾，并修改MAP的数量（即MAP规则第一行的数字）
'''
import re

with open("rule.txt", "r", encoding="utf-8")as InputFile, open("save.txt", "w+", encoding="utf-8")as OutputFile:
    RuleText = InputFile.read()
    # 第一个分组是简体，第二个分组是日语
    Reg = re.compile(r"(?P<Hanzi>\w{1})\t(?P<Kanji>\w{1})")
    OutputFileTexts = []
    for iter in Reg.finditer(RuleText):
        OutputFileTexts.append("MAP\t"+iter.group("Kanji") +
                               iter.group("Hanzi")+"\n")
    OutputFile.write("MAP\t"+str(len(OutputFileTexts))+"\n")
    OutputFile.writelines(OutputFileTexts)
