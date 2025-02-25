# Summariser

This Python application allows users to extract textual content from various sources, including YouTube videos, websites, PDF documents, and plain text files. The extracted content can then be queried using the ChatGPT language model to generate responses, summaries, or additional information.

## Features

- Extract text from:
  - YouTube videos (via transcripts)
  - Web articles
  - PDF documents
  - Plain text input
- Interactive querying of extracted text using DeepAI's language models.
- Summarization and refining responses with configurable model parameters.

## Requirements

- Python 3.7 or later
- Necessary Python packages:
  - `openai`: For using the DeepAI API.
  - `httpx`: For making HTTP requests.
  - `playwright`: For web automation (installation includes browser binaries).
  - `llama-index`: For handling content processing and querying.
  - `colorama`: For text coloring in output.

You can install the required packages using pip:

```bash
pip install openai httpx playwright llama-index colorama
playwright install
```

## Setup

1. **API Key**: Obtain an API key from DeepAI and set it in the code:
   ```python
   openai.api_key = 'YOUR_API_KEY'
   ```

2. **Run the Application**:
   Save the script (e.g., `multi_source_query.py`) and run it:

   ```bash
   python multi_source_query.py
   ```

## Usage

Once the application starts, follow these steps:

1. Choose an option to extract content:
   - `1` for YouTube: Enter a YouTube video URL to extract the transcript.
   - `2` for a Website: Enter the URL of a web article.
   - `3` for a PDF: Enter the URL of the PDF file.
   - `4` for Word: Enter plain text or context manually.

2. After extraction, type in your query at the prompt. To exit the querying phase, type `exit`.

## Example Flow

1. Select option `1` for YouTube.
2. Input a valid YouTube video URL.
3. Query the extracted transcript by typing in your questions.
4. View the responses generated by the model.

## Error Handling

The application currently handles basic user input and HTTP request errors but may need further improvements for stronger resilience in production-level use.

## Notes

- Content extraction might take some time, especially for longer documents or videos.
- Ensure your API usage complies with their usage policies.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE.

## Acknowledgments

- [Openai](https://openai.com/) for providing the language model API.
- [Playwright](https://playwright.dev/) for enabling web automation.
- [httpx](https://www.python-httpx.org/) for HTTP requests.
- [Llama Index](https://github.com/jerryjliu/llama_index) for document management and querying functionalities.
- [Colorama](https://pypi.org/project/colorama/) for better output display in the terminal.
```

### Customizations
- Replace `'YOUR_API_KEY'` in the setup section with explicit instructions to fetch the DeepAI API key securely.
- Adjust the projects' acknowledgments and license information according to your needs, especially if you modify any of the dependencies or their usage. 
- You can expand the error handling section with additional descriptions if necessary based on your testing outcomes.
