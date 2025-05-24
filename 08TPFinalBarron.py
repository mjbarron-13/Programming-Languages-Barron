# Simulates per-session counter (stack-dynamic)
def session_counter():
    counter = 0  # reinitialized every call
    counter += 1
    print(f"Session visits: {counter}")

# Simulates persistent kiosk usage tracker (static-like)
def kiosk_usage():
    if not hasattr(kiosk_usage, "total_users"):
        kiosk_usage.total_users = 0  # initialize on first call
    kiosk_usage.total_users += 1
    print(f"Total users today: {kiosk_usage.total_users}")

# Main Program
def main():
    print("=== Simulating Kiosk Sessions ===")
    for i in range(3):
        print(f"\n--- Customer {i+1} ---")
        session_counter()  # should always print 1
        kiosk_usage()      # should increment each time

    print("\n=== Testing session_counter() resets ===")
    for i in range(5):
        session_counter()  # should print 1 every time

if __name__ == "__main__":
    main()
