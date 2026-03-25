def main():
    print("App started")

    if feature_login_enabled:
        print("Login feature is ON")
        print("User can now log in 🚀")  # ← новая строка
    else:
        print("Login feature is OFF")
