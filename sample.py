import wolframalpha

WOLFRAM_API_KEY = 'THVWJR-KPGAJ6EJVY'
wolfram_client = wolframalpha.Client(WOLFRAM_API_KEY)

query = "Who is the Prime Minister of India?"
try:
    res = wolfram_client.query(query)
    answer = next(res.results).text
    print("Answer:", answer)
except Exception as e:
    print(f"Error: {e}")
