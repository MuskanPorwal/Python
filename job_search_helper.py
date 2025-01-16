import random
import os

# File paths
COMPANY_LIST_FILE = "companies.txt"
CHECKED_COMPANIES_FILE = "checked_companies.txt"

def load_companies():
    # Load the full list of companies
    if not os.path.exists(COMPANY_LIST_FILE):
        print(f"Error: {COMPANY_LIST_FILE} not found!")
        return []
    with open(COMPANY_LIST_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def load_checked_companies():
    # Load the list of already checked companies
    if not os.path.exists(CHECKED_COMPANIES_FILE):
        return []
    with open(CHECKED_COMPANIES_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def save_checked_companies(checked_companies):
    # Save the updated list of checked companies
    with open(CHECKED_COMPANIES_FILE, "w") as f:
        f.write("\n".join(checked_companies))

def select_random_companies(companies, checked_companies, count=5):
    # Get companies that haven't been checked
    unchecked_companies = list(set(companies) - set(checked_companies))
    if len(unchecked_companies) == 0:
        print("All companies have been checked! Reset to start over.")
        return []
    return random.sample(unchecked_companies, min(count, len(unchecked_companies)))

def main():
    print("\n=== Job Search Helper ===")
    companies = load_companies()
    checked_companies = load_checked_companies()
    
    if not companies:
        return
    
    while True:
        print("\nOptions:")
        print("1. Select 5 random companies to check.")
        print("2. Reset the process.")
        print("3. Exit.")
        
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == "1":
            selected_companies = select_random_companies(companies, checked_companies)
            if selected_companies:
                print("\nToday's Companies to Check:")
                print("\n".join(selected_companies))
                checked_companies.extend(selected_companies)
                save_checked_companies(checked_companies)
        elif choice == "2":
            if os.path.exists(CHECKED_COMPANIES_FILE):
                os.remove(CHECKED_COMPANIES_FILE)
            print("Reset successful! All companies are now available.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
