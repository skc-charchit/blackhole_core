import pandas as pd
from datetime import datetime
from bson import ObjectId
from blackhole_core.data_source.mongodb import get_mongo_client
import os

class ArchiveSearchAgent:
    def __init__(self, memory=None, source=None):
        """Initialize ArchiveSearchAgent with optional memory and source, and setup MongoDB client."""
        self.memory = memory
        self.source = source or "csv"
        self.client = get_mongo_client()
        self.db = self.client["blackhole_db"]

        # Dynamically resolve archive CSV path
        self.archive_path = os.path.join(os.path.dirname(__file__), '..', 'data_source', 'sample_archive.csv')
        if not os.path.exists(self.archive_path):
            raise FileNotFoundError(f"Sample archive not found at {self.archive_path}")

    def plan(self, query):
        """Search for matches in the archive CSV based on the provided document_text in query."""
        document_text = query.get('document_text', "")
        if not document_text:
            return {"error": "No document_text provided."}

        df = pd.read_csv(self.archive_path)

        matches = df[
            df.apply(lambda row: document_text.lower() in row.astype(str).str.lower().to_string(), axis=1)
        ]

        result = {
            "agent": "ArchiveSearchAgent",
            "input": query,
            "output": matches.to_dict(orient='records') if not matches.empty else "No matches found.",
            "timestamp": datetime.now(),
            "metadata": {"source_file": self.archive_path}
        }
        return result

    def run(self, query):
        """Alias for the plan() method for compatibility with pipelines."""
        return self.plan(query)
