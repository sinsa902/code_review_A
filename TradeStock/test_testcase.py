from unittest import TestCase
from customer import Customer
from unittest.mock import Mock


class TradeTestClass(TestCase):
    def setUp(self):
        super().setUp()
        self.customer = Mock(Customer)
        self.customer.get_name.return_value = "jack"
        self.customer.get_stock_list.return_value = [
            "삼성전자",
            "현대자동차",
            "SK텔레콤",
        ]
        self.customer.get_function_list.return_value = [
            '예약매수("삼성전자",1000)',
            '예약매수("lg전자",500)',
            '예약매도("현대자동차",10)',
        ]

    def test_case1_Customer(self):
        self.assertEqual(self.customer.get_name(), "jack")
        self.assertEqual(
            self.customer.get_stock_list(), ["삼성전자", "현대자동차", "SK텔레콤"]
        )
        self.assertEqual(
            self.customer.get_function_list(),
            [
                '예약매수("삼성전자",1000)',
                '예약매수("lg전자",500)',
                '예약매도("현대자동차",10)',
            ],
        )
