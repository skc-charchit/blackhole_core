import logging
from mongodb import get_mongo_client  # updated import

class BaseAgent:
    def __init__(self, tools=None, memory=None, source=None):
        self.tools = tools if tools is not None else []
        self.memory = memory
        self.source = source

        self.logger = logging.getLogger(self.__class__.__name__)
        if not logging.getLogger().hasHandlers():
            logging.basicConfig(level=logging.INFO)

        # Initialize Mongo client only once per agent instance
        self.client = get_mongo_client()

    def plan(self, input_data):
        raise NotImplementedError("Subclasses should implement the plan method.")

    def run(self, input_data):
        self.logger.info(f"Running agent {self.__class__.__name__} with input: {input_data}")
        plan = self.plan(input_data)
        self.logger.info(f"Generated plan: {plan}")
        return plan

    def tag_source(self, data):
        if self.source:
            return {"source": self.source, "data": data}
        return data

    def store_result(self, data):
        try:
            db = self.client["blackhole_db"]
            collection = db["agent_outputs"]
            collection.insert_one(data)
            self.logger.info(f"Result stored successfully for {self.__class__.__name__}")
        except Exception as e:
            self.logger.error(f"Error storing result: {e}")
