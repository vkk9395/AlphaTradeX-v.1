from upstox_client.configuration import Configuration
from upstox_client.api_client import ApiClient
from upstox_client.apis.tags import market_quote_api

# Replace with your credentials
access_token = "eyJ0eXAiOiJKV1QiLCJ..."  # your access token
api_key = "7fea734d-af8b-48a6-bef2-8018be5f9db9"

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
