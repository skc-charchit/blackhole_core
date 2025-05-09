from blackhole_core.agents.base_agent import BaseAgent

class MyAgent(BaseAgent):
    def plan(self, input_data):
        return f"MyAgent recevied: {input_data}"

    # def run(self, input_data):
    #     return f"Running with {input_data}"
