from google.adk.agents.callback_context import CallbackContext
from .sqlite_handler import EmployeeDB
import re

async def get_schema_callback(callback_context: CallbackContext):
    emp_db = EmployeeDB()
    schema = emp_db.get_schema()
    callback_context.state['sql_schema'] = str(schema)
    callback_context.state['table'] = str(emp_db.table_name)
    print("callback_context.state['sql_schema']",callback_context.state['sql_schema'])
    print("callback_context.state['table']",callback_context.state['table'])
    return None





async def execute_query_callback(
    callback_context: CallbackContext, 
   
):
    # In v1.28.1, response text is accessed via candidates
  
        
    # Store it in the session state
    # Save the result to state so the next agent can see it
    print("query llm : ",callback_context.state['llm_sql_query'])
    sql_query = str(callback_context.state['llm_sql_query'])
    clean_sql = re.sub(r"```sql|```", "", sql_query).strip()
    callback_context.state['sql_query'] = clean_sql
    emp_db = EmployeeDB()
    output = emp_db.read_custom(clean_sql)
    callback_context.state['final_df'] = output.to_dict(orient='list')
    print(f"✅ Saved to Session State: {callback_context.state['final_df']}...datatype {type(output)}")
        
    return None