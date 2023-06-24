import telebot, os, requests

api_key = '5403078159:AAG1KF79NlxR24cMJrBGlzMlEIi-N7UgVXY'
bot = telebot.TeleBot(api_key)

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['start'])
def price(message):
    bot.reply_to(message, "If you want to use this bot type /help.")

@bot.message_handler(commands=['help'])
def price(message):
    bot.reply_to(message, """
     If you want to use this bot type any token in coingecko.
                 
Example: /token bitcoin, /token BITCOIN
    """)

#this code is for checking spot price in binance app
@bot.message_handler(commands=['token'])
def price(message):
  try:
    messages = status = extract_arg(message.text)
    msg = messages[0].lower()
    token = "https://api.coingecko.com/api/v3/coins/"+msg
    token = requests.get(token)
    data = token.json()
    print(data)
    
    #PRICE, ATH, ADN ATL WITHIN 24H
    priceInUSD = "$ "+ str(data['market_data']['current_price']['usd'])
    ATHChangePercentageUSD = str(data['market_data']['ath_change_percentage']['usd'])
    ATLChangePercentageUSD = str(data['market_data']['atl_change_percentage']['usd'])
     
    #ATH AND ATL IN USD AND PHP
    AthUSD = str(data['market_data']['ath']['usd'])
    AtlUSD = str(data['market_data']['atl']['usd'])
    
    #PRICE HIGH AND LOW WITHIN 24H IN USD AND PHP
    High24hUSD = str(data['market_data']['high_24h']['usd'])
    Low24hUSD = str(data['market_data']['low_24h']['usd'])
    
    #PRICE PERCENTAGE OF THE TOKEN IN 1D, 1W, 1M, AND 1Y IN USD
    priceChangePercentage24hUSD = str(data['market_data']['price_change_percentage_24h_in_currency']['usd'])
    priceChangePercentage7dUSD = str(data['market_data']['price_change_percentage_7d_in_currency']['usd'])
    priceChangePercentage1mUSD = str(data['market_data']['price_change_percentage_30d_in_currency']['usd'])
    priceChangePercentage1yUSD = str(data['market_data']['price_change_percentage_1y_in_currency']['usd'])
    
    
    allDataUSD = """
Price in US Dollar: """+ priceInUSD + """
All Time HIgh in Percentage: """+ATHChangePercentageUSD+ "%"+ """
All Time Low in Percentage: """+ATLChangePercentageUSD+ "%"+ """
All Time High: $"""+AthUSD+"""
All Time Low: $"""+AtlUSD+"""
High within 24h: $"""+High24hUSD+"""
Low within 24h: $"""+Low24hUSD+"""
1 Day Change: """+priceChangePercentage24hUSD+"%"+"""
30 Dyas Change: """+priceChangePercentage7dUSD+"%"+"""
1 Month Change: """+priceChangePercentage1mUSD+"%"+"""
1 Year Change: """+priceChangePercentage1yUSD+"%"
    

    bot.reply_to(message, allDataUSD)
  except KeyError as e:
    print(e)
    bot.reply_to(message, "If you see this message you probably put the ticker or they don't have the token you want to search. Try tu put the full name of the token again.")

  except IndexError as w:
    print(w)
    
if __name__ == "__main__":
  bot.polling()
