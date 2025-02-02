import telebot
from openai import OpenAI
import json
from telebot.async_telebot import AsyncTeleBot
import asyncio
import os
import dotenv

from smolagents import ToolCallingAgent, OpenAIServerModel, Tool
from schema import schema

# Only load .env file if it exists (local development)
if os.path.exists(".env"):
    dotenv.load_dotenv()

# Get environment variables with fallbacks
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SANITY_API_KEY = os.getenv("SANITY_API_KEY")

if not all([TELEGRAM_TOKEN, OPENAI_API_KEY, SANITY_API_KEY]):
    raise ValueError(
        "Missing required environment variables. Please check your configuration."
    )

available_categories = [
    {
        "name": "shelter",
        "description": "Shelter and basic needs. Use this category to get information about shelters, basic needs, and other support services.",
    },
    {
        "name": "dentist",
        "description": "Dentist and dental care. Use this category to get information about dentists, dental care, and other support services.",
    },
    {
        "name": "doctors",
        "description": "Doctors and healthcare services. Use this category to get information about doctors, healthcare services, and other support services.",
    },
    {
        "name": "emergencyLines",
        "description": "Emergency lines. Use this category to get information about emergency services, police, and emergency support.",
    },
    {
        "name": "childrensCare",
        "description": "Childrens care. Use this category to get information about childrens care, childrens support, and other support services.",
    },
    {
        "name": "helpdesk",
        "description": "Helpdesk. Use this category to get information about helpdesk, helpdesk support, and other support services.",
    },
    {
        "name": "financialHelp",
        "description": "Financial help. Use this category to get information about financial help, financial support, and other support services.",
    },
    {
        "name": "childrensRights",
        "description": "Childrens rights. Use this category to get information about childrens rights, childrens support, and other support services.",
    },
    {
        "name": "work",
        "description": "Work. Use this category to get information about work, employment, and employment support. Also includes labour rights information and flyers",
    },
    {
        "name": "legal",
        "description": "Legal advice and support. Use this category to get information about legal advice, legal support, and other support services.",
    },
    {
        "name": "hygiene",
        "description": "Hygiene. Use this category to get information about hygiene, hygiene services, and other support services.",
    },
    {
        "name": "food",
        "description": "Food and clothing distribution. Use this category to get information about food, clothing distribution, and other support services.",
    },
    {
        "name": "medication",
        "description": "Medication. Use this category to get information about medication, healthcare services, and healthcare support.",
    },
    {
        "name": "sexualHealth",
        "description": "Sexual health. Use this category to get information about sexual health, and other support services.",
    },
    {
        "name": "emergencyPolice",
        "description": "Emergency services and police. Use this category to get information about emergency services, police, and emergency support.",
    },
    {
        "name": "whereToGo",
        "description": "Where to go first. Use this category to get information about where to go first, and other support services.",
    },
    {
        "name": "mentalWellbeing",
        "description": "Mental wellbeing. Use this category to get information about mental wellbeing, and other support services.",
    },
    {
        "name": "domesticViolence",
        "description": "Domestic violence. Use this category to get information about domestic violence, and other support services.",
    },
    {
        "name": "sexualExploitation",
        "description": "Sexual exploitation. Use this category to get information about sexual exploitation, and other support services.",
    },
    {
        "name": "criminalExploitation",
        "description": "Criminal exploitation. Use this category to get information about criminal exploitation, and other support services.",
    },
    {
        "name": "labourExploitation",
        "description": "Labour exploitation. Use this category to get information about labour exploitation like working hours, minimum wage, etc.",
    },
    {
        "name": "pregnancyCare",
        "description": "Pregnancy care. Use this category to get information about pregnancy care, pregnancy support, and other support services.",
    },
    {
        "name": "birthControlAndMenstruation",
        "description": "Birth control and menstruation. Use this category to get information about birth control and menstruation, and other support services.",
    },
    {
        "name": "organizationsThatCanHelp",
        "description": "Organizations that can help. Use this category to get information about organizations that can help, and other support services.",
    },
    {
        "name": "abortion",
        "description": "Abortion. Use this category to get information about abortion, and other support services.",
    },
    {
        "name": "firstAsylumRequest",
        "description": "First asylum request. Use this category to get information about first asylum request.",
    },
    {
        "name": "afterRejection",
        "description": "Legal advice after rejection. Use this category to get information about legal advice after rejection.",
    },
    {
        "name": "voluntaryReturn",
        "description": "Support with voluntary return. Use this category to get information about support with voluntary return.",
    },
]


class GroqQueryTool(Tool):
    name = "groq_query_tool"
    description = "This tool is used make requests to the Sanity API using Groq Query Language. Just get all the fields for each category. "

    inputs = {
        # "query": {
        #     "type": "string",
        #     "description": "The query to be executed using Groq Query Language"
        # }
        "category": {"type": "string", "description": "The category to be fetched"}
    }
    output_type = "string"

    def __init__(self, url):
        super().__init__()
        self.url = url

    def forward(self, category):
        import requests
        import json
        import os

        response = requests.get(self.url, params=category)
        params = {"query": f"*[_type == '{category}']"}  # This will fetch all documents
        # Make the GET request
        headers = {
            "Authorization": f"Bearer {os.getenv('SANITY_API_KEY')}",
            "Content-Type": "application/json",
        }
        response = requests.get(self.url, params=params, headers=headers)

        # Check if request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Pretty print the results
            return json.dumps(data, indent=2)
        else:
            return f"Error: {response.status_code}, {response.text}"


class GreetingTool(Tool):
    name = "greeting_tool"
    description = "This tool is used to greet the user"
    inputs = {
        "message": {"type": "string", "description": "The message to be greeted."}
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def forward(self, message):
        return (
            self.llm.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": message}],
            )
            .choices[0]
            .message.content
        )


class UnRelatedQuestionTool(Tool):
    name = "unrelated_question_tool"
    description = (
        "This tool is used to answer questions that are not related to the categories."
    )
    inputs = {
        "message": {"type": "string", "description": "The message to be answered."}
    }
    output_type = "string"

    def forward(self, message):
        return "I'm sorry, but I can't answer that question. I can answer questions related to finding shelter, doctors, dentists, legal advice, etc. Give this as the final answer."


# Initialize your Telegram bot with your token from BotFather
bot = AsyncTeleBot(TELEGRAM_TOKEN)

agent = ToolCallingAgent(
    tools=[
        GroqQueryTool(
            url="https://jpt8guat.api.sanity.io/v2022-03-07/data/query/production"
        ),
        GreetingTool(),
        UnRelatedQuestionTool(),
    ],
    model=OpenAIServerModel(
        api_key=os.getenv("OPENAI_API_KEY"),
        model_id="gpt-4o",
        api_base="https://api.openai.com/v1",
    ),
)


@bot.message_handler(commands=["start", "help"])
async def send_welcome(message):
    welcome_text = """
Welcome to the Refugee Support Assistant! 👋

I can help you with information about:
- Legal help
- Shelter
- Medical assistance
- And more...

Just ask me your question and I'll do my best to help you.

Example questions:
- Where can I find shelter?
- How do I get medical help?
- I need legal assistance
"""
    await bot.reply_to(message, welcome_text)


@bot.message_handler(func=lambda message: True)
async def handle_message(message):
    client = OpenAI()

    # Send "typing" action
    await bot.send_chat_action(message.chat.id, "typing")

    # Prepare the query
    query = (
        "You have the following categories: "
        + json.dumps(available_categories)
        + "Do not include the category in the results. You can use multiple tools."
        + "Reply in markdown format and include the address, website and phone numbers."
        + "Question: "
        + message.text
    )

    # Get agent output
    agent_output = agent.run(query, reset=True)

    # Prepare final prompt
    final_prompt = (
        "The agent has replied with the following: "
        + str(agent_output)
        + "Format the output for telegram. "
        + "If there are phone numbers and addresses in the output, make sure to list them properly by highlighting them. Query: \n"
        + message.text
    )

    # Get OpenAI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": final_prompt}],
        stream=False,  # Changed to False for simplicity
    )

    # Send the response
    try:
        await bot.reply_to(
            message, response.choices[0].message.content, parse_mode="Markdown"
        )
    except Exception as e:
        # Fallback without markdown if markdown parsing fails
        await bot.reply_to(message, response.choices[0].message.content)


@bot.message_handler(content_types=["voice"])
async def handle_voice(message):
    client = OpenAI()

    # Send "typing" action
    await bot.send_chat_action(message.chat.id, "typing")

    # Download the voice message
    file_info = await bot.get_file(message.voice.file_id)
    downloaded_file = await bot.download_file(file_info.file_path)

    # Save voice message temporarily
    with open("voice_message.ogg", "wb") as voice_file:
        voice_file.write(downloaded_file)

    # Transcribe with Whisper
    with open("voice_message.ogg", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1", file=audio_file
        )

    # Create a new message object with the transcribed text
    message.text = transcript.text

    # Process the transcribed text using the existing handler
    await handle_message(message)


# Function to run the bot
async def main():
    print("Bot started...")
    await bot.polling(non_stop=True)


# Run the bot
if __name__ == "__main__":
    asyncio.run(main())
