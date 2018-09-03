from wit import Wit

access_token = "LJ3KXHG6YUNLPEJCMQCYVRIKVOSSW3VI"

client = Wit(access_token = access_token)

message_text = "i like sports"

resp = client.message(message_text)


print(resp)