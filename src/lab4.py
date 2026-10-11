import re
from collections import Counter

# === Функції для базових операцій з рядками ===

def find_substring(text, substring):
    return text.find(substring)

def replace_substring(text, old, new):
    return text.replace(old, new)

def split_text(text, delimiter=' '):
    return text.split(delimiter)

def format_string_f(name, age):
    return f"Мене звати {name} і мені {age} років."

def format_string_method(name, age):
    return "Мене звати {} і мені {} років.".format(name, age)

# === Функції для роботи з регулярними виразами ===

def extract_emails(text):
    return re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

def validate_phone_number(number):
    return bool(re.fullmatch(r'\+380\d{9}', number))

def extract_hashtags(text):
    return re.findall(r'#\w+', text)

def extract_mentions(text):
    return re.findall(r'@\w+', text)

# === Функції для аналізу тексту ===

def count_words(text):
    return len(re.findall(r'\b\w+\b', text))

def count_sentences(text):
    return len(re.findall(r'[.!?]+', text))

def word_frequency(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words)

def analyze_text(text):
    return {
        'word_count': count_words(text),
        'sentence_count': count_sentences(text),
        'emails': extract_emails(text),
        'hashtags': extract_hashtags(text)
    }

def format_analysis_results(results):
    output = "Результати аналізу тексту:\n"
    output += f"Кількість слів: {results['word_count']}\n"
    output += f"Кількість речень: {results['sentence_count']}\n"
    output += f"Знайдені email: {', '.join(results['emails']) if results['emails'] else 'Немає'}\n"
    output += f"Хештеги: {', '.join(results['hashtags']) if results['hashtags'] else 'Немає'}\n"
    return output

# === Функція для вилучення даних за варіантом 3 ===

def extract_variant_data(text, variant_pattern):
    return re.findall(variant_pattern, text)

def parse_csv_string(csv_text):
    """Практичне завдання Варіанту 3: Парсинг CSV"""
    lines = csv_text.strip().split('\n')
    parsed_data = []
    for line in lines:
        parsed_data.append(line.split(','))
    return parsed_data

# === Головна частина програми ===

def read_file_content(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Помилка: Файл не знайдено за шляхом {filepath}")
        return None

def main():
    print("Ласкаво просимо до аналізатора тексту!")
    text_filepath = 'src/data/neoterra_text.txt'
    text_to_analyze = read_file_content(text_filepath)
    
    if not text_to_analyze:
        return 

    while True:
        try:
            print("\nОберіть опцію:")
            print("1. Аналіз тексту 'NeoTerra 3000'")
            print("2. Валідація телефонного номера")
            print("3. Вилучення даних за варіантом (Варіант 3: Нейромережі)")
            print("4. Практичне завдання (Варіант 3: CSV)")
            print("5. Вихід")
            choice = input("Ваш вибір: ")

            if choice == '1':
                results = analyze_text(text_to_analyze)
                print(format_analysis_results(results))

            elif choice == '2':
                phone = input("Введіть номер телефону (+380...): ")
                if validate_phone_number(phone):
                    print("Номер телефону валідний.")
                else:
                    print("Номер телефону невалідний.")

            elif choice == '3':
                # Патерн для версій нейромереж (наприклад: NT-Net v5.3)
                pattern = r'\b[A-Za-z]+-[A-Za-z]+\sv\d+\.\d+\b'
                variant_data = extract_variant_data(text_to_analyze, pattern)
                print(f"Знайдені нейромережі: {variant_data}")

            elif choice == '4':
                sample_csv = "id,name,role\n1,Alice,Admin\n2,Bob,User"
                print("Оригінальний CSV:\n", sample_csv)
                print("Розпарсений список списків:\n", parse_csv_string(sample_csv))

            elif choice == '5':
                print("Дякуємо за використання аналізатора!")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except Exception as e:
            print(f"Виникла помилка: {e}")

if __name__ == '__main__':
    main()