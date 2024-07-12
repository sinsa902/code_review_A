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

    def test_case2_Stock(self):
        stock = Stock("삼성전자")
        name = stock.get_name()
        stock.update_price(5000)
        stock.update_price(3000)
        stock.update_price(2000)
        stock.update_price(1000)
        stock.update_price(8000)
        price_list = stock.get_price_list()


        self.assertEqual(name, "삼성전자")
        self.assertEqual(price_list, [5000,3000,2000,1000,8000])
        )
