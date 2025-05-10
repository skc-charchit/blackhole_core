import pandas as pd
from datetime import datetime
from blackhole_core.agents.base_agent import BaseAgent
from mongodb import client  # assuming mongodb.py is at project root

class ArchiveSearchAgent(BaseAgent):
    def plan(self, input_data):
        try:
            # Load CSV from data_sources
            file_path = "blackhole_core/data_sources/sample_archive.csv"
            df = pd.read_csv(file_path)

            # Simple keyword search: look for input_data in any cell
            results = df[df.apply(lambda row: row.astype(str).str.contains(input_data, case=False).any(), axis=1)]

            # Prepare structured result
            output = results.to_dict(orient="records") if not results.empty else "No matches found."

            insight = {
                "agent": "ArchiveSearchAgent",
                "input": input_data,
                "output": output,
                "timestamp": datetime.utcnow(),
                "metadata": {"source_file": file_path}
            }

            # Store result in MongoDB
            self.store_result(insight)

            return insight

        except Exception as e:
            return {"error": str(e)}

    def store_result(self, data):
        try:
            db = client["blackhole_db"]  # your database name
            collection = db["agent_outputs"]
            collection.insert_one(data)
        except Exception as e:
            print(f"Error storing result: {e}")
