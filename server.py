from typing import List, Optional

import fire

from llama import Dialog, Llama

from flask import Flask, request, Response
import json, os




def main(
        ckpt_dir: str = '/data/xufeng/llama3/Meta-Llama-3-8B-Instruct/',
        tokenizer_path = '/data/xufeng/llama3/Meta-Llama-3-8B-Instruct/tokenizer.model',
        temperature: float = 0.6,
        top_p: float = 0.9,
        max_seq_len = 8192,
        max_batch_size: int = 4,
        max_gen_len: Optional[int] = None,
        ):
    generator = Llama.build(
            ckpt_dir=ckpt_dir,
            tokenizer_path=tokenizer_path,
            max_seq_len=max_seq_len,
            max_batch_size=max_batch_size,
        )
    app = Flask(__name__)

    @app.route('/api/llama3', methods=['GET', 'POST'])
    def llama3():
        if request.method == 'GET':
            response = 'This is the llama3 server created by Xufeng Zhao. Contact: xufeng.zhao@uni-hamburg.de'
        else:
            print(request.json)
            results = generator.chat_completion(**request.json)
            response = json.dumps(results)
        return Response(response=response, status=200, mimetype="application/json")

    app.run(host="0.0.0.0", port=8848)

if __name__ == "__main__":
    fire.Fire(main)
