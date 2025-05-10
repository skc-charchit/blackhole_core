# BlackHole Core MCP(Model Context Protocol)

This project sets up the foundational architecture for the Blackhole SLM/Multimodal core --- agent-ready.

- Multimodal-capable, and MCP-compatible

## Steps:
- blackhole_core: #Contains all agents and Data integration (live API's)
1. agents
2. data_sources

- data: #Contains csv, PDF's, etc.
1. multimodal
2. pipelines
3. tasks
4. api

- adapter #Contains Helper Module
1. utils
2. config

### Project Structure:

project_root/
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yaml
├── LICENSE
├── mongodb.py
├── MyAgent.log
├── README.md
├── requirements.txt
├── run_agents_demo.py
├── run_multimodal_demo.py
│
├── blackhole_core/
│   ├── agents/
│   │   ├── base_agent.py
│   │   ├── my_agent.py
│   │   ├── live_data_agent.py
│   │   ├── archive_search_agent.py
│   │   └── loader.py
│   │
│   ├── data_sources/
│   │   ├── __init__.py
│   │   └── sample_archive.csv
│   │
│   └── data/
│       ├── __init__.py
│       ├── api/
│       ├── multimodal/
│       │   ├── __init__.py
│       │   ├── pdf_reader.py
│       │   ├── image_ocr.py
│       │   └── caption_generator.py
│       │
│       ├── pipelines/
│       └── tasks/
│
├── adapter/
│   ├── config/
│   └── utils/


### Initial Logs:
Day 1: Base model runs successfully.

Day 2: Key Scripts Recap:
✅ mongodb.py → Connects to MongoDB Atlas
✅ loader.py → Dynamically loads agents by name
✅ base_agent.py → Base class for agents
✅ live_data_agent.py → Fetches live Bitcoin price
✅ archive_search_agent.py → Searches CSV for keywords
✅ pdf_reader.py → Extracts text from PDF (PyMuPDF)
✅ image_ocr.py → OCR from image (Pytesseract)
✅ run_agents_demo.py → Runs both sample agents
✅ run_multimodal_demo.py → Runs PDF and Image OCR tests

📄 mongodb.py — MongoDB connection script

🧠 agents/ — BaseAgent and agent implementations

📚 data_sources/ — Local data files like CSVs or PDFs

📊 data/ — Multimodal processing modules (PDF, OCR, etc.)

⚙️ adapter/ — Config and utility scripts

🚀 run_agents_demo.py & run_multimodal_demo.py — Demo runners for agents and multimodal inputs

