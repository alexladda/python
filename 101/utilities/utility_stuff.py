class Shortner:
    def __init__(self, items):
        self.original_items = items
    def print_original_items(self):
        print(self.original_items)


class ListAndCharShortner(Shortner):
    def print_shortned_items(self):
        print(self.original_items[0:3])

class DictionaryShortner(Shortner):
    def print_shortned_items(self):
        dict = self.original_items
        short_dict = {}
        counter = 0
        for k, v in dict.items():
            if counter < 3:
                short_dict.update({k: v})
                # or: short_dict[k] = dict[k]
                counter += 1
        print(short_dict)

# silence is golden!
