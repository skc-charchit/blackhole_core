# agents/base_agent.py

import logging

class BaseAgent:
    def __init__(self, tools=None, memory=None, source=None):
        self.tools = tools or []
        self.memory = memory
        self.source = source
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = logging.FileHandler(f'{self.__class__.__name__}.log')
            formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def plan(self, input_data):
        self.logger.info(f"Planning with input: {input_data}")
        raise NotImplementedError

    def run(self, input_data):
        self.logger.info(f"Running with input: {input_data}")
        raise NotImplementedError

    def tag_source(self, data):
        if self.source:
            return {"source": self.source, "data": data}
        return data
