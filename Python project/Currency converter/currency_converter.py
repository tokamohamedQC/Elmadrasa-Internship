import requests

init_currency = input("Enter your initial currency: ")
target_currency = input("Enter your target currency: ")

while True:
    try:
        amount = float(input("Enter amount: "))
    except:
        print("The amount should be numeric!")
        continue
    
    if amount == 0:
        print("amount should be greater than 0")
        continue
    else:
        break
    
url = ("https://api.apilayer.com/fixer/convert?to=" + target_currency + "&from=" + init_currency + "&amount=" +str(amount))

payload = {}
headers= {
  "apikey": "U9r6O1PRdXQY6i7zibgk5RvBI7MtlidR"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if(status_code !=200):
    print("Sorry, server error")


result = response.json()
converted_amount = result['result']
print(f"{amount} {init_currency} = {converted_amount} {target_currency}")    