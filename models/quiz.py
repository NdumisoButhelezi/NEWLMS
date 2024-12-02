from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Quiz:
    id: int
    course_id: int
    title: str
    questions: List[Dict]

class QuizRepository:
    _quizzes = [
        Quiz(
            id=1,
            course_id=1,
            title="Cloud Computing Basics",
            questions=[
                {
                    "id": 1,
                    "question": "What is cloud computing?",
                    "options": [
                        "A type of weather system",
                        "Internet-based computing services",
                        "A local storage system",
                        "A type of database"
                    ],
                    "correct_answer": 1
                },
                {
                    "id": 2,
                    "question": "What is IaaS?",
                    "options": [
                        "Infrastructure as a Service",
                        "Internet as a Service",
                        "Integration as a Service",
                        "Information as a Service"
                    ],
                    "correct_answer": 0
                }
            ]
        ),
        Quiz(
            id=2,
            course_id=2,
            title="DevOps Fundamentals",
            questions=[
                {
                    "id": 1,
                    "question": "What is Docker?",
                    "options": [
                        "A programming language",
                        "A containerization platform",
                        "A cloud provider",
                        "A database system"
                    ],
                    "correct_answer": 1
                }
            ]
        )
    ]

    @classmethod
    def get_by_course_id(cls, course_id: int) -> Quiz:
        return next((q for q in cls._quizzes if q.course_id == course_id), None)

    @classmethod
    def get_by_id(cls, quiz_id: int) -> Quiz:
        return next((q for q in cls._quizzes if q.id == quiz_id), None)