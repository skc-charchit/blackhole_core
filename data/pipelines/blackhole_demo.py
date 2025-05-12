import os
from data.multimodal import image_ocr
from blackhole_core.agents.archive_search_agent import ArchiveSearchAgent
from blackhole_core.data_source.mongodb import get_agent_outputs_collection

def process_image_with_agent(image_path):
    print(f"\n🖼️  Processing Image: {image_path}")

    extracted_text = image_ocr.extract_text_from_image(image_path, debug=True)
    print("\n🔍 Extracted Text Preview:\n", extracted_text)

    agent = ArchiveSearchAgent()
    agent_output = agent.plan({"document_text": extracted_text})  # <-- fixed here
    print("\n📊 Agent Output:\n", agent_output)

    result_record = agent_output
    result_record.pop("_id", None)

    try:
        collection = get_agent_outputs_collection()
        collection.insert_one(result_record)
        print("✅ Agent output saved to MongoDB.")
    except Exception as e:
        print(f"❌ Error saving to MongoDB: {e}")

if __name__ == "__main__":
    image_path = r"data\multimodal\black-white-color-quotes-dave-matthews-nothing-is-black-or-white-nothings-us-o-2042.webp"

    if not os.path.exists(image_path):
        print(f"❌ Image file not found: {image_path}")
    else:
        process_image_with_agent(image_path)
