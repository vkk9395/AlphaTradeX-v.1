from upstox_client.configuration import Configuration
from upstox_client.api_client import ApiClient
from upstox_client.apis.tags import market_quote_api

# 🔑 Use your new keys
api_key = "3599d065-c7d0-4a2c-b36f-2ed73b69c490"
access_token = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2U0JZTjQiLCJqdGkiOiI2ODc2Njk2OWJlNmRhMzRiNjhjNzg3NzEiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6dHJ1ZSwiaWF0IjoxNzUyNTkwNjk3LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NTI2MTY4MDB9.36651kytqbJk0XIEwzWoBlkWDxEcxmVEOgxYh82zyOw"

def get_live_index_prices():
    try:
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
