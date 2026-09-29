# People Counter - Python Project for Foreign Job
# Developed by: aishwaryapujari670-a11y

count = 0

def people_counter():
    global count
    print("=== Smart People Counter ===")
    while True:
        action = input("Enter 'in' / 'out' / 'q': ").lower()
        if action == 'in':
            count += 1
            print(f"Person IN -> Total inside: {count}")
        elif action == 'out':
            count -= 1
            if count < 0:
                count = 0
            print(f"Person OUT -> Total inside: {count}")
        elif action == 'q':
            break
        else:
            print("Invalid input")
    
    print(f"Final count: {count}")

if __name__ == "__main__":
    people_counter()