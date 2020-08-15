def comma(lista):
    last_word = lista.pop()
    comma_add = ', '.join(lista)
    print(f'{comma_add.title()} and {last_word.title()}.')

if __name__ == "__main__":
    spam = ['apples', 'bananas', 'tofu', 'cats', 'dogs']
    lista = ['1', '2', '3']
    comma(spam)
    comma(lista)