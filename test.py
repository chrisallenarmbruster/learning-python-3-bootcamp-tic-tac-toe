print("\033[91;1m\u2665\033[00m\033[90;1m\u2660\033[00m\033[91;1m\u2666\033[00m\u2663\U0001f0a1 \U0001f0da \U0001f0da \U00002684")


def ask():
    while True:
        try: 
            p = input("Enter number: ")
            p = (int(p))**2
        except:
            print("Input error, try again.")
            continue
        else:
            print(p)
            break

    print("All done!")

ask()