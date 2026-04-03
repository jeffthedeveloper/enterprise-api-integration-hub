"class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if status.text.lower() != ""bot response"":  # Evita responder ao próprio bot
            tweet_text = status.text
            response = generate_response(tweet_text)
            print(f""Resposta gerada: {response}"")
            api.update_status(f""@{status.user.screen_name} {response}"", in_reply_to_status_id=status.id)

# Configuração do Stream para monitorar tweets
stream_listener = MyStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

# Filtros para acompanhar tweets com hashtags ou palavras-chave
stream.filter(track=['#exemplo', 'exemplo'], is_async=True)
"