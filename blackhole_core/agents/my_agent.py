# from agents.loader import load_agent

# AgentClass = load_agent('my_agent')
# agent = AgentClass(memory=[], source="api")


from blackhole_core.agents.base_agent import BaseAgent

class MyAgent(BaseAgent):
    def plan(self, input_data):
        return "Plan created"

    def run(self, input_data):
        return f"Running with {input_data}"
