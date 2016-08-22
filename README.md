# lda-api
Simple web service that will enable the LDA 
Simple web service that will provide API. The methods are based on Gensim LDA implementation. Models are passed as parameters and must be in the LDA  binary format.

- Launching the service
```
python lda-api.py --model path/to/the/model [--host host --port 1234]
```

- Example calls
```
curl http://127.0.0.1:5000/lda/show_topic?number=24
curl http://127.0.0.1:5000/lda/print_topic?number=20
curl http://127.0.0.1:5000/lda/topic?sentence=Football%20is%20a%20family%20of%20team%20sports%20that%20involve%20to%20varying%20degrees%20kicking%20a%20ball%20with%20the%20foot%20to%20score%20a%20goal
```


