def find_and_extract_sentence(text, target_keyword):
  """Finds and extracts a sentence containing a target keyword from a text string.

  Args:
    text: The input text string.
    target_keyword: The keyword to search for within sentences.

  Returns:
    The extracted sentence containing the target keyword, or None if not found.
  """

  sentences = text.split('.') # Splitting text into sentences by period
  for sentence in sentences:
    if target_keyword.lower() in sentence.lower():
      return sentence.strip() 
  return None

# Example usage
my_text = "This is a sample text. It contains a keyword called 'example'. Can you find it?"
target_keyword = "example"

extracted_sentence = find_and_extract_sentence(my_text, target_keyword)

if extracted_sentence:
  print("Extracted sentence:", extracted_sentence)
else:
  print(f"Sentence containing '{target_keyword}' not found.")