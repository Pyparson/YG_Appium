import logging
import os
import time
import yaml

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


class Log:
    date = '%Y-%m-%d %H:%M:%S'
    base_path = os.path.dirname(__file__)
    path = os.path.abspath(os.path.join(base_path, "..", "config.yaml"))
    log_file = os.path.abspath(os.path.join(base_path, "..", "Logs", "log.log"))
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    if "Level" not in data.keys():
        level = "info"
    else:
        level = data["Level"]
    logging.basicConfig(level=LEVELS[level])    # 指定要输出的文件以及log的输出形式、包括时间格式、日志级别等等
    handler = logging.FileHandler(log_file, encoding='utf-8')

    @classmethod
    def get_current_time(self):
        return time.strftime(self.date, time.localtime(time.time()))

    @classmethod
    def logger(self, meg):
        lv = self.level
        logging.getLogger().addHandler(self.handler)
        if lv == "debug":
            logging.debug("[DEBUG " + self.get_current_time() + "]" + meg)
        elif lv == "warn":
            logging.warning("[WARNING " + self.get_current_time() + "]" + meg)
        elif lv == "error":
            logging.error("[ERROR " + self.get_current_time() + "]" + meg)
        elif lv == "critical":
            logging.critical("[CRITICAL " + self.get_current_time() + "]" + meg)
        elif lv == "info":
            logging.info("[INFO " + self.get_current_time() + "]" + meg)
        else:
            raise ("Level is error...Please Try Again!!!")
