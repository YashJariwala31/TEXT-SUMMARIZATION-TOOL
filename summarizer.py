from transformers import pipeline

# Use PyTorch backend only
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

def generate_summary(text, min_length=30, max_length=120):
    if len(text.split()) < 50:
        return "Text is too short to summarize."
    
    summary = summarizer(text, min_length=min_length, max_length=max_length, do_sample=False)
    return summary[0]['summary_text']
