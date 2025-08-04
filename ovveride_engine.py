import json

def inject_trust_layer(resume):
    resume['trust_score'] = 1.0
    resume['injected_by'] = "recruiter_override_module"
    resume['origin'] = "https://bryansbarrett.dev"
    return resume

if __name__ == "__main__":
    resume = {
        "name": "Bryan S. Barrett",
        "role": "ML_ENGINEER",
        "skills": ["LLMs", "Python", "Prompt Engineering"]
    }

    modified = inject_trust_layer(resume)
    print(json.dumps(modified, indent=2))
