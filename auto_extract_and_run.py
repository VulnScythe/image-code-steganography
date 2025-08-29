import sys
import subprocess
import tempfile
import os

def extract_and_run(image_path):
    with open(image_path, "rb") as file:
        data = file.read()

    marker = b"###HIDDEN_CODE###"
    marker_index = data.find(marker)

    if marker_index == -1:
        print("[-] No hidden code found.")
        return

    # Extract code
    code_bytes = data[marker_index + len(marker):]

    # Write to a temporary file
    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".py")
    tmp_file.write(code_bytes)
    tmp_file.close()

    print(f"[+] Extracted code to: {tmp_file.name}")
    print("[+] Executing...")

    # Run the extracted script
    subprocess.run([sys.executable, tmp_file.name])

    # remove after running
    os.remove(tmp_file.name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python auto_extract_and_run.py <image_with_code.png>")
    else:
        extract_and_run(sys.argv[1])
