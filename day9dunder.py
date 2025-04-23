class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages

b1 = Book("Python Mastery", 300)
print(b1)         # 👈 __str__() chalta hai
print(len(b1))    # 👈 __len__() chalta hai
