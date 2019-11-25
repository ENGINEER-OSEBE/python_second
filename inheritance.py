from datetime import datetime


class Date(object):
    def get_date(self):
        return "2018-02-02"


class Time(Date):
    def get_time(self):
        return "09:00:00"


dt = Date()
print("get date from the date class:" , dt.get_date())

tm = Time()
print("get time from the time class:", tm.get_time())
print("get gate from time class by inheriting from the date class:", tm.get_date())

