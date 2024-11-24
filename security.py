import bcrypt
import os
from dotenv import load_dotenv, set_key
import re

load_dotenv()

# Load the hashed passcode from environment variables
HASHED_PASSCODE = os.getenv('HASHED_PASSCODE')

def sanitize_input(input_string):
    # Remove any HTML tags
    cleaned = re.sub(r'<[^>]*>', '', input_string)
    
    # Remove any potential SQL injection attempts
    cleaned = re.sub(r'(\s(SELECT|INSERT|UPDATE|DELETE|DROP|TRUNCATE|ALTER|CREATE|TABLE|FROM|WHERE|AND|OR)(\s|\())','', cleaned, flags=re.IGNORECASE)
    
    # Remove any non-alphanumeric characters except spaces and common punctuation
    cleaned = re.sub(r'[^\w\s.,!?-]', '', cleaned)
    
    # Limit the length of the input
    #max_length = 1000  # Adjust this value as needed
    #cleaned = cleaned[:max_length]
    
    return cleaned.strip()

def validate_passcode(passcode):
    if not HASHED_PASSCODE:
        return False
    try:
        return bcrypt.checkpw(passcode.encode('utf-8'), HASHED_PASSCODE.encode('utf-8'))
    except ValueError as e:
        print(f"Error validating passcode: {str(e)}")
        return False

def generate_hashed_passcode(new_passcode):
    hashed = bcrypt.hashpw(new_passcode.encode('utf-8'), bcrypt.gensalt(rounds=10))
    hashed_str = hashed.decode('utf-8')
    set_key('.env', 'HASHED_PASSCODE', hashed_str)
    global HASHED_PASSCODE
    HASHED_PASSCODE = hashed_str
    return hashed_str

def is_passcode_set():
    return bool(HASHED_PASSCODE)