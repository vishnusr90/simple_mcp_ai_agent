from tools.tools import calculator_tool
from context.mcp_context import MCPContext

def fake_llm_response(context: dict, user_input: str):
    if "calculate" in user_input.lower():
        expression = user_input.lower().replace("calculate", "").strip()
        return f"[tool:calculator] {calculator_tool(expression)}"
    
    return f"I have received user input: {user_input}"

def run_agent():
    mcp = MCPContext(system_prompt = "You are a helpful AI assistent")

    print("AI agent is ready. Type 'exit' to quit")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit"]:
            break

        mcp.add_user_message(user_input)
        context = mcp.get_context()
        response = fake_llm_response(context, user_input)
        mcp.add_ai_reponse(response)
        print(f"AI: {response}")


if __name__ == "__main__":
    run_agent()