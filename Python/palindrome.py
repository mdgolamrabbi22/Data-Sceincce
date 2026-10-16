text = input("Enter a text:")
text_list = []
reverse_list = []
for i in text:
    text_list.append(i)

for i in range(len(text)-1, -1, -1):
    reverse_list.append(text[i])

if text_list == reverse_list:
    print(f"{text} palindrom!")
else:
    print(f"{text} Not palindrom!")
