import json
import urllib.request


API_URL = "http://127.0.0.1:18081/generate"

TESTS = [
    ("hindi mai bol", "Hindi/Hinglish"),
    ("ladki ko first message kya bheju", "Ye bhej"),
    ("she replied haha nice", "Reply options"),
    ("she said she is not interested", "Do not pressure"),
    ("bonjour parle francais", "francais"),
    ("1+1", "1+1 = 2"),
]


def ask(prompt: str) -> str:
    body = json.dumps({"prompt": f"User: {prompt}\nAssistant:", "max_new_tokens": 96}).encode("utf-8")
    request = urllib.request.Request(API_URL, data=body, method="POST", headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8", "replace")).get("text", "")


def main() -> None:
    for prompt, expected in TESTS:
        text = ask(prompt)
        ok = expected.lower() in text.lower()
        print(("PASS" if ok else "FAIL"), "-", prompt)
        print(text.replace("\n", " ")[:240])
        if not ok:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
