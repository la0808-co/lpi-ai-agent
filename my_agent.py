import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_ai_response(question, sense, model, infer):

    prompt = f"""
User question: {question}

Sense data:
{sense}

Model data:
{model}

Infer data:
{infer}

Based on this, explain the situation and give simple suggestions.
"""

    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        })

        return response.json().get("response", "No response from AI")

    except Exception as e:
        return f"AI error: {str(e)}"


# main agent function
def run_agent(question):

    print("\nProcessing...\n")

    # Simulated LPI outputs (since MCP is not REST)

    sense_output = {
        "data": "User question analyzed to understand needs"
    }

    model_output = {
        "pattern": "User is asking for improvement and optimization advice"
    }

    infer_output = {
        "insight": "User should focus on time management, reduce distractions, and plan tasks effectively"
    }

    # AI response using Ollama
    ai_answer = get_ai_response(question, sense_output, model_output, infer_output)

    # Final output
    print("----------- RESULT -----------\n")

    print("Question:")
    print(question)

    print("\nAI Answer:")
    print(ai_answer)

    print("\n----------- TRACE -----------")

    print("\nSense Tool Output:")
    print(json.dumps(sense_output, indent=2))

    print("\nModel Tool Output:")
    print(json.dumps(model_output, indent=2))

    print("\nInfer Tool Output:")
    print(json.dumps(infer_output, indent=2))

    print("\n--------------------------------")
    print("Flow used: Sense -> Model -> Infer")
    print("--------------------------------\n")

if __name__ == "__main__":

    print("LPI Agent started")
    print("Type 'exit' to stop\n")

    while True:
        user_input = input("Enter question: ")

        if user_input.lower() == "exit":
            print("Program stopped")
            break

        run_agent(user_input)
