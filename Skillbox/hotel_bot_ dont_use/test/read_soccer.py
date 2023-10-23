import json
def get_leagues():
    with open('soccer.json', 'r', encoding='utf-8') as s:
        print(json.load(s))


def main():
    get_leagues()
if __name__ == '__main__':    main()