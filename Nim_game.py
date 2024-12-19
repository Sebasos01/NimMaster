def nim_game(heaps):
    if len(heaps) != 4:
        return "Error: Please enter a tuple of 4 positive integers."
    for h in heaps:
        if not isinstance(h, int) or h < 0:
            return "Error: All heap sizes must be non-negative integers."
    nim_sum = 0
    for h in heaps:
        nim_sum ^= h
    if nim_sum == 0:
        return "The second player has a winning strategy."
    else:
        for i, h in enumerate(heaps):
            target_heap_size = h ^ nim_sum
            if target_heap_size < h:
                amount_to_remove = h - target_heap_size
                heap_number = i + 1
                return (f"The first player has a winning strategy.\n"
                        f"The first player should remove {amount_to_remove} "
                        f"coin{'s' if amount_to_remove > 1 else ''} from heap {heap_number}.")
        return "Error: No valid move found."

heaps_3 = [(4, 2, 0, 0), (50, 25, 0, 0), (8, 8, 0, 0), (15, 15, 0, 0), (2, 4, 6, 8)]
for heap in heaps_3:
    print(heap)
    print(nim_game(heap) + "\n")

heaps_4 = [(10, 10, 10, 10), (12, 10, 10, 10)]
for heap in heaps_4:
    print(heap)
    print(nim_game(heap) + "\n")

def nim_game_play():
    print("LET'S PLAY NIM :)")
    while True:
        try:
            initial_input = input("Enter the sizes of the 4 heaps, separated by spaces: ")
            heap_sizes = list(map(int, initial_input.strip().split()))
            if len(heap_sizes) != 4:
                print("Please enter exactly 4 numbers.")
                continue
            if any(h < 0 for h in heap_sizes):
                print("Heap sizes must be non-negative integers.")
                continue
            break
        except ValueError:
            print("Invalid input. Enter 4 non-negative integers separated by spaces.")
            continue

    heaps = heap_sizes.copy()
    game_over = False
    turn = "machine"

    while not game_over:
        print("\nCurrent heap sizes:")
        for i, h in enumerate(heaps):
            print(f"Heap {i+1}: {h}")

        if turn == "machine":
            nim_sum = 0
            for h in heaps:
                nim_sum ^= h

            if nim_sum == 0:
                for i, h in enumerate(heaps):
                    if h > 0:
                        heap_index = i
                        amount_to_remove = 1
                        break
            else:
                for i, h in enumerate(heaps):
                    target_heap_size = h ^ nim_sum
                    if target_heap_size < h:
                        heap_index = i
                        amount_to_remove = h - target_heap_size
                        break

            heaps[heap_index] -= amount_to_remove
            print(f"\nThe machine removes {amount_to_remove} coin{'s' if amount_to_remove > 1 else ''} from heap {heap_index+1}.")
            turn = "human"
        else:
            if all(h == 0 for h in heaps):
                game_over = True
                break

            while True:
                try:
                    heap_num_input = input("\nYour turn. Enter the number of the heap (1-4) you want to take coins from: ")
                    heap_index = int(heap_num_input) - 1
                    if heap_index < 0 or heap_index >= 4:
                        print("Invalid heap number. Enter a number between 1 and 4.")
                        continue
                    if heaps[heap_index] == 0:
                        print(f"Heap {heap_index+1} is empty. Choose a non-empty heap.")
                        continue

                    amount_input = input(f"Enter the number of coins you want to remove from heap {heap_index+1} (1 to {heaps[heap_index]}): ")
                    amount_to_remove = int(amount_input)
                    if amount_to_remove < 1 or amount_to_remove > heaps[heap_index]:
                        print(f"Invalid amount. You can remove between 1 and {heaps[heap_index]} coins from heap {heap_index+1}.")
                        continue

                    break
                except ValueError:
                    print("Invalid input. Please enter only integers.")
                    continue

            heaps[heap_index] -= amount_to_remove
            print(f"\nYou removed {amount_to_remove} coin{'s' if amount_to_remove > 1 else ''} from heap {heap_index+1}.")
            turn = "machine"

        if all(h == 0 for h in heaps):
            game_over = True

    if turn == "human":
        print("\nGame over. The machine wins!")
    else:
        print("\nGame over. You win!")

nim_game_play()
