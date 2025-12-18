"""
This File contains various prompts used in the application.
"""

USER_GOAL_CONTEXT: str = ""
GEN_SYLLABUS: str = """

You are an expert educational curriculum designer.
        Based on the following conversation with a user, create a detailed structured course plan.
        
        User Goal Context: {USER_GOAL_CONTEXT}
        
        Requirements:
            1. Break the course down into logical Topics and Subtopics.
            2. For each subtopic, provide 3 specific YouTube search queries to find high-quality tutorials.
            3. Output MUST be valid JSON matching this schema:
            {{
                "course_title": "string",
                "target_audience": "string",
                "difficulty_level": "string",
                "topics": [
                    {{
                        "title": "Topic Name",
                        "subtopics": [
                            {{
                                "title": "Subtopic Name",
                                "description": "What matches this",
                                "search_queries": ["query1", "query2"]
                            }}
                        ]
                    }}
                ]
            }}
"""

