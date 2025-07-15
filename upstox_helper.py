from upstox_api.api import Upstox
from upstox_api.api import LiveFeedType
from upstox_api.exceptions import UpstoxAPIException

api_key = "7fea734d-af8b-48a6-bef2-8018be5f9db9"
access_token = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2U0JZTjQiLCJqdGkiOiI2ODc2NjU2NGJlNmRhMzRiNjhjNzg3M2IiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6dHJ1ZSwiaWF0IjoxNzUyNTg5NjY4LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NTI2MTY4MDB9.-uOZVd_-Q7X8D5VJFRMJjlrK1YGp1p7EynbQDIF6GII"

u = Upstox(api_key, access_token)

def get_live_index_prices():
    try:
        u.get_master_contract('NSE_INDEX')
        indices = ["Nifty 50", "Nifty Bank", "Sensex"]
        result = {}
        for index in indices:
            instrument = u.get_instrument_by_symbol('NSE_INDEX', index)
            quote = u.get_live_feed(instrument, LiveFeedType.Full)
            result[index] = {
                "LTP": quote['last_traded_price'],
                "Change": quote['change'],
                "Change (%)": round(quote['change_percent'], 2)
            }
        return result
    except UpstoxAPIException as e:
        return {"error": f"Upstox Error: {e}"}
    except Exception as e:
        return {"error": f"Unhandled Error: {e}"}



