import yaml

""" 配置文件环境 """
YAML_PROV = "prov"
YAML_DEV = "dev"
YAML_READER = None


def init(environment):
    global YAML_READER
    path = '/Users/caizhuohan/PycharmProjects/GamerHelper/config/' + 'config-' + environment + '.yaml'
    f = open(path, 'r')
    data = f.read()
    YAML_READER = yaml.safe_load(data)
    return YAML_READER


if __name__ == "__main__":
    init(YAML_DEV)
