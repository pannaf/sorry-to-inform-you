import os

from retell import Retell
from dotenv import load_dotenv

load_dotenv()

number_test = "+1 (510) 570-7879"
def place_call(to_number):
    client = Retell(api_key=os.getenv("RETELL_API_KEY"))
    call = client.call.create(
        from_number="+14158910214",
        to_number=to_number,
        override_agent_id="c2a3bb9ef69532220dde5eeb26a9c289",
    )
    return call.agent_id

place_call(number_test)