from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarizer.extract import extractText
from summarizer.chunking import chunkText
from summarizer.summarization import summarize
import tempfile
import os
from summarizer.embedding import embedText

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; you can specify specific origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/summarize/")
async def summarize_pdf(pdf_file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(await pdf_file.read())
            pdf_path = temp_file.name
        
        text = extractText(pdf_path)
        chunks = chunkText(text)

        summaries = summarize(chunks)

        os.remove(pdf_path)

        return {"summaries": summaries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
