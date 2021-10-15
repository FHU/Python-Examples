
def vol_of_box(height, width, length):
    value = int(height) * int(width) * int(length)
    return value

def vol_of_box_with_user_menu():
    h = input()
    w = input()
    l = input()
    vol = int(h) * int(w) * int(l)
    print(vol)

def user_menu():
    h = input()
    w = input()
    l = input()
    vol = vol_of_box(width=w,height=h,length=l)
    print(vol)

if __name__ == "__main__":
    user_menu()