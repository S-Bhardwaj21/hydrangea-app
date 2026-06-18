import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

# Initialize the client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)