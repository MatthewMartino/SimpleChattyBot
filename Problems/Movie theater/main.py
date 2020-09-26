halls = int(input())
capacity = int(input())
viewers = int(input())
viable = None

if viewers > halls * capacity:
    viable = False

else:
    viable = True

print(viable)
