"""
抛出自定义异常的语法为 raise 异常类对象


"""


##长度小于3抛出异常
class SIError(Exception):
    def __init__(self, len, min_len):
        self.len = len
        self.min_len = min_len

    def __str__(self):
        return f'你输入的长度是{self.len},不能少于{self.min_len}'


def main():
    try:
        con = input('输入密码: ')
        if len(con) < 3:
            raise SIError(len(con), 3)

    except Exception as result:
        print(result)
    else:
        print('密码输入完成')


main()
