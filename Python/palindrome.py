text = input("Enter a text:")
txt_list = []
reverse_list = []
for i in text:
    txt_list.append(i)

for i in range(len(text)-1, -1, -1):
    reverse_list.append(text[i])

if txt_list == reverse_list:
    print("palindrom!")
else:
    print("Not palindrom!")
