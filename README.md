# MovieAssistant

MovieAssistant is a personal movie recommendation app powered by AI, designed to recommend a movie based on your profile and objectives.

## Features

- **Personal Profile Management:**  
  Fill out a form with your name, age, nationality, gender, movie enthusiasm level, and preferred movie types. Your profile is securely stored and can be updated anytime.

- **AI-Powered Recommendations:**  
  Ask for movie recommendations or share your viewing goals. The app uses a two-stage AI process:
  1. An LLM (Llama 3.2 1b) picks a movie that fits your profile and request.
  2. The app fetches real details from Wikipedia about the suggested movie.
  3. A second LLM crafts a personalized response, combining these facts and your profile.

- **Interactive UI:**  
  Built with [Streamlit](https://streamlit.io/), for easy-to-use forms.

- **Database Integration:**  
  User profiles and personal data are stored using a database (AstraDB via `astrapy`), ensuring persistent and secure data handling.

## How It Works

1. **Start the App:**  
   Launch the app using Streamlit.

2. **Fill Your Profile:**  
   Enter personal details and movie preferences—these are used to tailor future recommendations.

3. **Ask for Suggestions:**  
   Type a question or state your movie-watching goal in the AI section (e.g., "I want to watch a sci-fi film with strong female leads").

4. **Receive Recommendations:**  
   The AI analyzes your profile and request, finds a suitable movie, retrieves accurate info from Wikipedia, and responds in a friendly, personalized way.

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dantas-a/MovieAssistant.git
   cd MovieAssistant
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up the AstraDB endpoint and Token:**

4. **Run the app:**
   ```bash
   streamlit run main.py
    ```

## Project Structure

- `main.py` – Streamlit UI and session management
- `profiles.py` – Profile creation and retrieval logic
- `form_submit.py` – Profile update logic
- `ai.py` – AI recommendation flow (integrates Langflow and Wikipedia API)
- `db.py` – Database connection and setup

## Requirements

- Python 3.12
- Streamlit
- AstraDB (via astrapy)
- Langflow
- Wikipedia API access

## Exemples



---

Enjoy discovering movies tailored just for you!
