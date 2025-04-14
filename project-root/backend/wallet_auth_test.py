from eth_account import Account
from eth_account.messages import encode_defunct

# Use a test private key (DO NOT use a real private key for testing)
private_key = "9b6b173c1206b7a7ec6b4731a6ccd33a4e0c8b65cb1f1b8857531fb1e17e01dc"  
account = Account.from_key(private_key).address

# Define the message you want the user to sign
message = "Please sign this message to log in to our DeFi platform"
encoded_message = encode_defunct(text=message)

# Sign the message
signed_message = Account.sign_message(encoded_message, private_key=private_key)

print("Account:", account)
print("Message:", message)
print("Signature:", signed_message.signature.hex())
