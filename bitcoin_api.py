import requests
from pprint import pprint

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'


# def get_user_dollars():
#     while True:
#         try:
#             money = float(input("Enter dollar vaule:  $"))
#         except ValueError:
#             print('Please enter a numeric value')
#             continue
#         if money <= 0:
#             print("Invalid. Please enter number higher than 0")
#             continue
#         elif money > 0:
#             return money

def get_api_data():
    response = requests.get(url)
    data = response.json()
    return data


def get_btc_value(data):
    while True:
        try:
            return data['bpi']['USD']['rate_float']
        except requests.RequestException:
            print("Something went wrong with the request ")
            break


def exchange(btc_value, dollars):
    rate = 1 / btc_value
    exchanged_value = round(dollars * rate, 2)

    return exchanged_value


# def quit_program():
#     while True:
#         choice = input("Enter to go again, or Q to quit: ")
#         if not choice.upper() == "Q":
#             if not choice.upper() == "":
#                 print("invalid entry")
#                 continue
#             elif choice == "":
#                 break
#         if choice.upper() == "Q":
#             exit()



def main():
    dollars = 100000
    data = get_api_data()
    rate = get_btc_value(data)
    exchanged_value = exchange(rate, dollars)
    print(f"${exchanged_value:.2f}")
    # quit_program()

if __name__ == "__main__":
    main()