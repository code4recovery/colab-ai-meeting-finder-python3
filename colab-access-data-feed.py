import json
from google.colab import ai
from google.colab import drive # For mounting Google Drive

# Mount Google Drive
drive.mount('/content/drive', force_remount=True)
json_data_path = "/content/drive/MyDrive/sample_data/feed.json"

"""Loads JSON data from a file."""
with open(json_data_path, "r", encoding="utf-8") as f:
    json_data = json.load(f)

nodetext = json_data

ai_prompt = f"""
Please provide meeting details such as day, formatted_time, name, and types based on the following json data:
{nodetext}
"""
try:
    # Start the interactive query loop
    while True:
        query = input("Enter your query: ")
        if query.lower() == "exit":
            break
        response = ai.generate_text(prompt=ai_prompt+" "+query)
        print("\n--- AI Model Response ---")
        print(response)
except Exception as e:
    print(f"\nCould not generate AI response. Please ensure you are running this in a Google Colab notebook. Error: {e}")
