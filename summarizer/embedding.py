from transformers import AutoTokenizer, AutoModel
import torch

modelName = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(modelName)
model = AutoModel.from_pretrained(modelName)

def embedText(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True,clean_up_tokenization_spaces=False)
    with torch.no_grad():
        embeddings = model(**inputs)
    return embeddings.last_hidden_state.mean(dim=1).squeeze().numpy()