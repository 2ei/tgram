import os, argparse, requests, re, inspect
from tgram import TgBot

methods = ["_send_request"] + [m for m in dir(TgBot) if not m.startswith("_")]
camel_to_snake = lambda s: re.sub(r"(?<!^)(?=[A-Z])", "_", s).lower()

def generate():
    print("Generating template..")
    for name in [".env", ".gitignore", "README.md", "config.py", "main.py", "requirements.txt", "plugins/start.py", "generate.md"]:
        os.makedirs(os.path.dirname(name), exist_ok=True)
        with open(name, "w", encoding="utf-8") as f:
            f.write(requests.get(f"https://raw.githubusercontent.com/z44d/tgram/main/tgram/cli/template/{name}").text)
        print(f"Generated {name}.")
    print("\033[92mGENERATED SUCCESSFULLY")

def parse_args(parser, method):
    for p in inspect.signature(getattr(TgBot("token"), method)).parameters.values():
        parser.add_argument(f"--{p.name}", required=False)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--token", type=str, help="Telegram bot token")
    p.add_argument("--method", type=str, help="Telegram method (e.g., sendMessage)")
    p.add_argument("-t", "--template", action="store_true")
    args, _ = p.parse_known_args()

    if args.template: return generate()
    if not args.token or not args.method:
        return print("Usage: tgram --token TOKEN --method sendMessage --chat_id ... --text ...")

    method = camel_to_snake(args.method)
    if method not in methods: return print(f"Wrong method [{method}]")
    
    parse_args(p, method)
    args = p.parse_args()
    params = {k: v for k, v in vars(args).items() if k not in ["token", "method", "template"] and v}

    try:
        print(getattr(TgBot(args.token), method)(**params))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
