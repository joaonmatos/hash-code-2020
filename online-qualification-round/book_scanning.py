import sys

def offset(book, library):
    return book + library * noBooks

lines = sys.stdin.readlines()

books = []
libraries = []
ocurrences = []
days = 0
noLibraries = 0
noBooks = 0

readFirstLine = False
readSecondLine = False
odd = True
library = 0
for line in lines:
    if not readFirstLine:
        numbers = line.split()
        noBooks = int(numbers[0])
        noLibraries = int(numbers[1])
        ocurrences = [False] * (noBooks * noLibraries)
        days = int(numbers[2])
        readFirstLine = True
    elif not readSecondLine:
        for score in line.split():
            books.append(int(score))
        readSecondLine = True
    elif odd:
        if library >= noLibraries:
            break
        numbers = line.split()
        signup = int(numbers[1])
        rate = int(numbers[2])
        libraries.append((signup, rate))
        odd = False
    else:
        for book in line.split():
            ocurrences[offset(int(book), library)] = True
        odd = True
        library += 1

def libraryBooks(library):
    libraryBooks = []
    for book in range(noBooks):
        if ocurrences[offset(book, library)]:
            libraryBooks.append((book, books[book]))
    return libraryBooks

def bookTupleToScore(book):
    (_, score) = book
    return score

def maxLibraryScore(library, day):
    (signupDays, booksPerDay) = libraries[library]
    operationStartDay = day + signupDays
    scores = libraryBooks(library)
    scores.sort(reverse=True,key=bookTupleToScore)
    totalScore = 0
    totalBooks = min(len(scores), (days - operationStartDay) * booksPerDay)
    for book in range(totalBooks):
        totalScore += bookTupleToScore(scores[book])
    return totalScore

def deleteBookOcurrences(book):
    for library in range(noLibraries):
        ocurrences[offset(book, library)] = False

def nextLibrary(day):
    maxScore = 0
    selectedLibrary = -1
    for library in range(noLibraries):
        score = maxLibraryScore(library, day)
        if score > maxScore and not processedLibraries[library]:
            selectedLibrary = library
            maxScore = score
    return selectedLibrary

def pickedBooks(library, day):
    (signupDays, booksPerDay) = libraries[library]
    operationStartDay = day + signupDays
    books = libraryBooks(library)
    books.sort(reverse=True,key=bookTupleToScore)
    totalBooks = min(len(books), (days - operationStartDay) * booksPerDay)
    out = []
    for book in range(totalBooks):
        (bookId, _) = books[book]
        out.append(bookId)
    return out

currentDay = 0
processedLibraries = [False] * noLibraries
selectedLibraries = []
while currentDay < days and len(selectedLibraries) < len(libraries):
    lib = nextLibrary(currentDay)
    picked = pickedBooks(lib, currentDay)
    (signup, _) = libraries[lib]
    currentDay += signup
    for book in picked:
        deleteBookOcurrences(book)
    selectedLibraries.append((lib, len(picked), picked))

print(len(selectedLibraries))
for selected in selectedLibraries:
    (lib, n, picked) = selected
    pickedStr = []
    for book in picked:
        pickedStr.append(str(book))
    print(lib, n)
    print(" ".join(pickedStr))
