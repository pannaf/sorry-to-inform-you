import os
import json
import textwrap

from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

from mock_data import BEHAVIORS, JOB_DESCRIPTIONS, MOCK_TRANSCRIPT


class JSONObjectOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a JSON object."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        try:
            data_dict = json.loads(text)
            return data_dict
        except json.JSONDecodeError:
            return str(text)


class InterviewAssistant:
    def __init__(self):
        load_dotenv()
        openai_api_key = os.getenv("TUNE_API_KEY")
        self.model = ChatOpenAI(
            openai_api_key=openai_api_key,
            openai_api_base="https://proxy.tune.app/",
            model_name="rohan/mixtral-8x7b-inst-v0-1-32k",
            max_tokens=4096,
            model_kwargs={"response_format": {"type": "json_object"}},
        )
        self.output_parser = JSONObjectOutputParser()

    def get_questions(self, job_description, behavior_characteristics, message="what questions do you have for me?"):
        system_message = textwrap.dedent(
            """Can you generate 6 interview questions for me based on the job description and behavioral characteristics provided?
            Do 3 questions for each.

            The expected output format is the following JSON output:
            ```json
            {{
                "job questions": ["question1", "question2", "question3"]
                "behavior questions": ["question1", "question2", "question3"]
            }}
            ```
            Very important: only return the JSON and nothing else.
            """
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "{system_message}\n---------\nJob description:\n{job_description}\n---------\nDesired behavior characteristics:\n{behavior_characteristics}",
                ),
                ("human", "{text}"),
            ]
        )
        chain = prompt | self.model | self.output_parser
        return chain.invoke(
            {
                "text": message,
                "job_description": job_description,
                "behavior_characteristics": behavior_characteristics,
                "system_message": system_message,
            }
        )

    def assess_call(self, call_transcript, job_description, behavior_characteristics, message="how did the call go?"):
        system_message = textwrap.dedent(
            """Can you assess the call and provide feedback on how it went? You are looking for great candidates.
            Be selective in your feedback and provide a recommendation based on the call transcript, job description, and behavior
            characteristics provided.
            The expected output format is the following JSON output:
            ```json
            {{
                "feedback": <str>, # what feedback you would give the candidate 
                "recommendation": <bool>, # whether to recommend the candidate
                "reason": <str> # reason for the recommendation
                "top relevant skills": <list>, # top relevant skills of the candidate for the job
                "potential skill gaps": <list>, # potential skill gaps of the candidate for the job
                "enthusiasm": <int> # enthusiasm level of the candidate for the job, 1-5 scale
                "job fit": <int>, # how well the candidate fits the job description, 1-5 scale
                "communication": <int>, # how well the candidate communicated, 1-5 scale
            }}
            Very important: only return the JSON and nothing else.
            """
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "{system_message}\n--------\nCall transcript:\n{call_transcript}\n--------\nJob descriptions:{job_description}\n---------\nDesired behavior characteristics:\n{behavior_characteristics}",
                ),
                ("human", "{text}"),
            ]
        )
        chain = prompt | self.model | self.output_parser
        return chain.invoke(
            {
                "text": message,
                "system_message": system_message,
                "call_transcript": call_transcript,
                "job_description": job_description,
                "behavior_characteristics": behavior_characteristics,
            }
        )


def main():
    assistant = InterviewAssistant()
    # Example usage of the assistant
    job = "retail_worker"
    job_description = JOB_DESCRIPTIONS[job]
    behavior_characteristics = BEHAVIORS[job]
    call_transcript = MOCK_TRANSCRIPT[job]["good"]

    questions = assistant.get_questions(job_description, behavior_characteristics)
    assessment = assistant.assess_call(call_transcript, job_description, behavior_characteristics)

    print("Generated Questions:", questions)
    print("Call Assessment:", assessment)


if __name__ == "__main__":
    main()
