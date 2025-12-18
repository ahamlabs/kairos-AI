from ytsearch import YtSearch
from geminiServices import GeminiService
import asyncio

async def main():
    user_goal_context: str = input("Enter the user goal context: ")
    gemini_service = GeminiService(user_goal_context)
    gemini_service.run()
    user_id = gemini_service.user_id()
    yt_search = YtSearch(user_id)
    yt_search.run()

if __name__ == "__main__":
    asyncio.run(main())
