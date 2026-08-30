import json

from llama_cpp import Llama

llm = Llama(
    model_path="model2_retention_0.5bv2.gguf",
    n_ctx=2048,
    n_threads=4,
    verbose=False,
)

test_input_i =  {"role":"user","content":{"analysis_type":"individual","customer_data":{"profile":{"age":36,"customer_segment":"salary","customer_yearly_value":1160},"financial_activity_30d_trend":{"balance_change":-22.97,"external_transfer_change":23.72,"fd_maturing_in_30d":"No"},"friction_signals":{"app_login_change":-10,"complaints_30d":5,"failed_transactions_30d":3,"recent_complaint_text":"Unfair hidden charges deducted from my account."}},"churn_probability":0.88}}

test_input_c ={"role":"user","content":{"analysis_type":"cluster","cluster_metadata":{"cluster_id":"C_118","cluster_size":119},"aggregated_data":{"dominant_profile":{"avg_age":45,"customer_segment":"wealth"},"friction_signals":{"avg_complaints_30d":0.2,"avg_failed_transactions_30d":1.1,"common_complaint_themes":[]}},"average_churn_probability":0.652}}

message = {"role":"system","content":"You are a banking retention AI. Analyze the customer data and output strict JSON containing 'why' and 'next_actions' as an object mapping each recommendation to an explanation. 'Why' should contain the appropriate reasoning for churn risk and 'next_actions' should contain a list of recommended actions to retain the customer. Do not include any other text or explanation outside of the JSON object. Do not include next_actions in why and vice versa."}

output = llm.create_chat_completion(
    messages=[
        message,
        {"role": "user", "content": json.dumps(test_input_i)}
    ],
    response_format={
        "type": "json_object",
        "schema": {
            "type": "object",
            "properties": {
                "why": {"type": "array", "items": {"type": "string"}},
                "next_actions": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["why", "next_actions"],
        },
    },
    temperature=0.3
)
response = output["choices"][0]["message"]["content"]

try:
    result = json.loads(response)
    print("Why:", result.get("why", "Not provided"))
    print("Next actions:")
    for action in result.get("next_actions", []):
        print(f"- {action}")
except json.JSONDecodeError:
    print(response)