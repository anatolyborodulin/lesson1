user_text='2+1='

sym_index = 0
for sym in user_text:
	sym_index = sym_index + 1
	if sym == "+":
		sign_pos = sym_index
		print(sign_pos)
	elif sym == "=":
		equal_pos = sym_index
		print(equal_pos)

for sym in user_text:
	first_part = sym