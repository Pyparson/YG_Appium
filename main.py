import time
import os
import yaml

base_path = os.path.dirname(__file__)
p = os.path.abspath(os.path.join(base_path, "config.yaml"))
with open(p, 'r')as f:
    data = yaml.safe_load(f)
test_list = data["TestList"]

if __name__ == '__main__':
    # base_path = os.path.dirname(__file__)
    # test_list = ['test_room.py']
    string = ""
    # if len(test_list):
    if isinstance(test_list, list):     # 判断是否为列表
        for i in test_list:
            file = os.path.abspath(os.path.join(base_path, "Case", str(i)))
            string += str(file) + " "
    else:
        file_path = os.path.abspath(os.path.join(base_path, "Case"))
        string += str(file_path) + " "
    command = "pytest %s --alluredir " % string
    # 本地执行,报告按时间戳生成
    # report = time.strftime('%Y-%m-%d_%H:%M')
    # xml_path = os.path.abspath(os.path.join(base_path, "Report", str(report), "xml"))
    # report_path = os.path.abspath(os.path.join(base_path, "Report", str(report), "html"))
    # print(command + xml_path)
    # os.system(command + xml_path)
    # os.system('allure generate ' + xml_path + ' -o ' + report_path)
    # 集成到Jenkins,报告固定在同一目录下,可查看历史记录
    # Jenkins服务参数化时使用
    phone = os.environ["phone"] + "_report"
    demo_report = os.path.abspath(os.path.join(base_path, "Report", phone))
    os.system(command + demo_report)
