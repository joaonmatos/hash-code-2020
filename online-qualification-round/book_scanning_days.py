# Copyright 2020 Carlos J. Albuquerque, João N. Matos, João V. de Macedo & J. Miguel Simões
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys

def offset(book, library):
    return book + library * noBooks

lines = sys.stdin.readlines()

books = []
libraries = []
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
        libraries.append([signup, rate])
        odd = False
    else:
        ocurrences = {}
        for book in line.split():
            bookId = int(book)
            bookScore = books[bookId]
            ocurrences[bookId] = bookScore
        libraries[library].append(ocurrences)
        odd = True
        library += 1

def libraryBooks(lib):
    ocurrences = libraries[lib][2]
    libraryBooks = []
    for book in ocurrences:
        libraryBooks.append((book, ocurrences[book]))
    return libraryBooks

def bookTupleToScore(book):
    (_, score) = book
    return score

def maxLibraryScore(library, day):
    lib = libraries[library]
    signupDays = lib[0]
    booksPerDay = lib[1]
    operationStartDay = day + signupDays
    scores = libraryBooks(library)
    scores.sort(reverse=True,key=bookTupleToScore)
    totalScore = 0
    totalBooks = min(len(scores), (days - operationStartDay) * booksPerDay)
    for book in range(totalBooks):
        totalScore += bookTupleToScore(scores[book])
    return totalScore

def deleteBookOcurrences(book):
    for library in libraries:
        ocurrences = library[2]
        if book in ocurrences:
            ocurrences.pop(book)

def nextLibrary(day):
    minDays = days
    maxScore = 0
    selectedLibrary = -1
    for library in range(noLibraries):
        signup = libraries[library][0]
        score = maxLibraryScore(library, day)
        if score == 0 or processedLibraries[library]:
            continue
        if score/signup > maxScore/minDays:
            selectedLibrary = library
            maxScore = score
            minDays = signup
    return selectedLibrary

def pickedBooks(library, day):
    lib = libraries[library]
    signupDays = lib[0]
    booksPerDay = lib[1]
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
    if lib == -1:
        break
    processedLibraries[lib] = True
    picked = pickedBooks(lib, currentDay)
    signup = libraries[lib][0]
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
