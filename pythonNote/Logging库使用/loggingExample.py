import logging
import sys
# 创建日志器logger并将其日志级别设置为DEBUG
logger = logging.getLogger("Logger")
logger.setLevel(logging.INFO)
# 创建一个流处理器handler并将其日志级别设置为INFO
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
# 创建一个格式化器formatter并将其添加到处理器handler中
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
# 为日志器logger添加上面创建好的处理器handler
logger.addHandler(handler)
# 将日志打印在控制台
logger.info('打印日志级别：info')