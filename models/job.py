from dataclasses import dataclass
from typing import List

@dataclass
class Job:
    id: int
    title: str
    company: str
    location: str
    description: str
    requirements: List[str]
    skills_required: List[str]

class JobRepository:
    _jobs = [
        Job(
            id=1,
            title="Cloud Solutions Architect",
            company="TechCorp",
            location="Remote",
            description="Design and implement cloud solutions for enterprise clients",
            requirements=[
                "5+ years of experience in cloud architecture",
                "AWS/Azure certification",
                "Experience with microservices"
            ],
            skills_required=["AWS", "Azure", "Kubernetes", "Microservices"]
        ),
        Job(
            id=2,
            title="DevOps Engineer",
            company="InnovateHub",
            location="New York, NY",
            description="Implement and maintain CI/CD pipelines",
            requirements=[
                "3+ years of DevOps experience",
                "Strong Linux knowledge",
                "Experience with containerization"
            ],
            skills_required=["Docker", "Kubernetes", "Jenkins", "Linux"]
        )
    ]

    @classmethod
    def get_all(cls) -> List[Job]:
        return cls._jobs

    @classmethod
    def get_by_id(cls, job_id: int) -> Job:
        return next((j for j in cls._jobs if j.id == job_id), None)

    @classmethod
    def search_by_skills(cls, skills: List[str]) -> List[Job]:
        return [
            job for job in cls._jobs
            if any(skill.lower() in [s.lower() for s in job.skills_required]
                  for skill in skills)
        ]