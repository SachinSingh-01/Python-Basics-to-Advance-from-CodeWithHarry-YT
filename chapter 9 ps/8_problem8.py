# ishmai ek this.txt file bana kar wousmai kuch likh diya toh jab run kiya program ko tab apne aap ek new file this_copy.txt sai ek file bana or wo chij copy ho gya ish file mai


with open("this.txt") as f:
    content=f.read()

with  open("this_copey.txt", "w") as f:
    f.write(content)    