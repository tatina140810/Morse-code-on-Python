dict = { "a": ".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..","m":"--", "n":"-.","o":"---", "p": ".--.", "q":"--.-","r":"._.", "s":"...", "t":"-","u":"..-", "v": "...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "1":".----","2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----"}
word = input("input word:").lower()
print(word)

letters = list(word)

value = [dict[i] for i in letters if i in dict]
print(f"Morse code: {str(value)}")


