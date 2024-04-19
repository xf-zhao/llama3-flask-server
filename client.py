import json
import requests


class Client:
    def __init__(self, address= "http://134.100.39.10:32033/api/llama3") -> None:
        self.headers = {"content-type": "application/json"}
        self.address = address

    def call(self, **kwargs):
        data = json.dumps(kwargs)
        resp = requests.post(self.address, data=data, headers=self.headers)
        print(resp)
        result = json.loads(resp.text)
        return result

def main():
    client = Client()
    dialogs = [
                    [{"role": "user", "content": "what is the recipe of mayonnaise?"}, {"role": "user", "content": "what is the recipe of mayonnaise?"}],
                    [{"role": "user", "content": "what is hello world?"}],
                    [{"role": "user", "content": "who are you?"}],
                    [{"role": "user", "content": "1+1=?"}],
                                                ]



    resp  = client.call(
        dialogs = dialogs,
        temperature = 0.6,
        top_p = 0.9,
        logprobs = False,
            )
    print(resp)


main()
