from PyPDF2 import PdfReader
from botScriptLauncher import SubBot
import time

# a function that correct the form of string to write in js console
def escape_js_string(string):
    # Liste des caractères spéciaux à échapper
    special_chars = ['\\', '\'', '\"', '\n', '\r', '\t', '\b', '\f']
    # Itération sur chaque caractère de la chaîne
    escaped_string = ''
    for char in string:
        # Si le caractère est spécial, ajouter un backslash devant
        if char in special_chars:
            escaped_string += '\\' + char
        # Sinon, ajouter le caractère tel quel
        else:
            escaped_string += char
    return escaped_string

# function to remove last space in pdf text
def remove_last_space_or_newline(string):
    # Vérifier si le dernier caractère est un espace ou un retour à la ligne
    if string[-1] == ' ' or string[-1] == '\n':
        # Supprimer le dernier caractère
        string = string[:-1]
    return string

# Read the PDF file as text
reader = PdfReader("./exemple.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"
text = text[:20000]

# Display the PDF text to chunks
pdf_text = remove_last_space_or_newline(text)
batch_size = 1024
text_chunks = [pdf_text[i:i+batch_size] for i in range(0, len(pdf_text), batch_size)]
# Initialize an empty list to store the generated text
generated_text = []
for chunk in text_chunks:
    request = "Write a Markdown version of the PDF using the following text, keep the text intact and no suggestions should be added: " 
    chunk             = escape_js_string(chunk)
    escaped_js_string = escape_js_string(request)
    subBot = SubBot()
    subBot.Instr_3 = r"textareaI.value = '" + escaped_js_string + chunk + r"'" 
    # time.sleep(2)
    # print(subBot.Instr_3)
    print(subBot.main())
    completion =  subBot.main()
    generated_text.append(completion.choices[0].text)

# Combine the generated text into a single string
full_text = "".join(generated_text)
# Use Markdown syntax to format the message
formatted_message = "# PDF Text\n\n" + full_text

# Save the message to a file
with open("generatedPDF.pdf", "w") as f:
    f.write(formatted_message)