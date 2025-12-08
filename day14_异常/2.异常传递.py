"""

"""
import time

try:
    f = open('testzzz.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            print(content)
            time.sleep(2)
    except:
        print('中直结束')
    finally:
        f.close()
except Exception as result:
    print(result)
else:
    print('没有异常的代码...')
