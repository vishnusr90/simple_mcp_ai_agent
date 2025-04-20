
from tools.tools import calculator_tool

class MCPContext:
    def __init__(self, system_prompt):
        self.system = system_prompt
        self.messages = []
        self.memory = []
        self.tools = {
            "calculator": {
                "function": calculator_tool,
                "description": "Performs basic math operations"
            }
        }

    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "content": message
        })
        self.memory.append(message)

    def add_ai_reponse(self, message):
        self.messages.append({
            "role": "assistant",
            "content": message
        })
        self.memory.append(message)

    def get_context(self):
        return {
            "system": self.system,
            "messages": self.messages,
            "tools": self.tools,
            "memory": self.memory[-5:]
        }
    
    def call_tool(self, tool_name, expression):
        if tool_name in self.tools:
            return self.tools[tool_name]["function"](expression)
        return "Unknown tool. We will be incorporating it soon !"