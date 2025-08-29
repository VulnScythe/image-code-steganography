title: "🖼️ Image Code Steganography"

description: |
  This project demonstrates a simple way to embed Python code into an image file
  and later extract & execute it.
  It is intended for educational and security research purposes only
  (e.g., showing students how hidden code works).

  ⚠️ Do not use this project to distribute malware or run untrusted code.

features:
  - Hide Python scripts inside any image (.png, .jpg, etc.)
  - Extract hidden code from the image
  - Automatically execute the extracted code

repository_structure: |
  embed_code.py           → Script to hide Python code in an image
  auto_extract_and_run.py → Script to extract and run hidden code
  example.png             → Example carrier image
  README.md               → Documentation
  LICENSE                 → MIT license

usage:
  embedding: |
    python embed_code.py example.png secret_code.py infected.png

    - Takes `example.png` and a Python file (`secret_code.py`)
    - Embeds the code inside the image
    - Produces a new image (`infected.png`) that still opens normally

  extracting: |
    python auto_extract_and_run.py

    - Reads the specified image (`infected.png`)
    - Extracts the hidden Python code
    - Executes it immediately

example:
  secret_code_content: |
    print("Hello from hidden code!")

  run_command: |
    python auto_extract_and_run.py

  expected_output: |
    Hello from hidden code!

notes: |
  - The hidden code is simply appended to the image file.
  - The image still works as an image, but if you open it in a hex editor,
    you can see the hidden data.
  - For true pixel-based steganography, more advanced methods are needed.

license: "MIT License"
