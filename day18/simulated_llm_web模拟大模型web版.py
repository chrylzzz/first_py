# -*- coding: utf-8 -*-
import argparse
import random
import time
import json
import sys

'''
模拟LLM，提供web api
'''
try:
    # Python 3.x
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    # Python 2.x
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# ==================== 模拟大模型核心逻辑（复用） ====================
REPLY_TEMPLATES = {
    "general": [
        "这个问题很有意义！{topic} 通常涉及 {aspect1} 和 {aspect2} 两个核心方面。在实际应用中，建议先关注 {suggestion}，再逐步深入。",
        "关于 {topic}，我的理解是：{definition}。它的主要优势在于 {advantage}，但也需要注意 {caution} 等潜在问题。",
        "感谢提问！{topic} 是一个热门话题，目前常见的解决方案包括 {solution1}、{solution2} 和 {solution3}。其中，{recommend} 可能更适合你的需求。"
    ],
    "tech": [
        "{topic} 技术的底层原理基于 {principle}，它通过 {mechanism} 实现核心功能。在 Python 中，可以使用 {library} 库快速实现相关需求。",
        "关于 {topic} 的实现，建议分三步：1. {step1}；2. {step2}；3. {step3}。需要注意的是，{pitfall} 是常见坑点，需提前规避。",
        "{topic} 近年来发展迅速，最新的趋势包括 {trend1} 和 {trend2}。对于开发者而言，掌握 {skill} 技能可以更好地应对相关需求。"
    ],
    "daily": [
        "关于 {topic}，我觉得可以从 {angle} 来看待。日常中，{example} 就是一个典型的应用场景，你可以尝试 {action} 来体验。",
        "这个问题很贴近生活！{topic} 的关键在于 {key}，只要把握好这一点，就能 {result}。如果有具体场景，还可以进一步细化建议。"
    ]
}

# 辅助词汇库
TOPICS = ["大模型", "Python 编程", "数据分析", "机器学习", "日常效率", "技术选型", "项目管理", "学习方法"]
ASPECTS = ["理论基础", "实践应用", "性能优化", "兼容性", "易用性", "扩展性"]
DEFINITIONS = ["一组解决特定问题的方法和工具", "基于数据驱动的智能系统", "通过算法实现自动决策的技术"]
ADVANTAGES = ["提高效率", "降低成本", "简化流程", "提升精度", "增强体验"]
CAUTIONS = ["过度依赖工具", "数据质量问题", "兼容性风险", "学习成本较高"]
SOLUTIONS = ["使用开源工具", "定制化开发", "参考成熟方案"]
RECOMMENDS = ["轻量级工具快速验证", "分步实现逐步迭代", "优先解决核心需求"]
PRINCIPLES = ["神经网络", "统计学习", "分布式计算", "模块化设计"]
MECHANISMS = ["数据训练→模型推理→结果反馈", "请求响应模式", "事件驱动架构"]
LIBRARIES = ["requests", "pandas", "numpy", "transformers", "flask"]
STEPS = ["明确需求边界", "调研相关技术", "设计实现方案", "测试验证效果"]
PITFALLS = ["忽略异常处理", "过度设计", "缺乏兼容性考虑"]
TRENDS = ["智能化", "轻量化", "国产化", "低代码"]
SKILLS = ["问题拆解", "技术选型", "代码调试", "文档编写"]
ANGLES = ["实用性", "效率", "成本", "体验", "长期价值"]
EXAMPLES = ["用 Python 自动化处理表格", "通过数据分析优化决策", "用工具简化重复工作"]
ACTIONS = ["从小项目入手实践", "参考他人经验总结", "加入社区交流学习"]
KEYS = ["明确目标", "抓住核心", "持续优化", "灵活调整"]
RESULTS = ["事半功倍", "快速达成目标", "避免走弯路"]


def get_random_word(word_list):
    return random.choice(word_list)


def generate_simulated_reply(prompt):
    # 分类问题类型
    tech_keywords = ["Python", "编程", "技术", "算法", "模型", "数据", "开发", "工具", "库", "框架"]
    daily_keywords = ["日常", "生活", "效率", "学习", "工作", "沟通", "经验", "技巧"]

    template_type = "general"
    if any(keyword in prompt for keyword in tech_keywords):
        template_type = "tech"
    elif any(keyword in prompt for keyword in daily_keywords):
        template_type = "daily"

    # 填充模板
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
        result=get_random_word(RESULTS)
    )
    return reply


def simulate_thinking_delay(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))


# ==================== POST 请求处理器 ====================
class LLMRequestHandler(BaseHTTPRequestHandler):
    """仅处理 POST 请求的处理器"""

    def _set_response(self, status_code=200):
        """设置响应头（固定 JSON 格式）"""
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")  # 允许跨域
        self.end_headers()

    def do_POST(self):
        """仅处理 POST 请求：接收 JSON 格式的 question，返回模拟回复"""
        # 1. 读取请求体长度和数据
        try:
            content_length = int(self.headers.getheader("Content-Length") if sys.version_info[0] == 2 else self.headers[
                "Content-Length"])
            post_data = self.rfile.read(content_length)
        except (ValueError, TypeError):
            response = {
                "code": 400,
                "message": "无效的请求体长度",
                "data": None
            }
            self._set_response(status_code=400)
            self._send_json_response(response)
            return

        # 2. 解析 JSON 数据
        try:
            # 兼容 Python 2.x/3.x 的编码处理
            if sys.version_info[0] == 3:
                data = json.loads(post_data.decode("utf-8"))
            else:
                data = json.loads(post_data)
        except ValueError:
            response = {
                "code": 400,
                "message": "请求体不是合法的 JSON 格式",
                "data": None
            }
            self._set_response(status_code=400)
            self._send_json_response(response)
            return

        # 3. 验证 question 字段
        if "question" not in data or not str(data["question"]).strip():
            response = {
                "code": 400,
                "message": "JSON 必须包含非空的 question 字段",
                "data": None
            }
            self._set_response(status_code=400)
            self._send_json_response(response)
            return

        # 4. 生成模拟回复
        question = str(data["question"]).strip()
        simulate_thinking_delay()
        reply = generate_simulated_reply(question)

        # 5. 构造成功响应
        response = {
            "code": 200,
            "message": "success",
            "data": {
                "question": question,
                "reply": reply
            }
        }
        self._set_response(status_code=200)
        self._send_json_response(response)

    def _send_json_response(self, response):
        """兼容 Python 2.x/3.x 的 JSON 响应发送"""
        try:
            # Python 3.x：需编码为 bytes
            json_str = json.dumps(response, ensure_ascii=False)
            self.wfile.write(json_str.encode("utf-8"))
        except TypeError:
            # Python 2.x：直接发送字符串
            json_str = json.dumps(response, ensure_ascii=False)
            self.wfile.write(json_str)


# ==================== 服务启动函数 ====================
def run_server(host="0.0.0.0", port=8080):
    """启动仅支持 POST 的 API 服务"""
    server_address = (host, port)
    httpd = HTTPServer(server_address, LLMRequestHandler)
    print("🚀 大模型 API 服务已启动（仅支持 POST 请求）")
    print("📡 服务地址：http://{}:{}".format(host, port))
    print("📋 接口说明：")
    print("  - 请求路径：/api/chat")
    print("  - 请求方式：POST")
    print("  - 请求头：Content-Type: application/json")
    print("  - 请求体：{\"question\":\"你的问题\"}")
    print("🔌 输入 Ctrl+C 停止服务")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
        print("\n🛑 服务已停止")


# ==================== 主函数（参数解析） ====================
def main():
    parser = argparse.ArgumentParser(description="模拟大模型 API 服务（仅支持 POST 请求）")
    parser.add_argument("--host", "-H", type=str, default="0.0.0.0", help="服务绑定地址（默认 0.0.0.0）")
    parser.add_argument("--port", "-P", type=int, default=8080, help="服务端口（默认 8080）")
    args = parser.parse_args()

    run_server(host=args.host, port=args.port)


if __name__ == "__main__":
    main()

'''
第一步：启动服务
# 默认配置（0.0.0.0:8080）
python simulated_llm_post_only.py

# 自定义端口（如 8000）
python simulated_llm_post_only.py --port 8000

# 绑定本地地址（仅本机可访问）
python simulated_llm_post_only.py --host 127.0.0.1 --port 8081

------------------------------------------------------------------
方式 1：命令行 curl
curl -X POST http://localhost:8080/api/chat \
  -H "Content-Type: application/json" \
  -d '{"question":"Python 如何处理 JSON 数据？"}'
------------------------------------------------------------------
import requests

# 接口地址
url = "http://localhost:8080/api/chat"
# 请求数据
data = {"question": "如何提高数据分析效率？"}
# 发送 POST 请求
response = requests.post(url, json=data)
# 打印结果
print("响应状态码：", response.status_code)
print("响应内容：", response.json())
'''
