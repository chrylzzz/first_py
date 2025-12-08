"""
pip3 install pyecharts
Mac安装pyecharts时，会让你使用brew进行安装，但是brew没有pyecharts
这个错误是 Mac 系统（尤其是 Sonoma 及以上版本）的 Python 环境保护机制：系统预装的 Python 或通过brew install python安装的 Python，会禁止直接用pip3 install安装全局包，强制要求通过brew安装软件（但pyecharts是 Python 第三方库，brew没有对应的包）。
解决步骤：
# 1. 进入你的项目目录（替换为chryl的实际项目路径，示例如下）
cd /Users/chryl/llm-project  # 建议用项目根目录，方便管理虚拟环境

# 2. 创建虚拟环境（path/to/venv 替换为自定义路径，如 ./venv，即项目内创建venv文件夹）
python3 -m venv ./venv  # 项目内创建虚拟环境，无需记复杂路径

# 3. 激活虚拟环境（Mac默认bash/zsh终端，直接执行）
source ./venv/bin/activate

# 4. 安装pyecharts（用国内镜像源，避免下载超时）
python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts

# 5. 验证安装（可选，确保无报错）
python3 -c "import pyecharts; print('安装成功，版本：', pyecharts.__version__)"

二、关键说明
激活成功标识：终端提示符前会显示 (venv)，此时所有 python3 和 pip3 命令都指向虚拟环境，不会触发系统限制。
后续操作：
安装其他依赖（如 pandas、requests 等）：直接执行 python3 -m pip install 包名 即可。
退出虚拟环境：执行 deactivate（退出后 (venv) 消失，恢复系统 Python 环境）。
虚拟环境复用：下次开发时，只需进入项目目录，重新执行 source ./venv/bin/activate 即可激活，无需重复创建。
"""
# 使用pycharm直接导入
import pyecharts
print(pyecharts.__version__)  # 输出版本号