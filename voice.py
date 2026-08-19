import os
import random 
import socket 
import speech_recognition as sr
import pyttsx3
import webbrowser
import psutil
from datetime import datetime

# =========================
# VOICE SETUP
# =========================

listener = sr.Recognizer()

engine = pyttsx3.init()

# =========================
# BROWSER SETUP
# =========================

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

try:
    browser = webbrowser.get(chrome_path)

except:
    browser = webbrowser

# =========================
# WAKE WORDS
# =========================

WAKE_WORDS = [
    "nadhu",
    "nandhu",
    "nandu",
    "nadhoo"
]

# =========================
# TALK FUNCTION
# =========================

def talk(text):

    print("Nadhu:", text)

    engine.stop()

    engine.say(text)

    engine.runAndWait()

# =========================
# NORMALIZE COMMAND
# =========================

def normalize_command(command):

    command = command.lower()

    # remove wake words
    for word in WAKE_WORDS:

        command = command.replace(
            word,
            ""
        )

    # roadmap fixes
    command = command.replace(
        "road map",
        "roadmap"
    )

    command = command.replace(
        "road-map",
        "roadmap"
    )

    return " ".join(
        command.split()
    )
def should_handle(command):
    """Check whether Nadhu should respond to the command."""

    command = command.lower()

    if any(word in command for word in WAKE_WORDS):
        return True

    keywords = [
        "youtube",
        "chatgpt",
        "whatsapp",
        "linkedin",
        "chrome",
        "browser",
        "time",
        "date",
        "day",
        "search",
        "roadmap",
        "notepad",
        "calculator",
        "vscode",
        "vs code",
        "battery",
        "internet",
        "motivate me",
        "python question",
        "dsa question",
        "stop",
        "exit"
    ]

    return any(keyword in command for keyword in keywords)


# =========================
# HANDLE COMMANDS
# =========================

def handle_command(command):

    command = normalize_command(
        command
    )

    print(
        "Normalized:",
        command
    )

    # =====================
    # OPEN APPS / WEBSITES
    # =====================

    if "youtube" in command:

        talk(
            "Opening YouTube"
        )

        browser.open(
            "https://youtube.com"
        )

    elif ("chatgpt" in command or
          "chat gpt" in command):

        talk(
            "Opening ChatGPT"
        )

        browser.open(
            "https://chatgpt.com"
        )

    elif ("whatsapp" in command or
          "what app" in command):

        talk(
            "Opening WhatsApp"
        )

        browser.open(
            "https://web.whatsapp.com"
        )

    elif ("linkedin" in command or
          "linked in" in command):

        talk(
            "Opening LinkedIn"
        )

        browser.open(
            "https://linkedin.com"
        )

    elif ("chrome" in command or
          "browser" in command):

        talk(
            "Opening Browser"
        )

        browser.open(
            "https://google.com"
        )

    # =====================
    # TIME / DATE / DAY
    # =====================

    elif "time" in command:

        current = datetime.now().strftime(
            "%I:%M %p"
        )

        talk(
            "Current time is " + current
        )

    elif "date" in command:

        today = datetime.now().strftime(
            "%d %B %Y"
        )

        talk(
            "Today's date is " + today
        )

    elif "day" in command:

        day = datetime.now().strftime(
            "%A"
        )

        talk(
            "Today is " + day
        )

    # =====================
    # GOOGLE SEARCH
    # =====================

    elif "search" in command:

        item = command.replace(
            "search",
            ""
        ).strip()

        if item:

            talk(
                "Searching " + item
            )

            browser.open(
                "https://www.google.com/search?q="
                + item
            )

        else:

            talk(
                "Please tell me what to search"
            )

    # =====================
    # ROADMAPS
    # =====================

    elif "python" in command and "roadmap" in command:

        talk(
            "Opening Python roadmap"
        )

        browser.open(
            "https://roadmap.sh/python"
        )

    elif "dsa" in command and "roadmap" in command:

        talk(
            "Opening DSA roadmap"
        )

        browser.open(
            "https://roadmap.sh/datastructures-and-algorithms"
        )

    elif "sql" in command and "roadmap" in command:

        talk(
            "Opening SQL roadmap"
        )

        browser.open(
            "https://roadmap.sh/sql"
        )

    elif "llm" in command and "roadmap" in command:

        talk(
            "Opening LLM roadmap"
        )

        browser.open(
            "https://roadmap.sh/ai-data-scientist"
        )

    elif ("gen ai" in command or
          "generative ai" in command) and "roadmap" in command:

        talk(
            "Opening Generative AI roadmap"
        )

        browser.open(
            "https://roadmap.sh/ai-engineer"
        )

    elif "data science" in command and "roadmap" in command:

        talk(
            "Opening Data Science roadmap"
        )

        browser.open(
            "https://roadmap.sh/ai-data-scientist"
        )

    elif ("machine learning" in command or
          "ml" in command) and "roadmap" in command:

        talk(
            "Opening Machine Learning roadmap"
        )

        browser.open(
            "https://roadmap.sh/ai-data-scientist"
        )

    elif "deep learning" in command and "roadmap" in command:

        talk(
            "Opening Deep Learning roadmap"
        )

        browser.open(
            "https://roadmap.sh/ai-data-scientist"
        )

    elif ("web development" in command or
          "web dev" in command) and "roadmap" in command:

        talk(
            "Opening Web Development roadmap"
        )

        browser.open(
            "https://roadmap.sh/full-stack"
        )

    elif ("prompt engineering" in command or
          "prompt" in command) and "roadmap" in command:

        talk(
            "Opening Prompt Engineering roadmap"
        )

        browser.open(
            "https://roadmap.sh/prompt-engineering"
        )

    elif "system design" in command and "roadmap" in command:

        talk(
            "Opening System Design roadmap"
        )

        browser.open(
            "https://roadmap.sh/system-design"
        )
    # =====================
    # NOTEPAD
    # =====================

    elif "notepad" in command:

        talk("Opening Notepad")

        os.system("notepad")

    # =====================
    # CALCULATOR
    # =====================

    elif "calculator" in command:

        talk("Opening Calculator")

        os.system("calc")

    # =====================
    # VS CODE
    # =====================

    elif "vscode" in command or "vs code" in command:

        talk("Opening VS Code")

        os.system("code")

    # =====================
    # BATTERY STATUS
    # =====================

    elif "battery" in command:

        battery = psutil.sensors_battery()

        if battery:

            talk(
                f"Battery is {battery.percent} percent"
            )

        else:

            talk(
                "Battery information not available"
            )

    # =====================
    # INTERNET STATUS
    # =====================

    elif "internet" in command:

        try:

            socket.create_connection(
                ("8.8.8.8", 53),
                timeout=3
            )

            talk(
                "Internet is connected"
            )

        except:

            talk(
                "Internet is not connected"
            )

    # =====================
    # MOTIVATION QUOTES
    # =====================

    elif "motivate me" in command:

        quotes = [

            "Success comes from consistency",

            "Keep learning every day",

            "Small progress is still progress",

            "Never stop improving yourself",

            "Dream big and work hard"

        ]

        talk(
            random.choice(quotes)
        )

    # =====================
    # PYTHON QUESTIONS
    # =====================

    elif "python question" in command:

        questions = [

            "What is a list in Python",

            "What is a dictionary in Python",

            "What is a function",

            "What is a tuple",

            "What is list comprehension"
    
        ]

        talk(
            random.choice(questions)
        )

    # =====================
    # DSA QUESTIONS
    # =====================

    elif "dsa question" in command:

        questions = [

            "What is Stack",

            "What is Queue",

            "What is Array",

            "What is Binary Search",

            "What is Recursion"

        ]

        talk(
            random.choice(questions)
        )
    # =====================
    # EXIT
    # =====================

    elif "stop" in command or "exit" in command:

        talk(
            "Goodbye Naga Devi"
        )

        return False

    else:

        talk(
            "Sorry I did not understand"
        )

    return True
# =========================
# START ASSISTANT
# =========================

def run_assistant():

    talk(
        "Hello Naga Devi. Nadhu is ready"
    )

    while True:

        try:

            listener = sr.Recognizer()

            with sr.Microphone() as source:

                print(
                    "Listening..."
                )

                listener.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                voice = listener.listen(
                    source,
                    timeout=None,
                    phrase_time_limit=None
                )

            command = listener.recognize_google(
                voice,
                language="en-IN"
            ).lower()

            print(
                "You said:",
                command
            )

            if should_handle(command):

                keep_running = handle_command(
                    command
                )

                if keep_running is False:
                    break

        except sr.WaitTimeoutError:

            print(
                "No speech detected"
            )

        except sr.UnknownValueError:

            print(
                "Could not understand audio"
            )

        except sr.RequestError as e:

            print(
                "Speech service error:",
                e
            )

        except KeyboardInterrupt:

            talk(
                "Goodbye Naga Devi"
            )

            break

        except Exception as e:

            print(
                "Unexpected error:",
                e
            )


if __name__ == "__main__":
    run_assistant()
