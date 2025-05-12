import math

def create_table(key, text, fill_char='X'):
    columns = len(key)
    rows = math.ceil(len(text) / columns)
    padded_text = text.ljust(rows * columns, fill_char)
    table = [padded_text[i:i + columns] for i in range(0, len(padded_text), columns)]
    return table

def sort_key(key):
    return sorted(range(len(key)), key=lambda k: key[k])

def encrypt(text, key_phrase):
    key = sort_key(key_phrase)
    table = create_table(key_phrase, text)
    encrypted_text = ''.join(''.join(row[k] for row in table) for k in key)
    return encrypted_text

def decrypt(encrypted_text, key_phrase):
    key = sort_key(key_phrase)
    columns = len(key_phrase)
    rows = len(encrypted_text) // columns
    cols = [encrypted_text[i * rows:(i + 1) * rows] for i in range(columns)]
    reordered_cols = [''] * columns
    for i, k in enumerate(key):
        reordered_cols[k] = cols[i]
    decrypted_text = ''.join(''.join(row) for row in zip(*reordered_cols)).rstrip('X')
    return decrypted_text

key = "MATRIX"
plain_text = """
The artist is the creator of beautiful things. To reveal art and conceal the artist is 
art's aim. The critic is he who can translate into another manner or a new material his 
impression of beautiful things. The highest, as the lowest, form of criticism is a mode 
of autobiography. Those who find ugly meanings in beautiful things are corrupt without 
being charming. This is a fault. Those who find beautiful meanings in beautiful things 
are the cultivated. For these there is hope. They are the elect to whom beautiful things 
mean only Beauty. There is no such thing as a moral or an immoral book. Books are well 
written, or badly written. That is all. The nineteenth-century dislike of realism is the 
rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of 
Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of 
man forms part of the subject matter of the artist, but the morality of art consists in 
the perfect use of an imperfect medium. No artist desires to prove anything. Even things 
that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an 
artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can 
express everything. Thought and language are to the artist instruments of an art. Vice 
and virtue are to the artist materials for an art. From the point of view of form, the 
type of all the arts is the art of the musician. From the point of view of feeling, the 
actor's craft is the type. All art is at once surface and symbol. Those who go beneath 
the surface do so at their peril. Those who read the symbol do so at their peril. It is 
the spectator, and not life, that art really mirrors. Diversity of opinion about a work 
of art shows that the work is new, complex, vital. When critics disagree the artist is 
in accord with himself. We can forgive a man for making a useful thing as long as he does 
not admire it. The only excuse for making a useless thing is that one admires it intensely. 
All art is quite useless.
"""


plain_count = len(plain_text)
cipher_text = encrypt(plain_text, key)
cipher_count = len(cipher_text)
decrypted_text = decrypt(cipher_text, key)

print("Зашифрований текст:", cipher_text)
print(f"У оригінальному тексті: {plain_count} символів\n")
print(f"У зашифрованому тексті: {cipher_count} символів\n")
if plain_text.lower() == decrypted_text.lower():
    print("Розшифрований текст співпадає з оригінальним!\n")
else:
    print("Йой! Розшифрований текст НЕ співпадає з оригінальним!\n")

print(
    "Розкоментуйте відповідні строки для виводу оригінального, зашифрованого та розшифрованого тексту."
)
# print(f"Оригінальний текст:\n{plain_text}")
# print(f"Зашифрований текст:\n{cipher_text}")
# print(f"Розшифрований текст:\n{decrypted_text}")
