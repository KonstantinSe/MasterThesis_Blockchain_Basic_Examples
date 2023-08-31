import hashlib

text = "Wein von Schloss Proschwitz ist toll!"
hash_object = hashlib.sha256(text.encode())
hex_dig = hash_object.hexdigest()

for number in range(0, 100000000):
    text_and_nonce = f"{text} {number}"
    print(text_and_nonce)
    hash_object = hashlib.sha256(text_and_nonce.encode())
    hex_dig = hash_object.hexdigest()
    if hex_dig[:5] == "00000":
        print(f' Das Hash Rätsel ist gelöst. Die ersten 5 Zeichen sind fünf Nullen. \n Die Nonce ist  {number}.'
              f' \n Der zugehörige Hash ist {hex_dig}')
        break
