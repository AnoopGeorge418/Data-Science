from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: { "title": "Start Today", "content": "You don’t need the perfect plan. Just take the first small step today." },
    2: { "title": "Consistency Wins", "content": "Doing a little every day is more powerful than doing a lot once." },
    3: { "title": "Keep Learning", "content": "Learn one new skill or idea daily. Growth compounds over time." },
    4: { "title": "Future You", "content": "Your future is built by the actions you take right now." },
    5: { "title": "Progress Over Perfection", "content": "Don’t wait for perfect. Improve step by step." },
    6: { "title": "Dream Big", "content": "Big dreams push you to take big actions." },
    7: { "title": "Mistakes Matter", "content": "Every mistake teaches a lesson you can’t learn from success." },
    8: { "title": "Discipline", "content": "Discipline today creates freedom tomorrow." },
    9: { "title": "Stay Curious", "content": "Curiosity keeps your mind alive and growing." },
    10: { "title": "Take Action", "content": "Ideas are useless without action. Move now." },
    11: { "title": "Beginner Mind", "content": "Every expert once struggled as a beginner." },
    12: { "title": "Build Skills", "content": "Skills pay off for life. Invest time in learning them." },
    13: { "title": "Small Habits", "content": "Tiny daily habits lead to massive long-term change." },
    14: { "title": "Keep Going", "content": "When it feels hard, you are closer than you think." },
    15: { "title": "Mindset", "content": "Your thoughts shape your actions and your life." },
    16: { "title20": "Create More", "content": "Spend more time creating than scrolling." },
    17: { "title": "Failure = Lesson", "content": "Failure is feedback, not the final result." },
    18: { "title": "Be Better", "content": "Aim to be 1% better than yesterday." },
    19: { "title": "Focus Mode", "content": "Remove distractions and your speed will double." },
    20: { "title": "You Can", "content": "You are capable of far more than you believe." }
}

# Endpoints
@app.get('/post')
def get_all_post(limit: int = None, ):    
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

# Endpoint to get a specific post by ID
@app.get('/post/{id}')
def get_post(id: int):
    if not id in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return text_posts.get(id)

@app.post('/post')
def create_post():
    pass