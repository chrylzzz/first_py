"""
date 12/4/25
@author chryl

"""
# 测试数据不会备份，正式数据会备份
# 将文件里的内容按照时间进行排序

def read_file_to_nested_list(file_path, encoding="utf-8", skip_empty_line=True, strip_whitespace=True):
    """
    读取文件内容，每行用逗号分隔为子列表，汇总为嵌套列表
    :param file_path: 文件路径（相对路径/绝对路径）
    :param encoding: 文件编码（默认 utf-8，需根据文件调整）
    :param skip_empty_line: 是否跳过空行（True=跳过，False=保留空列表）
    :param strip_whitespace: 是否去除每个元素的首尾空白（True=去除，False=保留原始格式）
    :return: 嵌套列表（每行一个子列表，汇总为总列表）
    """
    nested_list = []
    try:
        # 打开文件并逐行读取（with 语句自动关闭文件，安全高效）
        with open(file_path, "r", encoding=encoding) as f:
            for line in f:
                # 去除行尾的换行符（\n/\r\n）
                line = line.rstrip("\n\r")
                # print(line)
                # 跳过空行（可选）
                if skip_empty_line and not line:
                    continue

                # 用逗号分隔行内容
                if strip_whitespace:
                    # 去除每个元素的首尾空白（如空格、制表符）
                    sub_list = [item.strip() for item in line.split(",")]
                else:
                    # 保留原始格式（不去除空白）
                    sub_list = line.split(",")

                # 将子列表添加到总列表
                nested_list.append(sub_list)
        return nested_list
    except FileNotFoundError:
        print(f"错误：找不到文件 {file_path}，请检查路径是否正确")
        return []
    except Exception as e:
        print(f"读取文件失败：{str(e)}")
        return []


if __name__ == '__main__':
    file_path = "bb/2025/test-file.txt"
    # 读取文件（传入文件路径，其他参数默认即可）
    result = read_file_to_nested_list(file_path)
    # 打印结果（每行一个子列表，汇总为总列表）
    print("最终嵌套列表：")
    for idx, sub_list in enumerate(result, 1):
        print(f"第{idx}行\t：{sub_list}")
