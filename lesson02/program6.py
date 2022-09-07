main_string = input('Enter main string :')
sub_string = input('Enter substring :')

range_len = len(main_string) - len(sub_string) + 1

counter = 0
for i in range(range_len):
    if main_string[i:i + len(sub_string)] == sub_string:
        counter += 1

print(f"Substring in string {counter} times")