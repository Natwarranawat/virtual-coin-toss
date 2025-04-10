import random
import time

class CoinToss:
    def __init__(self):
        self.session_history = []
        self.current_session = {"heads": 0, "tails": 0, "total": 0}
    
    def flip_coin(self):
        """Simulates a single coin flip and returns the result."""
        result = random.choice(["Heads", "Tails"])
        return result
    
    def perform_tosses(self, num_tosses):
        """Performs multiple coin tosses and records the results."""
        results = []
        heads_count = 0
        tails_count = 0
        
        print("\nFlipping coins...")
        time.sleep(0.5)  # Small delay for effect
        
        for i in range(num_tosses):
            result = self.flip_coin()
            results.append(result)
            
            # Update counts
            if result == "Heads":
                heads_count += 1
            else:
                tails_count += 1
                
            # Display individual toss result with a small delay
            print(f"Flip {i+1}: {result}")
            time.sleep(0.1)  # Small delay between flips for visual effect
        
        # Update current session data
        self.current_session["heads"] += heads_count
        self.current_session["tails"] += tails_count
        self.current_session["total"] += num_tosses
        
        return results, heads_count, tails_count
    
    def display_results(self, heads_count, tails_count, total_flips):
        """Displays the results of the coin tosses."""
        print("\n===== Results =====")
        print(f"Total flips: {total_flips}")
        print(f"Heads: {heads_count} ({(heads_count/total_flips)*100:.2f}%)")
        print(f"Tails: {tails_count} ({(tails_count/total_flips)*100:.2f}%)")
        print("==================\n")
    
    def save_session(self):
        """Saves the current session results to history."""
        if self.current_session["total"] > 0:
            self.session_history.append(dict(self.current_session))
            # Reset current session
            self.current_session = {"heads": 0, "tails": 0, "total": 0}
    
    def display_session_history(self):
        """Displays the history of all sessions."""
        if not self.session_history:
            print("\nNo previous sessions found.")
            return
            
        print("\n===== Session History =====")
        for i, session in enumerate(self.session_history):
            print(f"Session {i+1}:")
            print(f"  Total flips: {session['total']}")
            print(f"  Heads: {session['heads']} ({(session['heads']/session['total'])*100:.2f}%)")
            print(f"  Tails: {session['tails']} ({(session['tails']/session['total'])*100:.2f}%)")
        print("==========================\n")


def main():
    print("Welcome to the Virtual Coin Toss Simulator!")
    print("This program allows you to simulate flipping a coin multiple times.\n")
    
    coin_toss = CoinToss()
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Flip coins")
        print("2. View session history")
        print("3. Exit program")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            # Get number of tosses
            while True:
                try:
                    num_tosses = int(input("\nHow many times would you like to flip the coin? "))
                    if num_tosses <= 0:
                        print("Please enter a positive number.")
                    else:
                        break
                except ValueError:
                    print("Please enter a valid number.")
            
            # Perform the tosses
            results, heads_count, tails_count = coin_toss.perform_tosses(num_tosses)
            
            # Display results
            coin_toss.display_results(heads_count, tails_count, num_tosses)
            
            # Ask if user wants to save this session
            save_choice = input("Would you like to save this session? (y/n): ").lower()
            if save_choice == 'y' or save_choice == 'yes':
                coin_toss.save_session()
                print("Session saved!")
            
        elif choice == "2":
            coin_toss.display_session_history()
            
        elif choice == "3":
            print("\nThank you for using the Virtual Coin Toss Simulator. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()