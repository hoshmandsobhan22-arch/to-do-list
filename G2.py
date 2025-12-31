print("welcome to my to do list")

class works:
    def __init__(self, name):
        self.name = name

my_work = []

class to_do_list:
    def __init__(self, name):
        while True:
            your_work = input(
                f"dear {name} please enter your work name "
                "(or press s to stop): "
            )
            if your_work == "s":
                break
            my_work.append(your_work)

        print(f"ok {name} these are your works", my_work)

        while True:
            coustomer = input(
                f"dear {name} if you did your job say the job name "
                "(press s to stop): "
            )

            if coustomer == "s":
                break
            elif coustomer in my_work:
                my_work.remove(coustomer)
            else:
                print("we cant help you")

            print(f"well done {name} thats your Remaining tasks for today", my_work)


class1 = works(input("please enter your name: "))
class2 = to_do_list(class1.name)
