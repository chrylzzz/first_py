# -*- coding: utf-8 -*-
import argparse
import random
import time
import sys
'''
模拟LLM，本地执行
'''

# ==================== 模拟回复配置 ====================
# 模拟不同类型的回复模板（可根据需求扩展）
REPLY_TEMPLATES = {
    "general": [
        "这个问题很有意义！{topic} 通常涉及 {aspect1} 和 {aspect2} 两个核心方面。在实际应用中，建议先关注 {suggestion}，再逐步深入。",
        "关于 {topic}，我的理解是：{definition}。它的主要优势在于 {advantage}，但也需要注意 {caution} 等潜在问题。",
        "感谢提问！{topic} 是一个热门话题，目前常见的解决方案包括 {solution1}、{solution2} 和 {solution3}。其中，{recommend} 可能更适合你的需求。",
        "简单来说，{topic} 的核心逻辑是 {logic}。如果需要进一步了解，可以从 {resource} 入手，逐步积累相关知识。"
    ],
    "tech": [
        "{topic} 技术的底层原理基于 {principle}，它通过 {mechanism} 实现核心功能。在 Python 中，可以使用 {library} 库快速实现相关需求。",
        "关于 {topic} 的实现，建议分三步：1. {step1}；2. {step2}；3. {step3}。需要注意的是，{pitfall} 是常见坑点，需提前规避。",
        "{topic} 近年来发展迅速，最新的趋势包括 {trend1} 和 {trend2}。对于开发者而言，掌握 {skill} 技能可以更好地应对相关需求。"
    ],
    "daily": [
        "关于 {topic}，我觉得可以从 {angle} 来看待。日常中，{example} 就是一个典型的应用场景，你可以尝试 {action} 来体验。",
        "这个问题很贴近生活！{topic} 的关键在于 {key}，只要把握好这一点，就能 {result}。如果有具体场景，还可以进一步细化建议。",
        "对于 {topic}，我的建议是 {suggestion}。另外，{tip} 这个小技巧可能会帮到你，不妨尝试一下～"
    ]
}

# 辅助词汇库（用于填充回复模板，增加随机性和合理性）
TOPICS = ["大模型", "Python 编程", "数据分析", "机器学习", "日常效率", "技术选型", "项目管理", "学习方法"]
ASPECTS = ["理论基础", "实践应用", "性能优化", "兼容性", "易用性", "扩展性", "安全性", "可维护性"]
DEFINITIONS = ["一组解决特定问题的方法和工具", "基于数据驱动的智能系统", "通过算法实现自动决策的技术", "人与人之间高效沟通的方式"]
ADVANTAGES = ["提高效率", "降低成本", "简化流程", "提升精度", "增强体验"]
CAUTIONS = ["过度依赖工具", "数据质量问题", "兼容性风险", "学习成本较高"]
SOLUTIONS = ["使用开源工具", "定制化开发", "外包给专业团队", "参考成熟方案"]
RECOMMENDS = ["轻量级工具快速验证", "分步实现逐步迭代", "优先解决核心需求"]
LOGICS = ["分解问题→分析关键→落地执行", "数据输入→处理→输出结果", "需求调研→方案设计→测试优化"]
RESOURCES = ["官方文档", "入门教程", "实战项目", "行业报告", "技术社区"]
PRINCIPLES = ["神经网络", "统计学习", "分布式计算", "模块化设计"]
MECHANISMS = ["数据训练→模型推理→结果反馈", "请求响应模式", "事件驱动架构"]
LIBRARIES = ["requests", "pandas", "numpy", "transformers", "flask"]
STEPS = ["明确需求和边界", "调研相关技术", "设计实现方案", "测试验证效果", "上线迭代优化"]
PITFALLS = ["忽略异常处理", "过度设计", "缺乏兼容性考虑", "性能瓶颈未预判"]
TRENDS = ["智能化", "轻量化", "国产化", "低代码", "跨平台"]
SKILLS = ["问题拆解", "技术选型", "代码调试", "文档编写", "沟通协作"]
ANGLES = ["实用性", "效率", "成本", "体验", "长期价值"]
EXAMPLES = ["用 Python 自动化处理表格", "通过数据分析优化决策", "用工具简化重复工作"]
ACTIONS = ["从小项目入手实践", "参考他人经验总结", "加入社区交流学习"]
KEYS = ["明确目标", "抓住核心", "持续优化", "灵活调整"]
RESULTS = ["事半功倍", "快速达成目标", "避免走弯路"]
TIPS = ["善用搜索工具", "建立知识体系", "定期复盘总结", "关注行业动态"]


# ==================== 模拟工具函数 ====================
def get_random_word(word_list):
    """从列表中随机选择一个词汇"""
    return random.choice(word_list)


def generate_simulated_reply(prompt):
    """根据输入生成模拟回复"""
    # 简单分类：判断输入是否偏向技术/日常/通用
    tech_keywords = ["Python", "编程", "技术", "算法", "模型", "数据", "开发", "工具", "库", "框架"]
    daily_keywords = ["日常", "生活", "效率", "学习", "工作", "沟通", "经验", "技巧"]

    # 选择回复模板类型
    template_type = "general"
    if any(keyword in prompt for keyword in tech_keywords):
        template_type = "tech"
    elif any(keyword in prompt for keyword in daily_keywords):
        template_type = "daily"

    # 随机选择模板并填充词汇
    template = get_random_word(REPLY_TEMPLATES[template_type])
    reply = template.format(
        topic=get_random_word(TOPICS),
        aspect1=get_random_word(ASPECTS),
        aspect2=get_random_word(ASPECTS),
        suggestion=get_random_word(RECOMMENDS),
        definition=get_random_word(DEFINITIONS),
        advantage=get_random_word(ADVANTAGES),
        caution=get_random_word(CAUTIONS),
        solution1=get_random_word(SOLUTIONS),
        solution2=get_random_word(SOLUTIONS),
        solution3=get_random_word(SOLUTIONS),
        recommend=get_random_word(RECOMMENDS),
        logic=get_random_word(LOGICS),
        resource=get_random_word(RESOURCES),
        principle=get_random_word(PRINCIPLES),
        mechanism=get_random_word(MECHANISMS),
        library=get_random_word(LIBRARIES),
        step1=get_random_word(STEPS),
        step2=get_random_word(STEPS),
        step3=get_random_word(STEPS),
        pitfall=get_random_word(PITFALLS),
        trend1=get_random_word(TRENDS),
        trend2=get_random_word(TRENDS),
        skill=get_random_word(SKILLS),
        angle=get_random_word(ANGLES),
        example=get_random_word(EXAMPLES),
        action=get_random_word(ACTIONS),
        key=get_random_word(KEYS),
        result=get_random_word(RESULTS),
        tip=get_random_word(TIPS)
    )
    return reply


def simulate_thinking_delay(min_sec=1, max_sec=3):
    """模拟模型思考延迟（1-3秒）"""
    time.sleep(random.uniform(min_sec, max_sec))


# ==================== 交互式对话 ====================
def interactive_chat():
    """交互式对话模式（无传入 question 时触发）"""
    print("🎯 进入模拟大模型交互式对话（输入 'exit' 退出）")
    print("💡 提示：支持技术、日常、通用类问题，回复为随机生成的合理内容\n")

    while True:
        try:
            # 兼容 Python 2.x/3.x 输入
            try:
                user_input = input("你：")
            except NameError:
                user_input = raw_input("你：")

            # 退出逻辑
            if user_input.strip().lower() == "exit":
                print("👋 对话结束！")
                break
            if not user_input.strip():
                print("⚠️  请输入有效内容！")
                continue

            # 模拟思考+生成回复
            print("🤖 模型思考中...", end="", flush=True)
            simulate_thinking_delay()
            sys.stdout.write("\r" + " " * 20 + "\r")  # 清除思考提示
            reply = generate_simulated_reply(user_input)
            print(f"🤖 模型：{reply}\n")
        except KeyboardInterrupt:
            print("\n👋 对话被中断，已退出！")
            break


# ==================== 主函数（参数解析+入口） ====================
def main():
    # 解析命令行参数（支持传入 question）
    parser = argparse.ArgumentParser(description="模拟大模型调用脚本（无需真实接口）")
    parser.add_argument("--question", "-q", type=str, default=None, help="可选：直接传入的问题（如 --question '什么是大模型'）")
    args = parser.parse_args()

    # 1. 若传入 question，直接生成回复并输出
    if args.question:
        print(f"📝 你的问题：{args.question}")
        print("🤖 模型思考中...", end="", flush=True)
        simulate_thinking_delay()
        sys.stdout.write("\r" + " " * 20 + "\r")
        reply = generate_simulated_reply(args.question)
        print(f"🤖 模型回复：\n{reply}")
    # 2. 未传入 question，进入交互式对话
    else:
        interactive_chat()


if __name__ == "__main__":
    main()

'''
场景 1：命令行传入问题（直接输出结果）
# 基础用法
python simulated_llm.py --question "什么是大模型？"
# 技术类问题
python simulated_llm.py -q "Python 如何实现数据分析？"
# 日常类问题
python simulated_llm.py -q "如何提高工作效率？"

场景 2：交互式对话（无参数运行）
python simulated_llm.py
'''