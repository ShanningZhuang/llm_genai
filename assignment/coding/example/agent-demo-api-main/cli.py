import cmd
from backend.api_interface import call_llm, summarize, translate, extend, interact

class InteractiveCLI(cmd.Cmd):
    intro = "CLI: only text ops or full interact via 'run'."
    prompt = "(cli) "
    messages = None

    def do_call(self, arg):
        print(call_llm(arg))

    def do_summarize(self, arg):
        text = open(arg, 'r').read() if arg.startswith('@') else arg
        print(summarize(text))

    def do_translate(self, arg):
        lang, rest = arg.split(maxsplit=1)
        text = open(rest, 'r').read() if rest.startswith('@') else rest
        print(translate(text, lang))

    def do_extend(self, arg):
        text = open(arg, 'r').read() if arg.startswith('@') else arg
        print(extend(text))

    def do_run(self, arg):
        print(interact(arg, self.messages))

    def do_exit(self, arg): return True
    def do_EOF(self, arg): return True

if __name__ == "__main__":
    InteractiveCLI().cmdloop()
