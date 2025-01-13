import requests

# Function to analyze key phrases using Azure Text Analytics
def analyze_key_phrases(game_idea, text_analytics_endpoint, text_analytics_key):
    path = "text/analytics/v3.1/keyPhrases"
    url = f"{text_analytics_endpoint}/{path}"
    headers = {
        "Ocp-Apim-Subscription-Key": text_analytics_key,
        "Content-Type": "application/json"
    }
    document = {
        "documents": [
            {"id": "1", "language": "en", "text": game_idea}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=document)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Connection Error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected Error: {e}"}

# Function to analyze project cost using Azure OpenAI
def analyze_project_cost(project_details, openai_endpoint, openai_key, deployment_name="gpt-35-turbo"):
    headers = {
        "Content-Type": "application/json",
        "api-key": openai_key
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in game development project budgeting. Provide a detailed cost breakdown for game development based on the provided project details."
            },
            {
                "role": "user",
                "content": project_details
            }
        ],
        "max_tokens": 200,
        "temperature": 0.7
    }

    url = f"{openai_endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2024-08-01-preview"

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Connection Error: Could not connect to OpenAI endpoint. Details: {e}"
    except KeyError as e:
        return f"Response Parsing Error: {e}. Ensure the OpenAI response format is correct."
    except Exception as e:
        return f"Unexpected Error: {e}"

# Function to analyze game idea using Azure OpenAI
def analyze_game_idea(game_idea, openai_endpoint, openai_key, deployment_name="gpt-35-turbo"):
    headers = {
        "Content-Type": "application/json",
        "api-key": openai_key
    }
    data = {
        "messages": [
            {
                "role": "system",
                "content": "You are an expert in game design. For the given game idea, generate the following details:\n1. A unique name for the game.\n2. Suggested gameplay phases and stages.\n3. Player roles and design suggestions.\n4. Whether the game should be 2D or 3D and why.\n5. Potential improvements and features for better engagement."
            },
            {
                "role": "user",
                "content": game_idea
            }
        ],
        "max_tokens": 300,
        "temperature": 0.7
    }

    url = f"{openai_endpoint}/openai/deployments/{deployment_name}/chat/completions?api-version=2024-08-01-preview"

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Connection Error: Could not connect to OpenAI endpoint. Details: {e}"
    except KeyError as e:
        return f"Response Parsing Error: {e}. Ensure the OpenAI response format is correct."
    except Exception as e:
        return f"Unexpected Error: {e}"
import requests

def analyze_animation_suggestions(details):
    # Logic to analyze animation suggestions using OpenAI or other tools
    return "Suggest using Unity Animator for smooth transitions and Unreal Engine Sequencer for cinematic animations."

def generate_character_images(details):
    # Logic to generate AI-based images for character designs
    # Replace with actual AI integration or a placeholder URL
    return "https://via.placeholder.com/400"

def suggest_gameplay_code(details):
    # Logic to suggest gameplay-related code snippets
    return """// Example Unity C# Script for Character Movement
void Update() {
    float move = Input.GetAxis("Horizontal");
    transform.position += new Vector3(move, 0, 0) * speed * Time.deltaTime;
}"""
