import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin_api

test_data = {
    'bpi': {
        'EUR': {
            'code': 'EUR',
            'description': 'Euro',
            'rate': '56,482.672',
            'rate_float': 56482.6719,
            'symbol': '&euro;'
        },
        'GBP': {
            'code': 'GBP',
            'description': 'British Pound Sterling',
            'rate': '48,342.728',
            'rate_float': 48342.7277,
            'symbol': '&pound;'},
        'USD': {
            'code': 'USD',
            'description': 'United States Dollar',
            'rate': '61,206.73',
            'rate_float': 61206.7297,
            'symbol': '&#36;'}
    },
    'chartName': 'Bitcoin',
    'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index '
                  '(USD). Non-USD currency data converted using hourly conversion '
                  'rate from openexchangerates.org',
    'time': {'updated': 'Feb 29, 2024 01:18:39 UTC',
             'updatedISO': '2024-02-29T01:18:39+00:00',
             'updateduk': 'Feb 29, 2024 at 01:18 GMT'}
}


class TestBitcoinAPI(TestCase):

    @patch('bitcoin_api.get_api_data', return_value=test_data)
    def test_exchange(self, mock_get_api_data):
        data = bitcoin_api.get_api_data()
        btc_value = bitcoin_api.get_btc_value(data)
        exchange_value = bitcoin_api.exchange(btc_value, 100000)
        self.assertEqual(exchange_value, 1.63)

    # @patch('builtins.input') # to test multiple numbers we forgo assigning side_effect list here
    # def test_get_user_dollars(self, mock_input):
    #     test_numbers = ['100', '1000', '10000', '10000', '100000', '1000000']
    #     for number in test_numbers:
    #         mock_input.side_effect = [number] # manually assign side_effect to test number iteration
    #         money = bitcoin_api.get_user_dollars()
    #         self.assertEqual(money, float(number))

    # @patch('builtins.input', side_effect = ['float', 'toast', 'grasp', 'chicken', 'argonaut', '1000000']) # to test
    # multiple numbers we forgo assigning side_effect list here def test_get_user_dollars_non_numeric(self,
    # mock_input): money = bitcoin_api.get_user_dollars() self.assertEqual(money, float(money))


