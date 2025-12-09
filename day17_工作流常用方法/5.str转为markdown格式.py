# -*- coding: utf-8 -*-

def str_to_markdown_basic(text, style="normal"):
    """
    普通字符串转Markdown基础格式
    :param text: 输入字符串
    :param style: 格式化样式（normal/title1-title6/bold/italic/list/item）
    :return: Markdown格式字符串
    """
    if style == "normal":
        return text  # 无格式
    elif style.startswith("title"):
        level = int(style.replace("title", ""))
        level = max(1, min(6, level))  # 限制标题级别1-6
        return f"{'#' * level} {text}"
    elif style == "bold":
        return f"**{text}**"
    elif style == "italic":
        return f"*{text}*"
    elif style == "list":
        # 按换行符分割为列表项
        items = text.split("\n")
        return "\n".join([f"- {item.strip()}" for item in items if item.strip()])
    elif style == "item":
        return f"- {text}"
    else:
        return text


# ---------------------- 使用示例 ----------------------
if __name__ == "__main__":
    raw_str = "您好！我是大瓦特，很高兴为您介绍用电业务办理相关内容。\n\n用电业务办理涵盖客户与供电企业建立、变更及终止供用电关系的全过程，旨在提供高效、便捷的服务。主要业务类型和办理渠道如下：\n\n### 一、主要业务类型\n1.  **新装增容**：包括低压居民/非居民新装、高压新装等，满足客户首次用电或增加用电容量的需求。\n2.  **变更用电**：涉及日常用电信息的变更，常见类型包括：\n    *   **更名过户**：用电地址、容量、性质不变，仅改变用电户名称。买卖房屋或企业名称变更时需办理。\n    *   **改类**：因用电用途改变（如住宅改为商铺）或其他原因需变更电价类别。\n    *   **移表**：因房屋修缮等原因，申请迁移电能表安装位置。\n    *   **暂拆与暂拆恢复**：因房屋修缮等需暂时停止用电并拆表，原因消除后申请恢复。\n    *   **减容**：包括**永久减容**（减少合同约定容量且不再恢复）和**临时性减容**（高压客户申请在特定期限内减少容量）。\n    *   **减容恢复**：在减容期限内申请恢复原容量。\n    *   **受电装置变更**：在产权分界点、合同容量等不变情况下，进行受电装置或配电房改造。\n3.  **临时用电**：为建筑施工、市政建设等临时性用电需求提供供电服务，并可办理**临时用电延期**。\n4.  **增值服务**：包括节能服务、设备代维等，满足客户多样化需求。\n5.  **“一件事”服务**：整合跨部门流程，将关联事项合并办理，实现“一次申请、并联办理”，提升效率。\n\n### 二、办理渠道\n您可以通过以下线上渠道便捷办理多数业务：\n*   **微信小程序**\n*   **支付宝小程序**\n*   **网上营业厅（网厅）**\n*   **掌上营业厅（掌厅）**\n\n### 三、通用注意事项\n1.  办理业务时，请确保提供的信息真实、准确。\n2.  部分业务（如更名过户）需结清以往电费。\n3.  业务办理时限通常较短，具体可咨询当地营业厅或查看服务指南。\n4.  对于临时用电等业务，请遵守约定的用电期限，需延期请及时申请。\n\n如果您有具体的业务办理需求或对上述任何一项业务想了解更多详细信息，欢迎随时提出，我将为您提供更精准的指导。"
    # raw_str = "Python字符串转Markdown\n基础样式演示\n支持标题、加粗、列表"

    # 转换为不同样式
    print("标题1：", str_to_markdown_basic("Python字符串转Markdown", "title1"))
    print("加粗：", str_to_markdown_basic("重点内容", "bold"))
    print("斜体：", str_to_markdown_basic("辅助说明", "italic"))
    print("列表：\n", str_to_markdown_basic(raw_str, "list"))