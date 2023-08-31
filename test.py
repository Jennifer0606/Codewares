def VendingMachine(num_items, item_coins):
    if num_items % item_coins == 0:
        print(num_items // item_coins)
    pass


VendingMachine(10, 2)
