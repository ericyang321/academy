from binary_search import binary_search

def main():
    data = [1, 3, 4, 5, 6, 7, 13, 15, 67, 68]
    print(binary_search(data, 68, 0, len(data)))
    return


if __name__ == "__main__":
    main()
