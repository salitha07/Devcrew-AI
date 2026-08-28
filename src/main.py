import json
from pathlib import Path


OUTPUT_FILE = Path("outputs/requirement_analysis.json")


def get_project_idea():
    while True:
        idea = input("Enter your software project idea: ").strip()

        if idea:
            return idea

        print("Project idea cannot be empty. Please try again.")


def create_analysis(idea):
    analysis = {
        "project_summary": idea,
        "user_roles": [],
        "functional_requirements": [],
        "non_functional_requirements": [],
        "constraints": [],
        "clarifying_questions": [
            "Who are the main users?",
            "What is the main problem this system should solve?"
        ]
    }

    return analysis


def save_analysis(analysis):
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(analysis, file, indent=2, ensure_ascii=False)


def main():
    project_idea = get_project_idea()
    result = create_analysis(project_idea)

    print("\nRequirement Analysis:")
    print(json.dumps(result, indent=2, ensure_ascii=False))

    save_analysis(result)
    print(f"\nAnalysis saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()