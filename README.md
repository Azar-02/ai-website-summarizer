
# AI Website Summarizer

A simple AI-powered web application that extracts readable content from a website and generates a concise summary using the Groq API.

Built with Python, Requests, BeautifulSoup, Gradio, and an OpenAI-compatible client configured to use Groq.

## Features

- Extract readable text from a website URL.
- Generate AI-powered summaries using Groq.
- Display summaries in a clean Gradio interface.
- Custom dark theme using external CSS.
- Handle common website fetching and summarization errors.
- Clear the input and reset the summary output.

## Tech Stack

- **Python** — application logic
- **Requests** — fetch website content
- **BeautifulSoup** — parse HTML and extract readable text
- **Groq API** — generate AI summaries
- **Gradio** — build the web interface
- **CSS** — customize the interface
- **python-dotenv** — load environment variables

## Project Structure

```text
ai-website-summarizer/
├── app.py
├── scraper.py
├── summarizer.py
├── requirements.txt
├── .gitignore
├── .env
└── static/
    └── style.css
```

The `.env` file contains a local API key and must not be committed to Git.

## How It Works

1. The user enters a website URL.
2. The scraper fetches the webpage using Requests.
3. BeautifulSoup extracts the page title and readable text.
4. The extracted content is sent to a Groq-hosted AI model with a summarization prompt.
5. The generated summary is displayed in the Gradio interface.

## Getting Started

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-website-summarizer
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Replace the placeholder with your own Groq API key.

Get an API key from the [Groq Console](https://console.groq.com/).

Never commit or share your real API key.

### 5. Run the application

```powershell
python app.py
```

Open the local URL displayed in the terminal, usually:

`http://127.0.0.1:7860`

Enter a website URL and click **Summarize Website**.

## Configuration

The model ID is configured in `summarizer.py`. The application requires a model that is available to your Groq account and supports chat completions.

API access and rate limits depend on your Groq account.

## Limitations

- Some websites may block automated requests.
- JavaScript-heavy websites may not expose their main content in the initial HTML.
- Very long pages may exceed the model's input limits.
- Summary quality depends on the extracted content and the selected model.

## Future Improvements

- Add support for summarizing longer webpages.
- Improve URL validation and error handling.
- Add summary length options.
- Deploy the application online.

## License

This project is created for learning and portfolio purposes.
