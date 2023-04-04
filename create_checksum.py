import hashlib

def create_checksum_string(string):
    # Convert the string to bytes
    string_bytes = bytes(string, 'utf-8')
    
    # Calculate the SHA-256 checksum
    checksum = hashlib.sha256(string_bytes).hexdigest()
    
    # Create a dictionary with the original string and the checksum
    checksum_string = {
        'string': string,
        'checksum': checksum
    }
    
    return checksum_string

# Example usage
original_string = 'Hello, world!'
checksum_string = create_checksum_string(original_string)
print(checksum_string)
