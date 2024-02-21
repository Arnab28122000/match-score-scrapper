import hashlib
import base64
import json
import uuid

def generate_checksum(payload, endpoint, salt_key, salt_index):
    # Convert JSON payload to Base64 encoded payload
    encoded_payload = base64.b64encode(json.dumps(payload).encode()).decode()

    # Concatenate Base64 encoded payload, endpoint, and salt key
    concatenated_data = encoded_payload + f"/pg/v1/{endpoint}" + salt_key

    # Calculate SHA256 hash
    checksum = hashlib.sha256(concatenated_data.encode()).hexdigest()

    # Append ### and salt index to the checksum
    final_checksum = f"{checksum}###{salt_index}"

    return final_checksum



def generate_uuid():
    # Generate a random UUID
    new_uuid = uuid.uuid4()

    # Convert the UUID to a string
    uuid_str = str(new_uuid)

    return uuid_str
