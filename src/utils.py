import requests
import json,re
import uuid

def generate_unique_id():
    return str(uuid.uuid4())

BASE_URL = "http://localhost:8000"


def extract_json(text):
    # Find JSON inside triple backticks (```json ... ```)
    match = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    
    if match:
        json_str = match.group(1)
        return json.loads(json_str)
    
    # Fallback: try to find any JSON-like structure
    match = re.search(r"(\{.*\})", text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    
    return None

def ensure_session(agent_id, user_id, session_id):
    """Creates the session if it doesn't already exist."""
    session_url = f"{BASE_URL}/apps/{agent_id}/users/{user_id}/sessions/{session_id}"
    
    # Try to GET the session first
    check = requests.get(session_url)
    if check.status_code == 200:
        return True # Session exists
    
    # If not found (404), create it
    if check.status_code == 404:
        print(f"Initializing new session: {session_id}...")
        # POST to the same URL creates the session
        # You can optionally pass an initial 'state' dict in the json body
        create = requests.post(session_url, json={})
        return create.status_code in [200, 201]
    
    return False

def call_adk_agent(query, agent_id="data_viz_project"):
    user_id = "user_default"
    session_id = generate_unique_id()

    # CRITICAL: Ensure the session is initialized first
    if not ensure_session(agent_id, user_id, session_id):
        return "Error: Could not initialize ADK session."

    # Now perform the run
    run_url = f"{BASE_URL}/run"
    payload = {
        "app_name": agent_id,
        "user_id": user_id,
        "session_id": session_id,
        "new_message": {
            "role": "user",
            "parts": [
                {
                    "text": query
                }
            ]
        }
    }

    response = requests.post(run_url, json=payload)
    print(response)
    
    if response.status_code == 200:
        events = response.json()
        events_data = events
        return extract_json(events[-1]["content"]["parts"][0]["text"])
        
    else:
        return f"Error: {response.status_code} - {response.text}"

# Example Usage

# print(f"Agent: {result}")