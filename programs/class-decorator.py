import datetime

# @staticmethod
# @classmethod
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def show_date(self):
        print('year: {}, month: {}, day: {}'.format(self.year, self.month, self.day))

    @staticmethod
    def today():
        return datetime.datetime.now()

print(Date.today())
d1 = Date(2021, 2, 3)
print(d1.today())
print('end ' * 20)

class MyDate(Date):
    "my class works with my date format"
    @classmethod
    def from_date_string(cls, date_string):
        # year, month, day = date_string.split('-')
        # return cls(year, month, day)
        return cls(*date_string.split('-'))

    @property
    def format_slash(self):
        return f'{self.year}/{self.month}/{self.day}'

    @property
    def format_cn(self):
        return f'{self.year}年{self.month}月{self.day}'

d1 = Date(2021, 8, 28)
d2 = MyDate.from_date_string('2019-9-10')
d1.show_date()
d2.show_date()


# @property
print(MyDate.format_slash)  # 2022/3/4
print(d2.format_slash)  # 2022/3/4
print(MyDate.format_cn)  # 2021年2月3日
print(d2.format_cn)  # 2021年2月3日
