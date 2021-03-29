from utilities.utility_stuff import ListAndCharShortner, DictionaryShortner


mylistshortner = ListAndCharShortner([1,2,3,4,5])
mylistshortner.print_original_items()
mylistshortner.print_shortned_items()

mydictshortner = DictionaryShortner({1: 'mike', 2: 'tom', 3: 'rebecca', 4: 'mike', 5: 'paul', })
mydictshortner.print_original_items()
mydictshortner.print_shortned_items()
# {1: 'mike', 2: 'tom', 3: 'rebecca', 4: 'mike', 5: 'paul', }
