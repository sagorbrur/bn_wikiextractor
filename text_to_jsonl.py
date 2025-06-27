import re
import glob
import json
from tqdm import tqdm

def extract_documents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Regex pattern to match each <doc ...> ... </doc> block
    doc_pattern = re.compile(r'<doc\s+id="(?P<id>\d+)"\s+url="(?P<url>[^"]+)"\s+title="(?P<title>[^"]+)">\s*(?P<content>.*?)\s*</doc>', re.DOTALL)
    
    documents = []
    for match in doc_pattern.finditer(text):
        doc = {
            'id': match.group('id'),
            'url': match.group('url'),
            'title': match.group('title'),
            'content': match.group('content').strip()
        }
        documents.append(doc)
    
    return documents

# Example usage
if __name__ == "__main__":
    files = glob.glob('text/**/*')  # Adjust the pattern as needed
    print(len(files))
    with open("bangla_wikipedia.jsonl", "w", encoding="utf-8") as output_file:
        for file_path in tqdm(files):
            docs = extract_documents(file_path)

            # Print or save results
            for i, doc in enumerate(docs):
                json.dump(doc, output_file, ensure_ascii=False)
                output_file.write('\n')
                