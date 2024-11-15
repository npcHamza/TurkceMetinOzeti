import re
import os
import time
from collections import defaultdict
from colorama import init, Fore, Style
from rich.console import Console
from rich.table import Table
import shutil


init(autoreset=True)
console = Console()

os.system('cls' if os.name == 'nt' else 'clear')
banner = r"""
 _____ _   _      _            __  __      _   _        ___          _   _ 
|_   _(_) (_)_ __| | _____ ___|  \/  | ___| |_(_)_ __  / _ \ _______| |_(_)
  | | | | | | '__| |/ / __/ _ \ |\/| |/ _ \ __| | '_ \| | | |_  / _ \ __| |
  | | | |_| | |  |   < (_|  __/ |  | |  __/ |_| | | | | |_| |/ /  __/ |_| |
    |_|  \__,_|_|  |_|\_\___\___|_|  |_|\___|\__|_|_| |_|\___//___\___|\__|_|   
                       
x/HFerrahoglu
"""
colors = [Fore.RED, Fore.RED + Style.BRIGHT, Fore.RED + Style.BRIGHT]

def print_colored_banner(banner_text):
    lines = banner_text.splitlines()
    terminal_width = shutil.get_terminal_size().columns
    
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        padded_line = line.center(terminal_width)
        print(color + padded_line)
        time.sleep(0.1)

print_colored_banner(banner)
console.rule(style="red")

def calculate_word_frequency(text):
    text = re.sub(r'[^a-zA-ZçÇğĞıİöÖşŞüÜ\s]', '', text.lower())
    words = text.split()
    word_freq = defaultdict(int)
    for word in words:
        word_freq[word] += 1
    return word_freq

def score_sentences(text, word_freq):
    sentences = re.split(r'(?<=[.!?]) +', text)
    sentence_scores = defaultdict(float)
    for sentence in sentences:
        words = sentence.split()
        score = sum(word_freq.get(word.lower(), 0) for word in words)
        sentence_scores[sentence] = score
    return sentences, sentence_scores

def summarize_text(sentences, sentence_scores, sentence_count):
    best_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:sentence_count]
    return ' '.join([sentence for sentence in sentences if sentence in best_sentences])

def summarize_file_content(file_content, sentence_count=3):
    word_freq = calculate_word_frequency(file_content)
    sentences, sentence_scores = score_sentences(file_content, word_freq)
    return summarize_text(sentences, sentence_scores, sentence_count)

def list_txt_files():
    txt_files = [file for file in os.listdir() if file.endswith('.txt')]
    table = Table(title="TXT Dosyaları", show_lines=True)
    table.add_column("Numara", style="cyan")
    table.add_column("Dosya İsmi", style="dark_violet")
    table.add_column("Önizleme (ilk 30 kelime)", style="green")

    for i, file in enumerate(txt_files):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read().split()[:30]
            preview = ' '.join(content)
            table.add_row(str(i), file, preview)
    table.add_row('', 'Çıkış (q)', '')
    console.print(table)
    return txt_files

def main():
    while True:
        txt_files = list_txt_files()
        print(Fore.GREEN + "Sayı seçin:")
        choice = input(Fore.CYAN + ">" + Fore.WHITE + " ")

        if choice == 'q':
            print(Fore.RED + "Çıkılıyor...")
            break

        try:
            file_index = int(choice)
            selected_file = txt_files[file_index]
            with open(selected_file, 'r', encoding='utf-8') as f:
                content = f.read()

            os.system('cls' if os.name == 'nt' else 'clear')
            print_colored_banner(banner)

            for i in range(5):
                for frame in "/-\|":
                    print(f"\r{Fore.YELLOW}Özetleniyor... {frame}", end="")
                    time.sleep(0.1)

            summary = summarize_file_content(content, sentence_count=3)
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n")
            table = Table(title="Orijinal Metin & Özet")
            table.add_column("Orijinal Metin", style="medium_purple1", width=50)
            table.add_column("Özet", style="cyan", width=50)
            table.add_row(content[:1000] + '...', summary)
            console.print(table)
            
            console.rule("[bold magenta]x/HFerrahoglu[/bold magenta]")
            
            save_choice = input(Fore.YELLOW + "Özeti kaydetmek ister misiniz? (y/n): ")
            if save_choice.lower() == 'y':
                file_name = input(Fore.YELLOW + "Özet dosyasını isimlendirin (uzantısız): ") + '.txt'
                with open(file_name, 'w', encoding='utf-8') as f:
                    f.write(summary)
                print(Fore.YELLOW + f"Özet {file_name} olarak kaydedildi.")

            continue_choice = input(Fore.WHITE + "Devam etmek ister misiniz? (y/n): ")
            if continue_choice.lower() != 'y':
                print(Fore.RED + "Çıkılıyor...")
                break

        except (ValueError, IndexError):
            print(Fore.RED + "Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

