import importlib
import sys
import os

# Ensure that Python can find the 'blackhole_core' directory for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

def load_agent(agent_name):
    """
    Dynamically import and return an agent class by its name.
    Example: load_agent('my_agent') imports agents/my_agent.py and returns MyAgent class.
    """
    # Use the corrected import path
    module = importlib.import_module(f"blackhole_core.agents.{agent_name}")  # Removed blackhole_core prefix
    class_name = ''.join([part.capitalize() for part in agent_name.split('_')])
    return getattr(module, class_name)

# Test block
if __name__ == "__main__":
    AgentClass = load_agent('my_agent')
    agent = AgentClass(memory=[], source="api")
    print(agent)


# import importlib

# def load_agent(agent_name):
#     module = importlib.import_module(f"agents.{agent_name}")
#     class_name = ''.join([part.capitalize() for part in agent_name.split('_')])

#     return getattr(module, class_name)

# # Example test
# if __name__ == "__main__":
#     AgentClass = load_agent('my_agent')
#     agent = AgentClass(memory=[], source="api")
#     print(agent)
