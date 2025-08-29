import sys

def embed_code(image_path, code_path, output_path):
    # Read the image as bytes
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()

    # Read the code as bytes
    with open(code_path, "rb") as code_file:
        code_bytes = code_file.read()

    # Append a marker + code bytes to image
    marker = b"###HIDDEN_CODE###"
    combined = img_bytes + marker + code_bytes

    # Save to new image
    with open(output_path, "wb") as out_file:
        out_file.write(combined)

    print(f"[+] Code embedded into {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python embed_code.py <image.png> <code.py> <output.png>")
    else:
        embed_code(sys.argv[1], sys.argv[2], sys.argv[3])
