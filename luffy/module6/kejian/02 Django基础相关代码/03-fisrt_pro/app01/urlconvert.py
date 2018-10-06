


class MonConvert:

    regex="[0-9]{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value): # 反向解析
        return '%04d' % value