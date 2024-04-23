import sys
from pathlib import Path
from colorama import init, Fore, Style
init(autoreset=True)

def visualize_directory_structure(directory_path, indent=0):
    directory = Path(directory_path)
    
    if not directory.exists():
        print(Fore.RED + "Помилка,директорія не існує!")
        return
    
    if not directory.is_dir():
        print(Fore.RED + "Помилка,ваш шлях не вказує на директорію!")
        return
    print(" " * indent + Style.BRIGHT + Fore.BLUE + f"📁 {directory.name}/")
    
    for file in directory.iterdir():
        if file.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {file.name}")
    
    for subdir in directory.iterdir():
        if subdir.is_dir():
            visualize_directory_structure(subdir, indent + 2)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка,передайте шлях до директорії як аргумент командного рядка!")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    
    visualize_directory_structure(directory_path)
