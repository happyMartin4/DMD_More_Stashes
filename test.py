def main():
    string = 'this is a string talking about bob, alice, bob, and eve'
    parts = string.split('bob', 1)
    string = "tim".join(parts)
    print(string)


if __name__ == '__main__':
    main()