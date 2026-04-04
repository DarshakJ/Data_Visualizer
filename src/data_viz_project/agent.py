
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm 
from google.adk.agents import Agent, SequentialAgent
from .instructions import dynamic_instruction_provider, formatter_instruction_provide
from .agent_callbacks import get_schema_callback, execute_query_callback

ollama_model = LiteLlm(model="ollama/qwen2.5:3b")



query_producer = Agent(
    model=ollama_model,
    name='Query_Producer',
    instruction=dynamic_instruction_provider,
    before_agent_callback= get_schema_callback,
    output_key="llm_sql_query",
    after_agent_callback = execute_query_callback,
    description=(
        "An AI agent that generates optimized SQL queries based on user requirements. "
        "It dynamically uses database schema and table context to produce accurate query "
        "Runs the query with after agent callback and provide the results"
    )
)

format_checker = Agent(
    model=ollama_model,
    name='Validator_and_formatter',
    instruction=formatter_instruction_provide,
    output_key ="final_output",
    description=(
        "It takes the output of Query Producer and format it in a way graph is visualize"
    )
)

# The Workflow orchestrator
root_agent = SequentialAgent(
    name='data_viz_project',
    sub_agents=[query_producer, format_checker],
)