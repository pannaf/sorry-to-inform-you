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
    return call.call_id


def get_transcript(call_id):
    client = Retell(api_key=os.getenv("RETELL_API_KEY"))
    call = client.call.retrieve("119c3f8e47135a29e65947eeb34cf12d", )
    return call.transcript


def update_llm(prompt):
    client = Retell()
    llm = client.llm.update("16b980523634a6dc504898cda492e939", )
    print(llm.llm_id)