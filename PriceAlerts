from twilio.rest import Client
from binance.client import Client as BinanceClient
import schedule
import time

# Twilio Credentials
twilio_account_sid = "AC1b7c93190d022da218a620a407cabcd0"
twilio_auth_token = "629c1666c474de55a51f10c68f83cdb9"
twilio_whatsapp_number = "whatsapp:+14155238886"  # Twilio Sandbox WhatsApp number
your_whatsapp_number = "whatsapp:+2348149040934"

# Binance API Client (Public API)
binance_client = BinanceClient()

# Twilio Client
twilio_client = Client(twilio_account_sid, twilio_auth_token)

# Function to fetch $HBAR price
def fetch_hbar_price():
    try:
        ticker = binance_client.get_symbol_ticker(symbol="HBARUSDT")
        price = float(ticker['price'])
        return price
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
        message = f"Current $HBAR price: ${price:.4f} USDT"
        send_whatsapp_message(message)
    else:
        print("Failed to fetch price.")

# Schedule the bot to run every minute
schedule.every(3).minutes.do(check_hbar_price)

if __name__ == "__main__":
    print("WhatsApp bot running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
