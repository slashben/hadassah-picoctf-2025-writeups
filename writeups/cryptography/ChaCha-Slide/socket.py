import socket

HOST = 'activist-birds.picoctf.net'
PORT = 53513

# --- PASTE YOUR FORGED MESSAGE HEX HERE ---
# Make sure this is the *newly generated* message from Step 1
FORGED_MESSAGE_HEX = "6f135007654c5ef358f610e19ce2f37a1107d940d24af3df9f746393b111b2860a60658f1e08dcad9a37c1c5289bf527045bbb9434712fb0f9703be79276e32586cec3bc5aede2770fdca941f21f0969082c" 
# --- END PASTE ---

def send_and_receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")

        # Receive initial banner/messages from the server
        # We need to read everything until it prompts for input
        received_data = b""
        while True:
            try:
                # Set a timeout for reading to prevent hanging if server doesn't send more
                s.settimeout(0.5) 
                chunk = s.recv(4096) # Read up to 4KB
                if not chunk:
                    break # Connection closed by server
                received_data += chunk
            except socket.timeout:
                # If no data for a while, assume it's waiting for input
                break
            except Exception as e:
                print(f"Error receiving initial data: {e}")
                break
        
        print("\n--- Initial Server Output ---")
        try:
            print(received_data.decode('utf-8', errors='ignore'))
        except UnicodeDecodeError:
            print(f"(Could not decode initial output cleanly: {received_data})")
        print("--- End Initial Server Output ---\n")

        # Send the forged message
        print(f"Sending forged message: {FORGED_MESSAGE_HEX}")
        s.sendall((FORGED_MESSAGE_HEX + "\n").encode('utf-8')) # Add newline for submission

        # Receive ALL subsequent data until connection closes
        final_response = b""
        s.settimeout(2) # Give it a bit more time for the final response
        while True:
            try:
                chunk = s.recv(4096)
                if not chunk:
                    break # Connection closed by server
                final_response += chunk
            except socket.timeout:
                # No more data after a timeout, server might be done
                break
            except Exception as e:
                print(f"Error receiving final response: {e}")
                break

        print("\n--- Final Server Response (hopefully the flag!) ---")
        try:
            print(final_response.decode('utf-8', errors='ignore'))
        except UnicodeDecodeError:
            print(f"(Could not decode final response cleanly: {final_response})")
        print("--- End Final Server Response ---\n")

if __name__ == "__main__":
    send_and_receive()