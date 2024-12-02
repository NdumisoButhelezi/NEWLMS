from typing import List, Dict

class AIService:
    @staticmethod
    def generate_cv_content(name: str, skills: List[str]) -> Dict:
        """Generate CV content using simulated AI."""
        return {
            'name': name,
            'skills': skills,
            'generated_sections': {
                'professional_summary': f"Experienced professional with expertise in {', '.join(skills)}",
                'career_objectives': "Seeking opportunities to leverage technical skills in a dynamic environment",
                'recommendations': "Consider adding cloud computing certifications to enhance your profile"
            }
        }

    @staticmethod
    def get_job_recommendations(skills: List[str]) -> List[Dict]:
        """Generate job recommendations based on skills."""
        return [
            {
                'title': 'Cloud Solutions Architect',
                'skills_matched': [skill for skill in skills if 'cloud' in skill.lower()],
                'confidence_score': 0.85,
                'requirements': ['Cloud certification', 'System design experience']
            },
            {
                'title': 'DevOps Engineer',
                'skills_matched': [skill for skill in skills if 'devops' in skill.lower()],
                'confidence_score': 0.78,
                'requirements': ['CI/CD experience', 'Container orchestration']
            }
        ]