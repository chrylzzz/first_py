"""
date 2025/12/9
@author chryl

"""
import logging

# 配置 logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')
logger = logging.getLogger()

logger.debug(f"Executing SQL: 你好,我是陈冠希")
