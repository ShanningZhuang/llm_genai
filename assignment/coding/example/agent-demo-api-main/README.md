# Local Data File Processing with OpenAI API Integration

This project demonstrates a demo application that processes local data files using OpenAI's API. It includes functionalities for summarizing, translating, and manipulating text files, as well as directly querying the OpenAI LLM.

## Features

- Summarize a text file using OpenAI's language model.
- Translate a text file into a target language.
- Manipulate the content of a text file (convert to uppercase or lowercase).
- Directly call OpenAI's language model with a custom prompt.

## Requirements

This project requires Python 3.6+.

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

You also need to set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-api-key'
```

Also, the API URL could be set as an environment variable as well:

```bash
export OPENAI_API_BASE_URL='api-base-url'
```

- When it is set to `https://api.openai.com/v1` or not set, the service is from OpenAI.
- When it is set to `https://open.bigmodel.cn/api/paas/v4`, the service is from ZhipuAI.
- When it is set to `https://api.deepseek.com`, the service is from DeepSeek-AI.

## Setup

Before using, you can reconfigure the default hyperparameters in `backend/config.py`. These include:

* `MODEL`: the model name to use (e.g., `"gpt-4o"`, `"gpt-4.1-nano"`).
* `TIME_OUT`: maximum timeout (in seconds) for API requests.
* `MAX_RETRIES`: maximum number of retries in case of request failures.
* `TEMPERATURE`: sampling temperature for controlling randomness.
* `MAX_TOKENS`: maximum number of tokens in the response.

The actual API call is handled with OpenAI Python SDK.

## Usage

Run the main command-line interface using:

```bash
python main.py [command] [options]
```

### Available Commands

1. **summarize**

   Summarize a text file using a LLM. Optionally, save the output to a file.

   Example:

   ```bash
   python main.py summarize path/to/file.txt --output summary.txt
   ```

2. **translate**

   Translate the content of a text file into a target language using a LLM. Optionally, save the output to a file.

   Example:

   ```bash
   python main.py translate path/to/file.txt Spanish --output translated.txt
   ```

3. **extend**

   Extend the content of a text file using a LLM with a pre-defined maximum output token. Optionally, save the output to a file.

   Example:

   ```bash
   python main.py extend path/to/file.txt --output extended.txt --max-tokens 300
   ```

4. **manipulate**

   Manipulate a file by applying an operation (uppercase or lowercase) to its content.

   Example:

   ```bash
   python main.py manipulate path/to/file.txt uppercase
   ```

5. **QA**

   Directly call the OpenAI LLM with a textual query prompt.

   Example:

   ```bash
   python main.py llm "Tell me a joke"
   ```

## Interactive CLI

A separate interactive CLI is available by running:

```bash
python cli.py
```

This launches an interactive command loop where you can run OpenAI-powered operations on text data directly from the terminal.

### Available Commands

* **call `<prompt>`**
  Sends a single prompt to the OpenAI LLM and prints the response.

  Example:

  ```bash
  call Tell me a story about a fox
  ```

* **summarize `<text or @filepath>`**
  Summarizes the given text using the OpenAI LLM. You can either pass the text directly or use `@filename.txt` to load text from a file.

  Examples:

  ```bash
  summarize This is a long article about machine learning...
  summarize @path/to/article.txt
  ```

* **translate `<target_language> <text or @filepath>`**
  Translates the given text into the specified language. The input can be inline text or a file reference prefixed with `@`.

  Examples:

  ```bash
  translate French Hello, how are you?
  translate Chinese @notes.txt
  ```

* **extend `<text or @filepath>`**
  Generates a continuation of the provided text. Useful for story or content generation.

  Examples:

  ```bash
  extend Once upon a time in a dark forest...
  extend @story_start.txt
  ```

* **run `<prompt>`**
  Enters a multi-turn interaction mode where the context (conversation history) is preserved across multiple prompts.

  Example:

  ```bash
  run Let's brainstorm ideas for a novel.
  ```

  This enables dynamic, ongoing interaction with the model, remembering previous messages in the session.

* **exit / Ctrl+D**
  Exit the CLI loop.

## Notes

Ensure you have a valid OpenAI API key set in your environment. The project uses the OpenAI API via the `openai` Python package.

## File Structure

```
agent-demo-api/
├── backend/
│   ├── __init__.py
│   ├── api_interface.py
│   ├── config.py
│   ├── file_tools.py
│   ├── llm_client.py
│   └── text_utils.py
├── cli.py
├── file_utils.py
├── main.py
├── output/
├── README.md
└── requirements.txt
```
