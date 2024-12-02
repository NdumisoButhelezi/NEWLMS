from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Course:
    id: int
    title: str
    description: str
    duration: str
    skills: List[str]
    prerequisites: List[str]
    modules: List[Dict]

class CourseRepository:
    _courses = [
        Course(
            id=1,
            title="Cloud Computing Fundamentals",
            description="Learn the basics of cloud computing and cloud service models.",
            duration="8 weeks",
            skills=["Cloud Computing", "AWS", "Azure", "GCP"],
            prerequisites=["Basic IT knowledge"],
            modules=[
                {"title": "Introduction to Cloud", "duration": "1 week"},
                {"title": "Cloud Service Models", "duration": "2 weeks"},
                {"title": "Cloud Security", "duration": "2 weeks"},
                {"title": "Cloud Architecture", "duration": "3 weeks"}
            ]
        ),
        Course(
            id=2,
            title="DevOps Engineering",
            description="Master DevOps practices and tools.",
            duration="10 weeks",
            skills=["DevOps", "CI/CD", "Docker", "Kubernetes"],
            prerequisites=["Basic Linux", "Programming basics"],
            modules=[
                {"title": "DevOps Introduction", "duration": "1 week"},
                {"title": "Containerization", "duration": "3 weeks"},
                {"title": "CI/CD Pipelines", "duration": "3 weeks"},
                {"title": "Monitoring and Logging", "duration": "3 weeks"}
            ]
        )
    ]

    @classmethod
    def get_all(cls) -> List[Course]:
        return cls._courses

    @classmethod
    def get_by_id(cls, course_id: int) -> Course:
        return next((c for c in cls._courses if c.id == course_id), None)