import openai,time

def load_data():
    with open("input.txt", 'r', encoding="UTF-8") as f:
        lines = f.readlines()
    return lines

def save_data(text):
    with open("output.txt", 'a', encoding="UTF-8") as f:
        f.writelines(text + "\n")


def get_completion(prompt, text):
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages = [{"role": "system", "content" : "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nKnowledge cutoff: 2021-09-01\nCurrent date: 2023-03-02"},
        {"role": "user", "content" : f"{prompt}"},
        {"role": "assistant", "content" : "I'll do my best!"},
        {"role": "user", "content" : f"{text}"}]
        )
        text = completion['choices'][0]['message']["content"]
        cost = int(completion["usage"]["total_tokens"])
        return text, cost


def main():
    print("========================================")
    openai.api_key = ""
    data = load_data()

    for line in data:
        prompt = '''Przetłumacz to z Języka Niemieckiego na Język Polski'''
        response = get_completion(prompt, line)
        text = response[0]
        price = int(response[1])

        prompt = '''Zrób z tego dobry tytuł oferty na Allegro.'''
        response = get_completion(prompt, text)
        save_data(response[0])

        print("text: " +(str(response[0])))
        print("price: "+str(price+int(response[1])))
        print("========================================")
        time.sleep(5)


if __name__ == "__main__":
    main()