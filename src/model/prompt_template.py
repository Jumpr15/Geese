def build_prompt_template(system_prompt: str, tool_list: list):
     string_tool_list = []
     for tool in tool_list:
          string_tool_list.append(f"""\n"tool_name": {tool["tool_name"]},\n"parameter_list": {tool["parameter_list"]}\n""")
     
     system_message = "System Prompt: " + system_prompt + """\n
Calling Tools Procedure:
### IMPORTANT <Tool_Call> and </Tool_Call> must be called in this exact spelling and capitalisation

<Tool_Call>
{
     "tool_name": tool name to call,
     "parameters": {
          key pair values of parameter and parameter values for all parameters in parameter_list
     }
}
</Tool_Call>

Tool Calls Available:
""" + '\n'.join(string_tool_list)

     return system_message