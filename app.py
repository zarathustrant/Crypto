import requests
from twilio.rest import Client
import schedule
import time

# Twilio Credentials
twilio_account_sid = "AC1b7c93190d022da218a620a407cabcd0"  
twilio_auth_token = "8bb269f8860b8b8424d36366498c3347"  
twilio_whatsapp_number = "whatsapp:+14155238886"  
your_whatsapp_number = "whatsapp:+2348149040934"  

# Twilio Client
twilio_client = Client(twilio_account_sid, twilio_auth_token)

# Function to fetch $HBAR price from CoinGecko
def fetch_hbar_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price"
        params = {"ids": "hedera-hashgraph", "vs_currencies": "usd"}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        return data["hedera-hashgraph"]["usd"]
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

# Function to send WhatsApp message
def send_whatsapp_message(message):
    try:
        message = twilio_client.messages.create(
            body=message,
            from_=twilio_whatsapp_number,
            to=your_whatsapp_number
        )
        print(f"Message sent: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Job to check $HBAR price and send updates
def check_hbar_price():
    price = fetch_hbar_price()
    if price is not None:
        message = f"Current $HBAR price: ${price:.4f} USD"
        send_whatsapp_message(message)
    else:
        print("Failed to fetch price.")

# Schedule the bot to run every minute
schedule.every(3).minutes.do(check_hbar_price)

if __name__ == "__main__":
    print("WhatsApp bot running...")
    while True:
        schedule.run_pending()
        time.sleep(3)
