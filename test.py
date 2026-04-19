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
        keywords = content.split(' ')
        if word in keywords:
            return True
        else :
            return False

def questions(x:int):
    to_sort = []
    print("give in the questions")
    
    for i in range(x):
        to_check = input()
        to_sort.append(to_check)

        if file_contains(correct, to_sort[i]):
            print_green("this word is true")
            print(" " + to_sort[i])

        elif file_contains(wrong, to_sort[i]):
            print_red("this word is wrong")
            print(" " + to_sort[i])
   



              
    print("did the question fail? n/number")
    answer = input()
    if(answer == "n"):
        print("which one is correct?")
        number = input()
        if file_contains(correct,to_sort[int(number)-1]) :  
                print("already registered")
        else:
            put_correct_word(to_sort[int(number)-1])

    else: 
        if file_contains(correct,to_sort[int(number)-1]) : 
            print(" ")
        else: 
            put_false_word(to_sort[int(answer)-1])


for i in range(1000):
    print("how many questions")
    amount = input()
    questions(int(amount))
