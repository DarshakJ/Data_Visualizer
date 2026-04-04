from google.adk.agents.callback_context import CallbackContext
database_name = "SQLITE"
final_json_format = {"output":"output", "graph_type": "suitable visualization for representing the data line, area, bar, pie","title": "<what could be title of graph>"}


def dynamic_instruction_provider(context: CallbackContext):
    sql_schema = context.state.get('sql_schema', '')
    table = context.state.get('table', '')
    # print('sql_schema',sql_schema,'table',table)
    instruction = f"Strict: 'Only provide sql query no extra text'.Generate an sql query based on user requirements use schema {sql_schema} and table as {table}. Check the columns before generating the query. Query should support {database_name} Database and output column should have headers and keep query simple. "
    print("Instruction :  ",instruction)
    return instruction


def formatter_instruction_provide(callback_context: CallbackContext):
    final_df = callback_context.state.get('final_df',"")
    instruction=f"Strict : NO SQL QUERY as Output only dict mentioned .Write following as json output = {str(final_df)}, graph_type = (choose between line, area, bar, pie), title= title for graph No sql query as output example: {str(final_json_format)}"
    print("instruction",instruction)
    return instruction