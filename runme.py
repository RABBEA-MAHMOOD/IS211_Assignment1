class Book:
    def __init__(self, author, title):
        """
        constructor a book with author and title

        :param author: The author of a book
        :param title: The title of a book
        """
        self.author = author
        self.title = title

    def display(self):
        """Display the author and title of a book"""
        print(f"I am {self.author} and my book is {self.title}")


if __name__ == "__main__":
    a = Book ("James Clear" , "Atomic habit")


    a.display()