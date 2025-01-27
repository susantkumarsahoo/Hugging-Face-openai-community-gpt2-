import streamlit as st
from transformers import pipeline

# Load the text generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Function to format the generated text
def format_generated_text(text):
    paragraphs = text.split("\n\n")
    formatted_text = "\n\n".join(paragraph.strip() for paragraph in paragraphs)
    return formatted_text

# Streamlit App
def main():
    st.title("Text Generator with GPT-2")
    st.write("Generate and format text using GPT-2!")

    # User input for text generation
    user_input = st.text_input("Enter a prompt:", "What is data science,")
    max_length = st.slider("Select max length:", min_value=50, max_value=300, value=200)
    num_return_sequences = st.number_input("Number of sequences:", min_value=1, max_value=5, value=1)

    if st.button("Generate Text"):
        with st.spinner("Generating text..."):
            # Generate text
            generated_text = generator(user_input, max_length=max_length, num_return_sequences=num_return_sequences)

            # Display each generated sequence
            for i, result in enumerate(generated_text):
                text = result['generated_text']
                formatted_text = format_generated_text(text)
                st.subheader(f"Generated Text {i+1}")
                st.text_area("Output", formatted_text, height=300)

if __name__ == "__main__":
    main()






