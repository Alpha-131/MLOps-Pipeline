from transformers import GPT2LMHeadModel, GPT2Tokenizer

class GPT2Model:
    def __init__(self, model_path='model\gpt_2'):
        # Load the pre-trained GPT-2 model and tokenizer from saved weights
        self.model = GPT2LMHeadModel.from_pretrained(model_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        
        # Add special tokens
        self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    def generate_text(self, prompt, max_length=50, num_return_sequences=1):
        input_ids = self.tokenizer.encode(prompt, return_tensors='pt', max_length=max_length, truncation=True, padding=True)
        
        output = self.model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
            no_repeat_ngram_size=2,
            pad_token_id=self.tokenizer.eos_token_id,
            attention_mask=input_ids.ne(self.tokenizer.pad_token_id)
        )
        
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return generated_text

# Example usage:
if __name__ == "__main__":
    gpt2_model = GPT2Model()
    generated_text = gpt2_model.generate_text("We at Matt Young Media, as an marketing and copywriting company")
    print(generated_text)
