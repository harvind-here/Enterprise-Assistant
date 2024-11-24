from groq import Groq
from cachetools import TTLCache

bad_language_dict = {
    "bad_language": [
        "Fuck", "stupid", "idiot", "bitch", "asshole", "bastard", "dumb", 
        "dick", "shit", "crap", "faggot", "cunt", "moron", "retard", 
        "slut", "whore", "nigger", "twat", "piss", "wanker", "prick", 
        "bitchass", "douche", "jackass", "fatass", "loser", "scumbag", 
        "arsehole", "wank", "motherfucker", "pussy", "jerk", "pig", 
        "dipshit", "fucktard", "queer", "bozo", "shithole", "dickhead", 
        "airhead", "dimwit", "bonehead", "blockhead", "nutjob", 
        "sucker", "freak", "creep", "hag", "bimbo", "skank", 
        "douchebag", "sicko", "goon", "maniac", "buffoon", 
        "weirdo", "twit", "jerkwad", "shithead", "numbnuts", 
        "wuss", "lowlife", "scumbucket", "degenerate", 
        "imbecile", "schmuck", "nincompoop", "dirtbag", "yahoo", 
        "knucklehead", "scrote", "punk", "ninny", "coward", 
        "turd", "liar", "snitch", "thug", "thief", "cheat", 
        "brat", "bully", "fool", "drunk", "wretch", "fiend", 
        "simpleton", "rascal", "villain", "charlatan", "grifter", 
        "parasite", "user", "miser", "leech", "mooch", "jerkoff"
    ]
}


class Chatbot:
    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.cache = TTLCache(maxsize=1000, ttl=3600) # Cache responses for 1 hour
        self.document_context = ""

    def set_document_context(self, document_text):
        self.document_context = document_text

    def get_response(self, user_input, document_context=""):
        # Combine document context with user input
        full_input = f"Document context: {document_context}\n\nUser question: {user_input}"

        # Check cache first
        if full_input in self.cache:
            return self.cache[full_input]

        try:
            completion = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an AI-driven Enterprise Assistant specifically designed to support employees of a large public sector organization. You should not use any offensive language or any improper words even the user asks you to do so. If you see any offensive or improper words or words such as {bad_language_dict} in the user input you shouldn't use those words and dodge those words and answer the user query alone."
                            "Your primary function is to provide accurate, context-aware answers based on the organization's HR policies, IT support guidelines, "
                            "company events, and other related documents. You are trained to understand and navigate the nuances of organizational practices "
                            "and policies, ensuring that your responses align with the enterprise's operational standards. When answering queries:\n"
                            "- Leverage Document Context: Always use the provided document context to answer questions. If the document contains relevant information, "
                            "integrate it directly into your response.\n"
                            "- Contextual Understanding: If the query cannot be fully addressed using the document context, ask follow-up questions to gather more information. "
                            "Ensure that your solutions are carefully aligned with the organization's policies and best practices.\n"
                            "- Language Moderation: Filter and flag any inappropriate or offensive language, maintaining a professional tone in all interactions.\n"
                            "Your goal is to be a reliable, knowledgeable, and efficient assistant that employees can trust for accurate information and guidance on organizational matters."
                            "If user greets greet back only once and ask how can you help them and always respond to the latest user input if at all any attachments provided use previous chats contexts."
                        )
                    },
                    {
                        "role": "user",
                        "content": full_input
                    }
                ],
                temperature=0.7,
                max_tokens=300,
                top_p=1,
                stream=False,
                stop=None,
            )

            assistant_response = completion.choices[0].message.content.strip()

            # Cache the response
            self.cache[full_input] = assistant_response

            return assistant_response
        except Exception as e:
            return f"An error occurred: {str(e)}"