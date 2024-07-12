from unittest import TestCase


class TradeTestClass(TestCase):
    def setUp(self):
        super().setUp()

    def test_case1_Customer(self):
        customer = Customer("jack")
        name = customer.get_name()
        stock_list = customer.get_stock_list()
        functions = customer.get_function_list()

        self.assertEqual(name, "jack")
        self.assertEqual(stock_list, ["삼성전자", "현대자동차", "SK텔레콤"])
        self.assertEqual(
            functions, ['예약매수("삼성전자",1000)', '예약매수("lg전자",500)', '예약매도("현대자동차",10)']
        )
