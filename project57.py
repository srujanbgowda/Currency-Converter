import requests

def currency_converter():

    amount = float(input("Enter the amount: "))
    from_currency  = input("From currency(e.g., USD):").upper()
    to_currency = input("To currecy(e.g., EUR):").upper()

    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    try:
        respons = requests.get(url)
        data = respons.json()

        if to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            converted_amount = amount*rate
            print(f"{amount:.2f}{to_currency}={converted_amount:.2f}{to_currency}")

        else:
            print("invalid target currecy.")

    except Exception as e:
        print("Error:",e)         


currency_converter()        



