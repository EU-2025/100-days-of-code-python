# 5. Print is your friend

# word_per_page = 0
# pages= int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# # print(word_per_page) # this variable has the wrogn value
# It is making a comparison insted of asigning the value
# total_words = pages * word_per_page
# print(total_words)

# print(f"word_per_page : {word_per_page}") # the bugs seems to ve in this part, so its better to chek in the code.
# print(f"pages : {pages}") # this seems to give the rigth value.
# print(f"total_words : {total_words}")

word_per_page = 0
pages= int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

