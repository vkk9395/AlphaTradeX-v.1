from upstox_client.api import Upstox
from upstox_client.configuration import Configuration
from upstox_client.api_client import ApiClient
from upstox_client.apis.tags import market_quote_api

# ⛳ Paste your actual keys here
access_token = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2U0JZTjQiLCJqdGkiOiI2ODc2NjE4MWJlNmRhMzRiNjhjNzg3MDAiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6dHJ1ZSwiaWF0IjoxNzUyNTg4NjczLCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NTI2MTY4MDB9.gWZfIu-J-biGiRuY31RQ_ke_f3199WJoc0zicVrCszo"
api_key = "7fea734d-af8b-48a6-bef2-8018be5f9db9"

def get_live_index_prices():
    config = Configuration()
    config.access_token = access_token
    config.api_key["apiKey"] = api_key
    config.api_key_prefix["apiKey"] = "Bearer"

    client = ApiClient(config)
    quote_api = market_quote_api.MarketQuoteApi(client)

    indices = [
        "NSE_INDEX|Nifty 50",
        "NSE_INDEX|Nifty Bank",
        "BSE_INDEX|Sensex"
    ]

    try:
        response = quote_api.get_full_market_quote(symbols=indices)
        result = {}
        for symbol, data in response["data"].items():
            result[symbol] = {
                "LTP": data["last_price"],
                "Change": data["change"],
                "Change (%)": round(data["pchange"], 2)
            }
        return result
    except Exception as e:
        return {"error": str(e)}

