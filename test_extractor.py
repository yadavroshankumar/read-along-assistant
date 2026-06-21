from app.extractor import extract_text

# Change this to match your actual test file name
file_path = "Roshan_Yadav_General_Resume_v2 (2).pdf"

text = extract_text(file_path)

print("--- Extracted text ---")
print(text)
print("--- End ---")
print(f"\nTotal characters: {len(text)}")