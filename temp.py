# ライブラリ
import tweepy

# Consumer Keys
ck = 'NkiOh87oQeCzvKwZhQ0mE1ITT' #API KEYが入ります
cs = 'FN0hbVabPNCbaJ1M9EdAYMiQijqWKD3UeFCYTITT0Aaq7kg68T' #API KEY SECRETが入ります

# Authentication Tokens
bt = 'AAAAAAAAAAAAAAAAAAAAAGPGwwEAAAAAiJyAOC4nttfOZ%2BH6GOkKfIS2bWY%3D5sJg3frfTG44Tp8Rs41dslI04OSOEuNyFAf5yfHyDKrSWvqr1f' #Bearer Tokenが入ります
at = '909624001663688705-UlF98s3LehZRVFK0z1WtxGtW6ApW6ks' #ACCESS TOKENが入ります
ats = 'Jb9XrSTgxd4VifZoJlLw0sThPhJ7QwWZgzJsplWKoIe9L' #ACCESS TOKEN SECRETが入ります

# 認証
client = tweepy.Client(
    bearer_token=bt,
    consumer_key=ck, consumer_secret=cs,
    access_token=at, access_token_secret=ats
)

#ツイート内容
content = 'ポストの内容'

#ツイート
client.create_tweet(text=content)