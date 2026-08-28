from pydantic import BaseModel


class RequirementAnalysis(BaseModel):
    project_summary: str
    user_roles: list[str]
    functional_requirements: list[str]
    non_functional_requirements: list[str]
    constraints: list[str]
    clarifying_questions: list[str]