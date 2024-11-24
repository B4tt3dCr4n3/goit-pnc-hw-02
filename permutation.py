def get_permutation_key(keyword):
    """
    Створює ключ перестановки на основі ключового слова.
    Наприклад, для слова 'SECRET':
    S E C R E T
    5 1 0 4 2 3
    """
    # Створюємо список пар (буква, початкова позиція)
    pairs = list(enumerate(keyword))
    
    # Сортуємо за буквами і отримуємо новий порядок
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    
    # Створюємо ключ перестановки
    permutation = [-1] * len(keyword)
    for new_pos, (orig_pos, _) in enumerate(sorted_pairs):
        permutation[orig_pos] = new_pos
    
    return permutation

def pad_text(text, width):
    """Доповнює текст пробілами до потрібної довжини"""
    padding = width - (len(text) % width) if len(text) % width else 0
    return text + ' ' * padding

def create_matrix(text, width):
    """Створює матрицю з тексту по рядках"""
    text = pad_text(text, width)
    return [list(text[i:i + width]) for i in range(0, len(text), width)]

def apply_column_permutation(matrix, permutation, reverse=False):
    """Застосовує перестановку стовпців до матриці"""
    if reverse:
        # Створюємо зворотню перестановку для дешифрування
        reverse_perm = [-1] * len(permutation)
        for i, p in enumerate(permutation):
            reverse_perm[p] = i
        permutation = reverse_perm
    
    result = []
    for row in matrix:
        new_row = [''] * len(permutation)
        for i, p in enumerate(permutation):
            new_row[p] = row[i]
        result.append(new_row)
    return result

# ------------------------- РІВЕНЬ 1 -------------------------
def simple_encrypt(text, keyword):
    """
    Шифрування методом простої перестановки
    
    Args:
        text (str): Текст для шифрування
        keyword (str): Ключове слово для створення перестановки
    
    Returns:
        str: Зашифрований текст
    """
    # Отримуємо ключ перестановки
    permutation = get_permutation_key(keyword)
    width = len(keyword)
    
    # Створюємо матрицю з тексту
    matrix = create_matrix(text, width)
    
    # Застосовуємо перестановку
    encrypted_matrix = apply_column_permutation(matrix, permutation)
    
    # Збираємо результат
    return ''.join(''.join(row) for row in encrypted_matrix)

def simple_decrypt(encrypted_text, keyword):
    """
    Дешифрування методом простої перестановки
    
    Args:
        encrypted_text (str): Зашифрований текст
        keyword (str): Ключове слово для створення перестановки
    
    Returns:
        str: Розшифрований текст
    """
    # Отримуємо ключ перестановки
    permutation = get_permutation_key(keyword)
    width = len(keyword)
    
    # Створюємо матрицю з зашифрованого тексту
    matrix = create_matrix(encrypted_text, width)
    
    # Застосовуємо зворотню перестановку
    decrypted_matrix = apply_column_permutation(matrix, permutation, reverse=True)
    
    # Збираємо результат і видаляємо доповнення
    return ''.join(''.join(row) for row in decrypted_matrix).rstrip()

# ------------------------- РІВЕНЬ 2 -------------------------
def double_encrypt(text, keyword1, keyword2):
    """
    Шифрування методом подвійної перестановки
    
    Args:
        text (str): Текст для шифрування
        keyword1 (str): Перше ключове слово
        keyword2 (str): Друге ключове слово
    
    Returns:
        str: Зашифрований текст
    """
    # Перша перестановка
    first_encryption = simple_encrypt(text, keyword1)
    
    # Друга перестановка
    return simple_encrypt(first_encryption, keyword2)

def double_decrypt(encrypted_text, keyword1, keyword2):
    """
    Дешифрування методом подвійної перестановки
    
    Args:
        encrypted_text (str): Зашифрований текст
        keyword1 (str): Перше ключове слово
        keyword2 (str): Друге ключове слово
    
    Returns:
        str: Розшифрований текст
    """
    # Дешифруємо в зворотньому порядку
    first_decryption = simple_decrypt(encrypted_text, keyword2)
    return simple_decrypt(first_decryption, keyword1)

def level1_demo(text):
    """Демонстрація роботи першого рівня"""
    print("\n" + "="*50)
    print("РІВЕНЬ 1: Проста перестановка")
    print("="*50)
    
    key = "SECRET"
    print(f"Початковий текст:\n{text}")
    print(f"\nКлюч: {key}")
    
    # Шифрування
    encrypted = simple_encrypt(text, key)
    print(f"\nЗашифрований текст:\n{encrypted}")
    
    # Дешифрування
    decrypted = simple_decrypt(encrypted, key)
    print(f"\nРозшифрований текст:\n{decrypted}")
    
    return encrypted

def level2_demo(text):
    """Демонстрація роботи другого рівня"""
    print("\n" + "="*50)
    print("РІВЕНЬ 2: Подвійна перестановка")
    print("="*50)
    
    key1 = "SECRET"
    key2 = "CRYPTO"
    print(f"Початковий текст:\n{text}")
    print(f"\nПерший ключ: {key1}")
    print(f"Другий ключ: {key2}")
    
    # Шифрування
    encrypted = double_encrypt(text, key1, key2)
    print(f"\nЗашифрований текст:\n{encrypted}")
    
    # Дешифрування
    decrypted = double_decrypt(encrypted, key1, key2)
    print(f"\nРозшифрований текст:\n{decrypted}")

def visualize_permutation(keyword):
    """Візуалізація процесу створення перестановки"""
    print(f"\nВізуалізація перестановки для ключа '{keyword}':")
    print("Оригінальні позиції: ", end='')
    print(' '.join(keyword))
    
    permutation = get_permutation_key(keyword)
    print("Нові позиції:        ", end='')
    print(' '.join(str(p) for p in permutation))

if __name__ == "__main__":
    # Текст для шифрування
    sample_text = "The artist is the creator of beautiful things. To reveal art and conceal the artist is art's aim. The critic is he who can translate into another manner or a new material his impression of beautiful things. The highest, as the lowest, form of criticism is a mode of autobiography. Those who find ugly meanings in beautiful things are corrupt without being charming. This is a fault. Those who find beautiful meanings in beautiful things are the cultivated. For these there is hope. They are the elect to whom beautiful things mean only Beauty. There is no such thing as a moral or an immoral book. Books are well written, or badly written. That is all. The nineteenth-century dislike of realism is the rage of Caliban seeing his own face in a glass. The nineteenth-century dislike of Romanticism is the rage of Caliban not seeing his own face in a glass. The moral life of man forms part of the subject matter of the artist, but the morality of art consists in the perfect use of an imperfect medium. No artist desires to prove anything. Even things that are true can be proved. No artist has ethical sympathies. An ethical sympathy in an artist is an unpardonable mannerism of style. No artist is ever morbid. The artist can express everything. Thought and language are to the artist instruments of an art. Vice and virtue are to the artist materials for an art. From the point of view of form, the type of all the arts is the art of the musician. From the point of view of feeling, the actor's craft is the type. All art is at once surface and symbol. Those who go beneath the surface do so at their peril. Those who read the symbol do so at their peril. It is the spectator, and not life, that art really mirrors. Diversity of opinion about a work of art shows that the work is new, complex, vital. When critics disagree the artist is in accord with himself. We can forgive a man for making a useful thing as long as he does not admire it. The only excuse for making a useless thing is that one admires it intensely. All art is quite useless."
    
    # Візуалізація перестановок
    visualize_permutation("SECRET")
    visualize_permutation("CRYPTO")
    
    # Демонстрація Рівня 1
    encrypted_text = level1_demo(sample_text)
    
    # Демонстрація Рівня 2
    level2_demo(sample_text)