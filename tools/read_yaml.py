import yaml
import config
import os

def read_yaml(file_name):
    with open(config.base_path + os.sep +'data' + os.sep + file_name,encoding='utf-8') as f:
        data = []
        result = yaml.safe_load(f)
        for i in result.values():
            data.append(tuple(i.values()))
            return data

if __name__ == '__main__':
    read_yaml('login.yaml')


