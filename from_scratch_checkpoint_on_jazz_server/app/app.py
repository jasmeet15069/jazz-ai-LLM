from pathlib import Path
from typing import Optional

import torch
from fastapi import FastAPI
from pydantic import BaseModel, Field
from transformers import GPT2LMHeadModel, GPT2TokenizerFast


MODEL_DIR = Path("/opt/texting-coding-model/model")

torch.set_num_threads(2)

tokenizer = GPT2TokenizerFast.from_pretrained(
    MODEL_DIR,
    bos_token="<s>",
    eos_token="</s>",
    unk_token="<unk>",
    pad_token="<pad>",
    mask_token="<mask>",
)
model = GPT2LMHeadModel.from_pretrained(MODEL_DIR)
model.eval()

app = FastAPI(title="Texting Coding Local LLM")


class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    max_new_tokens: int = Field(80, ge=1, le=256)
    temperature: float = Field(0.8, ge=0.0, le=2.0)
    top_p: float = Field(0.95, ge=0.1, le=1.0)
    seed: Optional[int] = None


@app.get("/health")
def health():
    return {"status": "ok", "model_dir": str(MODEL_DIR)}


@app.post("/generate")
def generate(request: GenerateRequest):
    if request.seed is not None:
        torch.manual_seed(request.seed)

    inputs = tokenizer(request.prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=request.max_new_tokens,
            do_sample=request.temperature > 0,
            temperature=request.temperature if request.temperature > 0 else None,
            top_p=request.top_p,
            pad_token_id=tokenizer.pad_token_id,
            eos_token_id=tokenizer.eos_token_id,
        )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"text": text}
