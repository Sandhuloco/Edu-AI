from transformers import AutoTokenizer

model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)

def chunkText(text, max_length=1024):
    tokenized_text = tokenizer(text, return_tensors='pt', truncation=False, padding=False)
    input_ids = tokenized_text['input_ids'].squeeze().tolist()
    
    chunks = []
    start = 0
    while start < len(input_ids):
        end = min(start + max_length, len(input_ids))
        chunk_ids = input_ids[start:end]
        chunk_text = tokenizer.decode(chunk_ids, skip_special_tokens=True)
        chunks.append(chunk_text)
        start = end
    
    return chunks
