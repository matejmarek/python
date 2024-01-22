import os

output_list_folder = "C:/Users/machm/smahaj"
number_of_players = 8

all_code = '''
import random

number = random.randint(1, 5)
winners = set()
while True:
'''
define_code = '''
'''
tie_line = "True"
rest_code = f'''
'''
end = '''
    if winners:
        print(f"Player number {' and '.join(map(str, winners))} win.")
        break
'''

for i in range(number_of_players):
    define_code = define_code + f'''
    number_player{i} = int(input("\033[9{i}mPlayer {i} guess the number: \033[0m"))
    '''
    tie_line = tie_line + f" and number_player{i} == number"
    rest_code = rest_code + f'''
    if number_player{i} == number:
        winners.add({i})
'''

tie_code = f'''
    if {tie_line}:
        print("Tie.")
        break        
'''

new_list_path = os.path.join(output_list_folder, f"guess_game{number_of_players}.py")
with open(new_list_path, "w") as py_file:
    py_file.write(all_code)
    py_file.write(define_code)
    py_file.write("print()")
    py_file.write(tie_code)
    py_file.write(rest_code)
    py_file.write(end)
print(f"\033[92mDone!\033[0m")
