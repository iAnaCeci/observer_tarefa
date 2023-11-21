class WordCounter:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, phrase):
        for observer in self.observers:
            observer.update(phrase)

    def count_words(self, phrase):
        word_list = phrase.split()
        total_words = len(word_list)
        even_length_words = len([word for word in word_list if len(word) % 2 == 0])
        uppercase_words = len([word for word in word_list if word.istitle()])

        self.notify_observers(phrase)

        return {
            "Total Words": total_words,
            "Even Length Words": even_length_words,
            "Uppercase Words": uppercase_words,
        }

class WordCounterObserver:
    def update(self, phrase):
        pass

class PrintObserver(WordCounterObserver):
    def update(self, phrase):
        print("Resultado")
        print(WordCounter().count_words(phrase))



word_counter = WordCounter()
print_observer = PrintObserver()

word_counter.register_observer(print_observer)

frase = input("Digite uma frase: ")
word_counter.count_words(frase)
