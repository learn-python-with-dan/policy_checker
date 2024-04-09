from openai import OpenAI

from src.models import *


__all__ = [
    'is_approved',
    'get_violation_reason',
]


policy = """
Python Playground Policy: Code of Conduct

This policy outlines the expectations for a productive and positive community within our Python coding blog.

Respectful Interactions:
Personal attacks, insults, and inflammatory language are strictly forbidden.
Focus on constructive criticism and helpful discussions.

Stay on Topic:
Comments must directly connect to the coding concepts or blog post subject matter.
Off-topic content is prohibited.

Accuracy Matters:
Sharing misinformation or unsubstantiated coding solutions is forbidden.
Back up claims with references or code examples whenever possible.

Privacy is Paramount:
Disclosing private information about yourself or others is strictly forbidden.

By participating, you agree to these terms.
"""


def is_approved(client: OpenAI, input: CommentInput) -> bool:

    messages = [
        {
            'role': 'system',
            'content': policy,
        },
        {
            'role': 'system',
            'content': "Can this comment be approved based on the Python Playground Policy? Reply with 'yes' or 'no' only.",
        },
        {
            'role': 'user',
            'content': input.content,
        }
    ]

    response = client.chat.completions.create(model='gpt-4-turbo-preview', messages=messages)
    return response.choices[0].message.content.lower().startswith('yes')


def get_violation_reason(client: OpenAI, input: CommentInput) -> str:

    messages = [
        {
            'role': 'system',
            'content': policy,
        },
        {
            'role': 'system',
            'content': "Explain why this comment violates the Python Playground Policy. Reply in one short sentence.",
        },
        {
            'role': 'user',
            'content': input.content,
        }
    ]

    response = client.chat.completions.create(model='gpt-4-turbo-preview', messages=messages)
    return response.choices[0].message.content
