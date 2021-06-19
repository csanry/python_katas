# who likes it, 6kyu

'''
You probably know the "like" system from Facebook and other pages.
Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.
It must return the display text as shown in the examples:

likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
'''

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} like this'
    }[min(4, n)].format(*names[:3], others = n-2)

print(likes(["Alex", "Jacob", "Mark", "Max"]))
print(likes(["Max", "John", "Mark"]))