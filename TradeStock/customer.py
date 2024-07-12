class Customer:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return "jack"

    def get_stock_list(self):
        return ["삼성전자", "현대자동차", "SK텔레콤"]

    def get_function_list(self):
        return [
            '예약매수("삼성전자",1000)',
            '예약매수("lg전자",500)',
            '예약매도("현대자동차",10)',
        ]
