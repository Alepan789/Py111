# курс PU200 - 2020год
# Пантелеев А.В.

# @property
# неизменяемый атрибут, для изменения его нужно setter, иначе никак-никак не изменить

# 7



class Date:

    def __init__(self, *args):
        if self.__is_valid_date(*args):
            self.date(*args)
            # self._year = args[0]
            # self._month = args[1]
            # self._day = args[2]
        else:
            raise ValueError('Введена не дата')

        
    def __str__(self):
        pass
        # return f'{self.year}.{self.month}.{self.day}'
    
    def __repr__(self):
        pass
    
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0


    @classmethod
    def get_max_day(cls, year, month):
        DAY_OF_MONTH = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  #
                        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))  #

        return DAY_OF_MONTH[Date.is_leap_year(year)][month - 1]

    @property
    def date(self):
        return self._date

    @classmethod
    def __is_valid_date(cls, *args):
        assert len(args) == 3
        # if len(args) == 3:
        year = int(args[0])
        month = int(args[1])
        day = int(args[2])

        print(f'57 y:{year} m:{month} d:{day} checkk:{cls.get_max_day(year, month)}')

        if not 1 <= month <= 12:
            raise ValueError('месяц должен быть в диапазоне 1-12')
        if not 1 <= day <= cls.get_max_day(year, month):
            raise ValueError('день должен быть в диапазоне дней')
        if not year > 0:
            raise ValueError('год > 0')
        print(f'65 y:{year} m:{month} d:{day}')
        return True

    @date.setter
    def date( *args):
        _year = args[0]
        _month = args[1]
        _day = args[2]
        # self._date = value
        _date = str(_year)+'.'+str(_month)+'.'+str(_day)
        # print(f'75 y:{year} m:{month} d:{day}')
        return _date
        # return f'{_year}.{_month}.{_day}'
        
    @property
    def day(self):
        return self._day
            
    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year

    
    def add_day(self, day):
        pass
    
    def add_month(self, month):
        pass
        
    def add_year(self, year):
        pass
    
    @staticmethod
    def date2_date1(date2, date1):
        pass



    # @staticmethod
    # def __validate_date(*args):
    #     if len(args) == 0:
    #         t = str(datetime.now())[:10].replace('-', ':')
    #         return t.hour, t.minute
    #     try:
    #         if len(args) == 1 and isinstance(args[0], str):
    #             s = args[0].split('.')
    #             if len(s) != 3:
    #                 raise Exception()
    #             year = int(s[0])
    #             month = int(s[1])
    #             day = int(s[2])
    #
    #             if not 1 <= month <= 23:
    #                 raise Exception()
    #             if not 1 <= day <= 31:
    #                 raise Exception()
    #             return year, month, day
            # if len(args) == 2:
            #     h = args[0]
            #     m = args[1]
            #     if not isinstance(h, int):
            #         raise Exception()
            #     if not isinstance(m, int):
            #         raise Exception()
            #
            #     if not 0 <= h <= 23:
            #         raise Exception()
            #     if not 0 <= m <= 59:
            #         raise Exception()
            #
            #     return args[0], args[1]
        # except:
        #     raise TypeError(
        #         'Arguments must be in the next format:  hour - int and minute - int or "HH:MM"')


# assert

# dt1 = Date.date('2015.01.03')
# dt1 = Date()
# dt1.day = 1
# dt1.month = 3
# dt1.year = 2013
#
# print(dt1.day)
# print(dt1.year)
# print(dt1.month)

dt1 = Date(2020, 2, 29)
print(dt1)