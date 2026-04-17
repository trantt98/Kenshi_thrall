correct = "correct.txt"
wrong = "false.txt"

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def put_correct_word(string: str):
    with open(correct,"a") as f:
        f.write(string)
        f.write(" ")

def put_false_word(string: str):
    with open(wrong,"a") as f:
        f.write(string)
        f.write(" ")

def file_contains(filename:str,word:str):
    with open(filename,"r") as f:
        content = f.read()
        if word in content:
            return True
        else :
            return False

def questions(x:int):
    to_sort = []
    print("give in the questions")
    for i in range(x):
       to_check = input()
       to_sort.append(to_check)

    for i in range(x):

        if file_contains(correct, to_sort[i]):
            print_green("this word is true")
            print(" "+ to_sort[i])

        elif file_contains(wrong,to_sort[i]):
            print_red("this word is wrong")
            print(" " + to_sort[i])

       
        else: 
            print("did the question fail? n/number")
            answer = input()
            if(answer == "n"):
                print("which one is correct?")
                number = input()
                index = int(number) -1
                put_correct_word(to_sort.pop(index))

            for i in range(len(to_sort)):
                if file_contains(wrong,to_sort[i]) == False:
                    put_false_word(to_sort[i])

            else: 
                put_false_word(to_sort[int(answer)-1])
                break


for i in range(1000):
    print("how many questions")
    amount = input()
    questions(int(amount))
