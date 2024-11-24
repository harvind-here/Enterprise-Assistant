from groq import Groq

class DocumentProcessor:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)

    def summarize(self, document_text):
        try:
            completion = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize the following document in a concise manner:\n\n{document_text}"
                    }
                ],
                temperature=0.7,
                max_tokens=100,
                top_p=1,
                stream=False,
                stop=None,
            )

            return completion.choices[0].message.content.strip()
        except Exception as e:
            return f"An error occurred during summarization: {str(e)}"

    def extract_keywords(self, document_text):
        try:
            completion = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "user",
                        "content": f"Extract key points and important keywords from this text:\n\n{document_text}"
                    }
                ],
                temperature=0.7,
                max_tokens=60,
                top_p=1,
                stream=False,
                stop=None,
            )

            return completion.choices[0].message.content.strip()
        except Exception as e:
            return f"An error occurred during keyword extraction: {str(e)}"