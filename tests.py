from functions.get_files_info import get_files_info

def main():
    pkgs = ['.', 'pkg', '/bin', '../']
    for pkg in pkgs:
        if pkg == '.':
            print("Result for current directory:")
        else:
            print(f"Result for '{pkg}' directory:")
        print(get_files_info("calculator", pkg))
        print()


if __name__ == "__main__":
    main()