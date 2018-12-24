import random
 
 
class Prompt(object):  # 提示信息显示
    colour_dic = {
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'purple_red': 35,
        'bluish_blue': 36,
        'white': 37,
    }
 
    def __init__(self):
        pass
 
    @staticmethod
    def display(msg, colour='white'):
        choice = Prompt.colour_dic.get(colour)
        # print(choice)
        if choice:
            info = "\033[1;{};1m{}\033[0m".format(choice, msg)
            return info
        else:
            return False
 
    def interlacing_color(msg):  # 随机换色
        colour_list = []
        for i in Prompt.colour_dic:
            colour_list.append(i)
 
        length = len(colour_list) - 1  # 最大索引值
        index = random.randint(0, length)  # 随机数
 
        ret = Prompt.display(msg, colour_list[index])  # 随机颜色
        return ret
 
 
if __name__ == '__main__':
    # pass
    ret = Prompt.interlacing_color('cccffff')
    print(ret)
