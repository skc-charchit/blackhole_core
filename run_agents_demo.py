from blackhole_core.agents.loader import load_agent

# Load MyAgent dynamically via loader
MyAgentClass = load_agent("my_agent")
my_agent = MyAgentClass(memory=[], source="test")
result = my_agent.plan("Hello Agent!")
print("\n--- MyAgent Result ---")
print(result)
