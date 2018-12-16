from manager import train_rf_squad, train_rf_duo

def main():
    # Training the models using three algorithms for 2 and 4 players team
    train_rf_squad()
    train_rf_duo()

if __name__ == '__main__':
    main()
