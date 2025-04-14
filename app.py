from transformers import pipeline, set_seed

# GPT-2 text generation pipeline
generator = pipeline('text-generation', model='gpt2')

# Set seed for reproducibility
set_seed(42)

# Ask for user input
prompt = input("Enter your prompt to generate text: ")

# Generate text
output = generator(prompt, max_length=100, num_return_sequences=1)

# Print generated text
print("\nGenerated Text:\n")
print(output[0]['generated_text'])
