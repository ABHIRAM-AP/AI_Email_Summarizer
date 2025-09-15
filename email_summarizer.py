from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn",device=0)

def summarize_email(email_body):
    length = len(email_body.split())

    max_len = min(150, int(length * 0.7))
    min_len = min(50, int(length * 0.3))
    try:
        summarized_email = summarizer(
            email_body, max_length=max_len, min_length=min_len, do_sample=False
        )
        return summarized_email[0]['summary_text'] 
        # print(f"Summarized Email: \n{summarized_email[0]['summary_text']}")
    except Exception as e:
        return f"Error: {e}"


