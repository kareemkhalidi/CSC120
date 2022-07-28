def main():
    while True:
        u = input()
        if(u.strip().lower() == "quit"):
            break
        else:
            print(len(u) - len(u.lstrip()))

main()