from mcp.server.fastmcp import FastMCP

from src.agent import init_agent
from src.config import *

server = FastMCP("API MCP Server")

logger = get_logger(__name__)

if __name__ == "__main__":
    env = Env()
    init_logging(env)
    init_agent(env)

    logger.info("MCP Server is starting...")

    server.run()
