import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import json
import os

def model_fn(model_dir, model_name):
    model_path = os.path.join(model_dir, model_name)
    model = GPT2LMHeadModel.from_pretrained(model_path)
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    return {'model': model, 'tokenizer': tokenizer}

def save_model(model, tokenizer, save_dir):
    os.makedirs(save_dir, exist_ok=True)
    model.save_pretrained(save_dir)
    tokenizer.save_pretrained(save_dir)

def input_fn(request_body, content_type):
    if content_type == 'application/json':
        data = json.loads(request_body)
        return data['prompt']
    else:
        raise ValueError(f"Unsupported content type: {content_type}")

def output_fn(prediction, content_type):
    return prediction

def predict_fn(input_data, saved_model):
    model = saved_model['model'].to(torch.device("cuda" if torch.cuda.is_available() else "cpu"))
    tokenizer = saved_model['tokenizer']
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    
    max_length = 150
    num_return_sequences = 1

    input_ids = tokenizer.encode(input_data, return_tensors='pt', max_length=max_length, truncation=True, padding=True)

    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        no_repeat_ngram_size=2,
        pad_token_id=tokenizer.eos_token_id,
        attention_mask=input_ids.ne(tokenizer.pad_token_id)
    )

    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return generated_text

# Example usage:
if __name__ == "__main__":
    model_dir = 'model'
    model_name = 'gpt_2'
    model = model_fn(model_dir, model_name)
    generated_text = predict_fn("We at Matt Young Media, as a marketing and copywriting company", model)
    
    # Save the model and tokenizer locally
    save_dir = 'model\gpt_2'
    save_model(model['model'], model['tokenizer'], save_dir)
    
    print(f"Generated Text: {generated_text}")
    print(f"Model and tokenizer saved to: {save_dir}")
