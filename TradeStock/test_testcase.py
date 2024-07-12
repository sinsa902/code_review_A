from unittest import TestCase


class TradeTestClass(TestCase):
    def setUp(self):
        super().setUp()

    def test_case1_Customer(self):
        customer = Customer("jack")
        name = customer.get_name()
        customer.add_initial_stock_list("[('삼성전자',10주,1500)")
        self.assertEqual(customer.get_stock_list, ["[('삼성전자',10주,1500)"])
        functions = customer.get_function_list()

        self.assertEqual(name, "jack")
        self.assertEqual(stock_list, ["삼성전자", "현대자동차", "SK텔레콤"])
        self.assertEqual(
            functions, ['예약매수("삼성전자",1000)', '예약매수("lg전자",500)', '예약매도("현대자동차",10)']
        )

    def test_case2_Stock(self):
        stock = Stock("삼성전자")
        name = stock.get_name()
        stock.add_EA(400)  # 시장에 나온 주식수
        stock.update_price(5000)
        stock.update_price(3000)
        stock.update_price(2000)
        stock.update_price(1000)
        stock.update_price(8000)
        price_list = stock.get_price_list()

        self.assertEqual(name, "삼성전자")
        self.assertEqual(price_list, [5000, 3000, 2000, 1000, 8000])
        self.assertEqual(stock.get_EA(), 400)

    def test_case3_functions(self):
        function = FunctionsPlan()
        customer1 = Customer("jack")
        customer2 = Customer("bro")
        customer1.add_initial_stock_list("[('삼성전자',10주,1500)")
        customer2.add_initial_stock_list("[('LG전자',5주,2000)")
        self.assertEqual(customer1.get_stock_list, ["[('삼성전자',10주,1500)"])
        self.assertEqual(customer2.get_stock_list, ["[('LG전자',5주,2000)"])
        stock_samsung = Stock("삼성전자")
        stock_samsung.set_EA(10)
        stock_samsung.update_price(5000)
        stock_samsung.update_price(3000)
        stock_samsung.update_price(2000)
        stock_samsung.update_price(1000)
        stock_samsung.update_price(500)
        stock_lg = Stock("LG전자")
        stock_lg.set_EA(5)
        stock_lg.update_price(5000)
        stock_lg.update_price(3000)
        stock_lg.update_price(2000)
        stock_lg.update_price(1000)
        stock_lg.update_price(8000)

        function.set_buyplan(customer1, stock_samsung, 1000)
        function.set_sellplan(customer2, stock_lg, 10)

        self.assertEqual(customer1.get_function_list, ["예약매수('삼성전자',1000)"])
        self.assertEqual(customer2.get_function_list, ["예약매도('LG전자',10)"])

        stock_samsung.update_price(700)
        stock_samsung.update_price(800)
        stock_samsung.update_price(1100)
        stock_lg.update_price(7000)
        stock_lg.update_price(6000)
        stock_lg.update_price(5000)
        self.assertEqual(customer1.get_stock_list, ["('삼성전자',??, ?? 계산필요)"])
        self.assertEqual(customer2.get_stock_list, [None])

    def test_case4_makeinterface(self):
        interface = InterfaceAPP()
        interface.add_customer()
        interface.get_customers()
        interface.login()
        interface.get_login_id()
        interface.buy(stock, ea, price)
        interface.sell(stock, ea, price)
        interface.get_price(stock)
        interface.get_revenue(customer)

    def test_case4_makeKIUM(self):
        app = KiumApp()
        self.assertIsInstance(app, InterfaceAPP)

        customer1 = Customer("jack")
        customer1.add_initial_stock_list("[('삼성전자',10주,1500)")
        app.add_customer(customer1, "pw1")
        self.assertEqual(app.get_customers(), ["jack"])

        rst = app.login(customer1.get_name(), "pw1")
        self.assertEqual(True, rst)
        app.login(customer1.get_name(), "pw2")
        self.assertEqual(False, rst)

        rst = app.get_login_id()
        self.assertEqual("jack", rst)

        app.buy(stock, ea, price)
        app.sell(stock, ea, price)
        app.get_price(stock)
        app.get_revenue(customer)

    def test_case5_makeNamu(self):
        pass
