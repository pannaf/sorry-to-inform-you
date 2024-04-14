import os
import json
import textwrap

from dotenv import load_dotenv
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

from mock_data import BEHAVIORS, JOB_DESCRIPTIONS, MOCK_TRANSCRIPT

behaviors = [behavior for behavior in BEHAVIORS.values()]
job_descriptions = [desc for desc in JOB_DESCRIPTIONS.values()]

load_dotenv()

openai_api_key = os.getenv("TUNE_API_KEY")


mixtral_model = ChatOpenAI(
    openai_api_key=openai_api_key,
    openai_api_base="https://proxy.tune.app/",
    model_name="rohan/mixtral-8x7b-inst-v0-1-32k",
    max_tokens=4096,
    model_kwargs={"response_format": {"type": "json_object"}},
)

interview_guidelines_system_message = textwrap.dedent(
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

call_assessment_system_message = textwrap.dedent(
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


class JSONObjectOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a JSON object."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        try:
            data_dict = json.loads(text)
            return data_dict
        except json.JSONDecodeError:
            return str(text)


def get_questions(
    llm_model, message="what questions do you have for me?", system_message=None, job_description=None, behavior_characteristics=None
):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "{system_message}\n---------\nJob description:\n{job_description}\n---------\nDesired behavior characteristics:\n{behavior_characteristics}",
            ),
            ("human", "{text}"),
        ]
    )

    chain = prompt | llm_model | JSONObjectOutputParser()
    response = chain.invoke(
        {
            "text": message,
            "job_description": job_description,
            "behavior_characteristics": behavior_characteristics,
            "system_message": system_message,
        }
    )
    return response


def assess_call(
    llm_model,
    message="how did the call go?",
    system_message=None,
    call_transcript=None,
    job_description=None,
    behavior_characteristics=None,
):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "{system_message}\n--------\nCall transcript:\n{call_transcript}\n--------\nJob descriptions:{job_description}\n---------\nDesired behavior characteristics:\n{behavior_characteristics}",
            ),
            ("human", "{text}"),
        ]
    )

    chain = prompt | llm_model | JSONObjectOutputParser()
    response = chain.invoke(
        {
            "text": message,
            "system_message": system_message,
            "call_transcript": call_transcript,
            "job_description": job_description,
            "behavior_characteristics": behavior_characteristics,
        }
    )
    return response


def main():
    run_get_questions = True

    job_description = "We are looking for a software engineer to join our team. The ideal candidate should have experience with Python, Java, and C++. The candidate should also have experience with machine learning and data science."
    behavior_characteristics = (
        "The ideal candidate should be a team player, have strong communication skills, and be able to work independently."
    )

    if 0:
        questions = get_questions(
            mixtral_model,
            message="what questions do you have for me?",
            system_message=interview_guidelines_system_message,
            job_description=job_description,
            behavior_characteristics=behavior_characteristics,
        )
        print(f"{questions}")

    if 0:
        call_assessment = assess_call(
            mixtral_model,
            message="how did the call go?",
            system_message=call_assessment_system_message,
            call_transcript=call_transcript,
        )

    if run_get_questions:
        results = []
        for i in range(3):
            questions = get_questions(
                mixtral_model,
                message="",
                system_message=interview_guidelines_system_message,
                job_description=job_descriptions[i],
                behavior_characteristics=behaviors[i],
            )
            results.append(questions)

        print(results)

    good_call_assessment = assess_call(
        mixtral_model,
        message="how did the call go?",
        system_message=call_assessment_system_message,
        call_transcript=MOCK_TRANSCRIPT["retail_worker"]["good"],
    )

    bad_call_assessment = assess_call(
        mixtral_model,
        message="how did the call go?",
        system_message=call_assessment_system_message,
        call_transcript=MOCK_TRANSCRIPT["retail_worker"]["bad"],
    )

    print("GOOD CALL ASSESSMENT")
    print(good_call_assessment)

    print("BAD CALL ASSESSMENT")
    print(bad_call_assessment)


if __name__ == "__main__":
    main()
