from transformers import AutoTokenizer, AutoModelForCausalLM
from deep_translator import GoogleTranslator
from langdetect import detect  # Mainām uz langdetect

# Ielādē modelis un tokenizētājs
model_name = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def complete_text(input_text, max_length=50):
    # Valodas noteikšana ar langdetect
    detected_language = detect(input_text)

    # Ja valoda nav angļu, tad tulko uz angļu
    if detected_language != 'en':
        translation = GoogleTranslator(source=detected_language, target='en').translate(input_text)
    else:
        translation = input_text

    # Ievade tokenizācijā
    input_ids = tokenizer.encode(translation, return_tensors="pt")
    
    # Teksta ģenerēšana
    output_ids = model.generate(input_ids, max_length=max_length, num_return_sequences=1, eos_token_id=tokenizer.eos_token_id)

    # Ģenerētā teksta dekodēšana
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    
    # Tulko atpakaļ uz sākotnējo valodu
    if detected_language != 'en':
        translated_generated_text = GoogleTranslator(source='en', target=detected_language).translate(generated_text)
        return translated_generated_text
    else:
        return generated_text

if __name__ == "__main__":
    text = "Reiz kādā tālā zemē"  # Piemērs ar latviešu valodas tekstu
    completed_text = complete_text(text)
    print("Pabeigtais teksts:")
    print(completed_text)
