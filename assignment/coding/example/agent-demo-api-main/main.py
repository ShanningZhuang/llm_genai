import argparse
import sys
import os

from backend import api_interface
import file_utils


def summarize_file(file_path, output):
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

    summary = api_interface.summarize_text(content)
    print("Summary:\n", summary)
    if output:
        try:
            with open(output, "w") as f:
                f.write(summary)
            print(f"Summary written to {output}")
        except Exception as e:
            print(f"Error writing summary to file: {str(e)}")


def translate_file(file_path, target_language, output):
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

    translated = api_interface.translate_text(content, target_language)
    print("Translated text:\n", translated)
    if output:
        try:
            with open(output, "w") as f:
                f.write(translated)
            print(f"Translated text written to {output}")
        except Exception as e:
            print(f"Error writing translated text to file: {str(e)}")


def extend_file(file_path, max_tokens, output):
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

    extended = api_interface.extend_text(content, max_tokens)
    print("Extended text:\n", extended)
    if output:
        try:
            with open(output, "w") as f:
                f.write(extended)
            print(f"Extended text written to {output}")
        except Exception as e:
            print(f"Error writing extended text to file: {str(e)}")


def manipulate_file_cmd(file_path, operation):
    result = file_utils.manipulate_file(file_path, operation)
    print(result)


def call_llm_cmd(prompt):
    response = api_interface.call_llm(prompt)
    print("LLM response:\n", response)


def main():
    parser = argparse.ArgumentParser(description="Local data file processing with OpenAI API integration")
    subparsers = parser.add_subparsers(dest="command", help="Sub-command help")

    summarize_parser = subparsers.add_parser("summarize", help="Summarize a text file using OpenAI LLM")
    summarize_parser.add_argument("file", help="Path to the file to summarize")
    summarize_parser.add_argument("--output", "-o", help="Path to write summary output", default=None)

    translate_parser = subparsers.add_parser("translate", help="Translate a text file into a target language using OpenAI LLM")
    translate_parser.add_argument("file", help="Path to the file to translate")
    translate_parser.add_argument("language", help="Target language for translation")
    translate_parser.add_argument("--output", "-o", help="Path to write translation output", default=None)

    extend_parser = subparsers.add_parser("extend", help="Extend a text file using OpenAI LLM")
    extend_parser.add_argument("file", help="Path to the file to extend")
    extend_parser.add_argument("--output", "-o", help="Path to write extended output", default=None)
    extend_parser.add_argument("--max-tokens", "-m", type=int, default=150, help="Max tokens for extension")

    manipulate_parser = subparsers.add_parser("manipulate", help="Manipulate a file (uppercase or lowercase)")
    manipulate_parser.add_argument("file", help="Path to the file to manipulate")
    manipulate_parser.add_argument("operation", choices=["uppercase", "lowercase"], help="Operation to apply")

    llm_parser = subparsers.add_parser("llm", help="Call the OpenAI LLM with a prompt")
    llm_parser.add_argument("prompt", help="Prompt to send to LLM")

    args = parser.parse_args()

    if args.command == "summarize":
        summarize_file(args.file, args.output)
    elif args.command == "translate":
        translate_file(args.file, args.language, args.output)
    elif args.command == "extend":
        extend_file(args.file, args.max_tokens, args.output)
    elif args.command == "manipulate":
        manipulate_file_cmd(args.file, args.operation)
    elif args.command == "llm":
        call_llm_cmd(args.prompt)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

