# app/llm_integration.py
import os
import torch
from transformers import pipeline

# Set up the model and pipeline
model_id = "meta-llama/Meta-Llama-3-8B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

def query_llm(prompt: str, context: str) -> str:
    messages = [
        {"role": "system", "content": "You are a knowledgeable assistant."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": context}
    ]
    
    # Create the prompt using the provided messages
    prompt_text = pipe.tokenizer.apply_chat_template(
        messages, 
        tokenize=False, 
        add_generation_prompt=True
    )

    # Define terminators for the generation
    terminators = [
        pipe.tokenizer.eos_token_id,
        pipe.tokenizer.convert_tokens_to_ids("")
    ]
    
    # Generate the output
    outputs = pipe(
        prompt_text, 
        max_new_tokens=256, 
        eos_token_id=terminators, 
        do_sample=True, 
        temperature=0.6, 
        top_p=0.9
    )
    
    return outputs[0]["generated_text"][len(prompt_text):].strip()

