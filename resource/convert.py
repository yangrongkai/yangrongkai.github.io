# coding=UTF-8

import time


def convert(path):
    content = ""
    with open(path, 'rb') as f:
        content = f.read()
    content = content.decode("gbk")

    with open(path + "_" + str(time.time()), 'w') as f:
        f.write(content)


if __name__ == "__main__":
    convert("myself.html")
