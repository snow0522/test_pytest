import json
import os
import config
def read_json(filename):
    with open(config.base_path + os.sep + 'data' + os.sep + filename,encoding='utf-8') as f:
        data = []
        result = json.load(f)
        for i in result.values():
            data.append(tuple(i.values()))
            return data





if __name__ == '__main__':
    read_json("add_emp.json")
