from upstox_client import Configuration, ApiClient
from upstox_client.apis.tags import market_quote_api

access_token = "eyJ0eXAiOiJKV1QiLCJrZXlfaWQiOiJza192MS4wIiwiYWxnIjoiSFMyNTYifQ.eyJzdWIiOiI2U0JZTjQiLCJqdGkiOiI2ODc2Njk2OWJlNmRhMzRiNjhjNzg3NzEiLCJpc011bHRpQ2xpZW50IjpmYWxzZSwiaXNQbHVzUGxhbiI6dHJ1ZSwiaWF0IjoxNzUyNTkwNjk3LCJpc3MiOiJ1ZGFwaS1nYXRld2F5LXNlcnZpY2UiLCJleHAiOjE3NTI2MTY4MDB9.36651kytqbJk0XIEwzWoBlkWDxEcxmVEOgxYh82zyOw"
api_key = "3599d065-c7d0-4a2c-b36f-2ed73b69c490"

def get_live_index_prices():
    try:
        config = Configuration()
        config.access_token = access_token
        config.api_key["apiKey"] = api_key
        config.api_key_prefix["apiKey"] = "Bearer"

        api_client = ApiClient(config)
        quote_api = market_quote_api.MarketQuoteApi(api_client)

        symbols = ["NSE_INDEX|Nifty 50", "NSE_INDEX|Nifty Bank", "BSE_INDEX|Sensex"]
        response = quote_api.get_full_market_quote(symbols=symbols)

        result = {}
        for symbol, item in response["data"].items():
            result[symbol] = {
                "LTP": item["last_price"],
                "Change": item["change"],
                "Change (%)": round(item["pchange"], 2)
            }

        return result
    except Exception as e:
        return {"error": str(e)}
