import requests
from datetime import datetime
from blackhole_core.agents.base_agent import BaseAgent

class LiveDataAgent(BaseAgent):
    def plan(self, input_data):
        try:
            response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
            data = response.json()
            price = data['bitcoin']['usd']

            insight = {
                "agent": "LiveDataAgent",
                "input": input_data,
                "output": f"Current Bitcoin price is ${price}",
                "timestamp": datetime.utcnow(),
                "metadata": {"currency": "BTC", "source": "CoinGecko API"}
            }

            self.store_result(insight)
            return insight
        except Exception as e:
            return {"error": str(e)}
