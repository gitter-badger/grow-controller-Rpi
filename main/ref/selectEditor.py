while True:
    print("Select Default Editor")
    print("1) emacs")
    print("2) nano")
    print("1) Vim/Vi")
    var1 = input("[1,2,3]:\n")
    if (var1 != "2"):
        print("try again")
    if (var1 == "2"):
        print("good choice")
        exit()
