text = "Python"
print(text)

textReverse = ""

for i in range(len(text)-1, -1, -1):
    textReverse += text[i]

print(textReverse)
