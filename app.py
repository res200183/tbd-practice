feature_login_enabled = False

def main():
    print("App started")

    if feature_login_enabled:
        print("Login feature is ON")
    else:
        print("Login feature is OFF")

if __name__ == "__main__":
    main()
