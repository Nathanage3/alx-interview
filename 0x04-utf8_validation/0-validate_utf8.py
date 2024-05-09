def validUTF8(data):
    # Initialize a variable `i` to 0, which will be used as an index to iterate through the `data` list.
    i = 0
    # Start a while loop that will continue until `i` is no longer less than the length of the `data` list.
    while i < len(data):
        # Initialize a variable `bytes_in_char` to 1, which will store the number of bytes in the current character.
        bytes_in_char = 1
        # Get the current byte from the `data` list using the index `i`.
        byte = data[i]
        # Check if the byte is a single-byte ASCII character (i.e., its value is less than 0x80).
        if byte < 0x80:
            # If it is, increment `i` to move to the next byte and skip to the next iteration of the loop using the `continue` statement.
            i += 1
            continue
        # Check if the byte is a multi-byte character that is not a valid start byte (i.e., its value is between 0x80 and 0xC0).
        elif byte < 0xC0:
            # If it is, return False, indicating that the `data` list does not represent a valid UTF-8 encoding.
            return False  # invalid byte
        # Check if the byte is the start of a 2-byte character (i.e., its value is between 0xC0 and 0xE0).
        elif byte < 0xE0:
            # If it is, set `bytes_in_char` to 2.
            bytes_in_char = 2
        # Check if the byte is the start of a 3-byte character (i.e., its value is between 0xE0 and 0xF0).
        elif byte < 0xF0:
            # If it is, set `bytes_in_char` to 3.
            bytes_in_char = 3
        # If the byte is the start of a 4-byte character (i.e., its value is 0xF0 or greater), set `bytes_in_char` to 4.
        else:
            bytes_in_char = 4
        # Start a for loop that will iterate `bytes_in_char - 1` times, checking the subsequent bytes of the character.
        for _ in range(1, bytes_in_char):
            # Increment `i` to move to the next byte.
            i += 1
            # Check if `i` is now greater than or equal to the length of the `data` list.
            if i >= len(data):
                # If it is, return False, indicating that the `data` list does not represent a valid UTF-8 encoding (incomplete character).
                return False  # incomplete character
            # Get the next byte from the `data` list using the index `i`.
            byte = data[i]
            # Check if the byte is not a valid subsequent byte (i.e., its value is less than 0x80 or 0xC0 or greater).
            if byte < 0x80 or byte >= 0xC0:
                # If it is, return False, indicating that the `data` list does not represent a valid UTF-8 encoding.
                return False  # invalid subsequent byte
        # Increment `i` to move to the next byte.
        i += 1
    # If the loop completes without returning False, return True, indicating that the `data` list represents a valid UTF-8 encoding.
    return True