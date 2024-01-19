# from preprocessing.data_preprocessing import preprocess_data
from models.gpt2_model import GPT2Model

def main():
    # Example main script logic
    
    # Data Preprocessing
    # Steps
    
    # GPT-2 Model Usage
    gpt2_model = GPT2Model()
    generated_text = gpt2_model.generate_text("As a marketing company we ")
    print(generated_text)

if __name__ == "__main__":
    main()
