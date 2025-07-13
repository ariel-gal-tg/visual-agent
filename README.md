Visual Agent MVP

This project is an MVP (Minimum Viable Product) for a visual agent that can understand and interact with your computer's graphical user interface (GUI).

## Core Functionality

- Takes a screenshot of your primary display.
- Uses Google Gemini Vision to:
  1. Describe exactly what is visible on your screen (windows, icons, text, etc.).
  2. Prints the screen resolution (width x height in pixels).
  3. Prompts you to specify an element you want to click (e.g., "Save button").
  4. Asks Gemini to return the (x, y) coordinates of the center of that element on the screenshot.
  5. Prints those coordinates for you to use (future versions may automate the click).

## Getting Started

Follow these instructions to get the project running on your local machine.

### Prerequisites
- Python 3.9+
- Git
### Installation

Clone the repository:

```
git clone <your-repo-url>
cd visual-agent
```

Create and activate a Python virtual environment:

```
# Create the environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
.\venv\Scripts\activate
```

Install the required dependencies:

```
pip install -r requirements.txt
```

Set up your API Key:

- Get a free Google AI API Key from Google AI Studio.
- Create a file named `.env` in the root of the project.
- Add your API key to the `.env` file like this:

```
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

## Usage

To run the agent, simply execute the main.py script from your terminal:

```
python main.py
```

The script will:
1. Take a screenshot.
2. Print a detailed description of what it sees.
3. Print your screen resolution.
4. Ask you what you want to click on.
5. Ask Gemini for the coordinates of that element and print them.

## Project Roadmap (Future Plans)

This MVP is the foundation. The next steps are to build upon this vision capability to enable action:

- [ ] Mouse Control: Move the mouse and click on the coordinates returned by Gemini.
- [ ] Keyboard Control: Type text or press keys.
- [ ] Complex Prompting: Ask the model for the next best action or for specific coordinates of UI elements.
- [ ] Continuous Operation Loop: See, think, and act in a loop.
- [ ] Explore Local Models: Run open-source vision models locally for offline use.