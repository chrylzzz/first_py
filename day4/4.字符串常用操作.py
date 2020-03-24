"""
查找:
    .find(子串,开始位置下标,结束为止下标):某个子串是否包含在字符串中,包含就返回下标,否则返回-1
    .index(子串,开始位置下标,结束为止下标):检测某个子串是否包含在这个字符串中,在就返回下标,否则报异常
    .rfind();.rindex() 从右侧开始找
    .count(子串,开始位置下标,结束为止下标)返回某个字符串在字符中出现的自出
注意:开始/结束位置下标可以省
"""

str1 = 'ooomxanuzzz'
print(str1.find('a', 0))
print(str1.find('as', 0))
print('--------')
# print(str1.index('c'))
print('--------')
print(str1.count('z'))

"""
修改:
    .replace(旧子串,新子串,替换次数):替换
    注意:替换册数如果查出淄川出现次数,则替换为该替换的次数
        数据可以修改为可变类型 和 不可变类型,是否改变原有的字符串
    .split(分个字符,num)
    注意:num为分个字符串的次数,即将来返回num+1个
        如果分割字符是原油字符串中的子串,分割后丢失该子串
    .join(多个字符串组成的序列):用一个字符或字串合并字符串,即 将多个字符串合并为一个字符串
    
    
"""
print('===================')

print(str1.replace('o', '1'))

print(str1.split('a'))
print(str1.join(["-aaa-", '-bbb-', '-yyy-']))
print("...".join(["aaa", 'bbb', 'yyy']))

print('===================')
"""
大小写转换:
    .capitalize():将字符串的第一个字符转为大写
    .title():每个单词首字母转为大写
    .upper():转大写
    .lower()转小写
"""
print(str1.capitalize())
print(str1.title())
print(str1.upper().lower())
print(str1.upper())

print('===================')

"""
删除:
    .lstrip():删除字符串左侧空白字符串
    .rstrip():删除字符串R侧空白字符串
    .strip():删除两侧空白
"""
str2 = ' 93ksz 2 omazZ '
print(str2.lstrip())
print(str2.rstrip())
print(str2.strip())

print('===================')

"""
左中右对齐:
    .ljust(长度,填充字符):返回左对齐字符串,并且使用指定字符(默认空格)来填充长度,左边对其,往右填充
    .rjust(长度,填充字符):右,右边对其,从左开始填充
    .center(长度,填充字符):两侧填充,会优先填充左边
"""
str3 = 'miss'
print(str3.ljust(7, ','))
print(str3.ljust(7))
print(str3.rjust(7, '-'))
print(str3.center(7, '-'))
print('===================')

"""
判断:
    .startswith(子串,开始下标,结束下表):以子串开头
    .endswith()
    
    .isalpha():都是字母,如果字符串至少有一个字符并且所有字符都是字母,返回true
    .isdigit():如果包含数字返回true
    .isalnum():数字或字母或组合
    
    .isspace():判断都是空白
"""
str4 = 'aax6gk'
str5 = '2300'
str6 = '2 a'
str7 = '  '
print(str3.startswith('i'))
print(str3.endswith('s'))
print(str4.isalpha())
print(str5.isdigit())
print(str6.isalnum())
print(str7.isspace())

print('===================')
