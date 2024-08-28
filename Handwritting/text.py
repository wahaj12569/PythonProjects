import pywhatkit as pw

txt = '''Paragraphs are the building blocks of papers. 
Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences, 
a paragraph is half a page long, etc. In reality, though, 
the unity and coherence of ideas among sentences is what constitutes a paragraph.'''

pw.text_to_handwriting(txt,"test1.png")
print("END")