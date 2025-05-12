# BlackHole Core MCP(Model Context Protocol)

This project sets up the foundational architecture for the Blackhole SLM/Multimodal core --- agent-ready.

- Multimodal-capable, and MCP-compatible
**Blackhole Core** is a modular Python framework for processing and analyzing multimodal data (like images and PDFs) using AI agents. It integrates text extraction tools, agent-based search systems, and a MongoDB backend to store processed outputs and insights.  
The project is designed for real-time document analysis and archive search scenarios.

---

## 📂 Project Structure


```plaintext
blackhole_core/
│
├── blackhole_core/
│   ├── agents/
│   │   ├── archive_search_agent.py      # Agent for searching text in archived CSV data
│   │   ├── live_data_agent.py           # (Optional) For live API data search
│   │   ├── loader.py                    # Agent loader utility
│   │   └── __init__.py
│   │
│   ├── data_source/
│   │   ├── mongodb.py                   # MongoDB connection and utility methods
│   │   ├── sample_archive.csv           # Archive data CSV file
│   │   └── __init__.py
│   │
│   ├── run_agents_demo.py               # Demo script for testing agent functionality
│   └── __init__.py
│
├── data/
│   ├── multimodal/
│   │   ├── image_ocr.py                 # OCR image text extraction module
│   │   ├── pdf_reader.py                # PDF text extraction module
│   │   ├── caption_generator.py         # (Optional) Image caption generation
│   │   ├── sample.pdf                   # Sample PDF file
│   │   ├── black-white-color-quotes-dave-matthews-...webp  # Sample image for OCR
│   │   └── __init__.py
│   │
│   ├── pipelines/
│   │   ├── blackhole_demo.py            # Main multimodal demo pipeline script
│   │   └── __init__.py
│   │
│   ├── tasks/
│   │   └── __init__.py
│   │
│   └── api/
│       └── __init__.py
│
├── .env                                 # Environment variables (MongoDB URI etc.)
├── .gitignore                           # Git ignore rules
├── Dockerfile                           # (Optional) Docker container setup
├── docker-compose.yaml                  # (Optional) Docker compose config
├── LICENSE
├── README.md                            # Project documentation
├── requirements.txt                     # Python dependencies
└── run_agents_demo.py                   # Agent test runner script