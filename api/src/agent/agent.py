from pydantic_ai import Agent

from src.config import Env


def init_agent(env: Env):
    agent = Agent(
        model=env.llmmodel_small, system_prompt="Write only in rythm and rhyme. "
    )
    return agent
