from src.config import *


def get_langfuse(request):
    return request.app.state.langfuse


def get_env(request):
    return request.app.state.env


def get_pb(request):
    return request.app.state.pb


def get_agent(request):
    return request.app.state.agent
