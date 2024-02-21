from SignLanguageRecognition import signLanguageRecognizer
from PIL import Image
import matplotlib.pyplot as plt

option = None
while option not in ["1" or "2"]:
    option = input(
        "Welcome to the sign language progam\n\n1. Convert text to sign language\n2. Convert sign language to text\nEnter: "
    )

folder = r"images/"

letters_dict = {
    "A": "A.png",
    "B": "B.png",
    "C": "C.png",
    "D": "D.png",
    "E": "E.png",
    "F": "F.png",
    "G": "G.png",
    "H": "H.png",
    "I": "I.png",
    "J": "J.png",
    "K": "K.png",
    "L": "L.png",
    "M": "M.png",
    "N": "N.png",
    "O": "O.png",
    "P": "P.png",
    "Q": "Q.png",
    "R": "R.png",
    "S": "S.png",
    "T": "T.png",
    "U": "U.png",
    "V": "V.png",
    "W": "W.png",
    "X": "X.png",
    "Y": "Y.png",
    "Z": "Z.png",
    " ": "space.jpg",
}


def translate_text(text: str):
    text_list = list(text)
    text_list = [letter.upper() for letter in text_list]
    sign_images = []
    print(text_list)
    for letter in text_list:
        if letter in letters_dict.keys():
            path = folder + letters_dict[letter]
            image = Image.open(path)
            sign_images.append(image)
    return sign_images


if option == "1":
    text = input("What would you like to be converted to ASL?\nEnter: ")
    text_images = translate_text(text)
    plt.figure(figsize=(15, 15))
    for i in range(len(text_images)):
        plt.subplot(5, 10, i + 1)
        plt.imshow(text_images[i])
        plt.axis("off")
    plt.show()

elif option == "2":
    signLanguageRecognizer.signLanguageRecognizerMethod()
