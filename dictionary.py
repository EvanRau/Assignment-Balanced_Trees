###ICS 311 Assignment 2
###
###Authors: Evan Rau, Yuzuki Fujimoto

import bisect

###  Evan Rau
# For this assignment, we chose to use a python dictionary to implement the database, which itself is an implementation of a hash table.
# Hash tables are extremely efficient for single-entry lookups, providing an average complexity of O(1) so long as each key has its own hash in the table. 
# In a worst case scenario, every key is placed on the same hash, which effectively turns the dictionary into an array, giving a worst case complexity of O(n)
# see the following link for more information on python dicts https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# In addtion to the dictionary, we also keep a sorted list of its keys that we update with each insertion. Doing this allows us to improve time complexity for first(), last(), predecessor(),
# successor(), and listAllSayings at the cost of slowing down insert(). This improves the time complexity of first() and last() to O(1), list_all_sayings() to O(n), and predecessor() and successor() to O(logn)
# consequently, insert()'s time complextiy goes up from O(1) to O(logn) since it has to utilize bisect's functions to resort sorted_keys every time it is called.
# Additionally, bisect is used in predecessor and successor in order to determine where its key exists in the sorted list of entries, allowing for us to locate the key pairs that occur 
# before and after it. bisect_left uses a binary search so this is why the time complexities of these functions are O(logn)
# See https://docs.python.org/3/library/bisect.html for full documentation on the bisect import
###

class HawaiianDictionary:
    def __init__(self):
        self.sayings = {}
        self.sorted_keys = []

    def member(self, saying):
        return self.sayings.get(saying, "Saying not in Dictionary")

    def first(self):
        if self.sorted_keys:
            first_key = self.sorted_keys[0]
            return {first_key: self.sayings[first_key]}
        return "Dictionary Empty"

    def last(self):
        if self.sorted_keys:
            last_key = self.sorted_keys[-1]
            return {last_key: self.sayings[last_key]}
        return "Dictionary Empty"

    def predecessor(self, saying):
        index = bisect.bisect_left(self.sorted_keys, saying)
        if index == 0:
            return "First entry in dictionary; no predecessor"
        elif saying in self.sayings:
            predecessor_key = self.sorted_keys[index - 1]
            return {predecessor_key: self.sayings[predecessor_key]}
        return "Saying not in dictionary"

    def successor(self, saying):
        index = bisect.bisect_left(self.sorted_keys, saying)
        if saying not in self.sayings:
            return "Saying not in dictionary"
        elif index < len(self.sorted_keys) - 1:
            successor_key = self.sorted_keys[index + 1]
            return {successor_key: self.sayings[successor_key]}
        return "Last entry in dictionary; no successor"

    def insert(self, saying, translation, explanation_non_english, explanation_english):
        if saying not in self.sayings:
            bisect.insort_left(self.sorted_keys, saying)
        self.sayings[saying] = {
            'translation': translation,
            'explanation_non_english': explanation_non_english,
            'explanation_english': explanation_english
        }

    def list_all_sayings(self):
        if not self.sorted_keys:
            print("No sayings found in the dictionary.")
            return

        print("===== Hawaiian Sayings Dictionary =====")
        for saying in self.sorted_keys:
            details = self.sayings[saying]
            print(f"   Saying: {saying}")
            print(f"   Translation: {details['translation']}")
            print(f"   Explanation (Hawaiian): {details['explanation_non_english']}")
            print(f"   Explanation (English): {details['explanation_english']}")
            print()


    ### MeHua and WithWord programmed by Yuzuki Fujimoto
    # This function searches through all sayings in the dictionary and returns those containing the given non-English word.
    # It iterates through each saying and checks if the word is present in the saying field of each entry.
    # If a saying contains the word, it is added to the sayings_containing_word list, which is then returned.
    # MeHua searches for sayings containing a given non-English word by iterating through each entry in self.sayings and checking if the word appears in the 'saying' field.
    # This function searches and returns all the matching sayings. However, its efficiency is moderate, operating with a time complexity of O(n) where n is the number of entries,
    # and a space complexity  O(n) in worst-case scenario for every saying containing the word.
    # The WithWord function searches for sayings containing a given English word in either the 'translation' or 'explanation_english' fields.
    # Like MeHua, it iterates through each saying in self.sayings to see if the word appears in the specified fields, collecting and returning all matching sayings.
    # This also operates with O(n) time complexity and a corresponding space complexity for smaller datasets but it could be even slower for bigger dictionaries with more sayings.
    def MeHua(self, word):
        sayings_containing_word = []
        for saying, details in self.sayings.items():
            if word in saying:
                sayings_containing_word.append({saying: details})
        return sayings_containing_word

    def WithWord(self, word):
        sayings_containing_word = []
        for saying, details in self.sayings.items():
            if word in details['translation'] or word in details['explanation_english']:
                sayings_containing_word.append({saying: details})
        return sayings_containing_word


### Main code to prove functionality

db = HawaiianDictionary()

db.insert(
    saying="A‘ea‘e mōhala i luna o ke kukui.",
    translation="Whiteness unfolds on the kukui trees.",
    explanation_non_english="Hoʻohana ʻia e pili ana i ke kanaka hina hina, me ka hoʻohālikelike ʻana iā ia me ka lāʻau kukui mohala piha i nā pua keʻokeʻo",
    explanation_english="Used in reference to a person who grays, comparing him to a blooming kukui tree laden with white flowers."
)

db.insert(
    saying="E mālama i ka makua, he mea laha ‘ole; ‘o ke kāne he loa‘a i ka lā ho‘okahi.",
    translation="Take care of parents for they are choice; a husband can be found in a day.",
    explanation_non_english="Pono e mālama ʻia nā mākua, no ka mea, ke hala lākou, ʻaʻohe mea nāna e pani.",
    explanation_english="Parents should be cared for, for when they are gone, there are none to replace them."
)

db.insert(
    saying="I pa‘a i kona kupuna ‘a‘ole kākou e puka.",
    translation="Had our ancestress died in bearing our grandparent, we would not have come forth.",
    explanation_non_english="Ua ʻōlelo ʻia e hoʻomanaʻo i kekahi lālā o ka ʻohana e mahalo i ka laina kiʻekiʻe, no ka mea ua hele mai lākou ka mua.",
    explanation_english="Said to remind a member of the family to respect the senior line, because they came first."
)

db.insert(
    saying="Kālina ka pona, ‘a‘ohe hua o ka pu‘e, aia ka hua i ka lālā.",
    translation="The potato hill is bare of tubers for the plant no longer bears; it is the vines that are now bearing.",
    explanation_non_english="ʻAʻole hānau hou ka makuahine, akā ʻo kāna mau keiki.",
    explanation_english="The mother is no longer bearing, but her children are."
)

db.insert(
    saying="Ola ka inoa.",
    translation="The name lives.",
    explanation_non_english="Ua ʻōlelo ʻia ke hāʻawi ʻia ka inoa o kahi hoahānau aloha i make i kahi keiki.",
    explanation_english="Said when the name of a beloved deceased relative is given to a child."
)

db.insert(
    saying="Ola nā iwi.",
    translation="The bones live.",
    explanation_non_english="Wahi a kekahi ʻelemakule hanohano i mālama maikaʻi ʻia e kona ʻohana.",
    explanation_english="Said of a respected oldster who is well cared for by his family."
)

db.list_all_sayings()

### Out-of-order insert to prove alphabetical sorting is maintained

db.insert(
    saying="Ha‘a ka pelehū i ka haka; ha‘a ka ‘elemakule i ke ala; ha‘a ka luahine i ka hale.",
    translation="The turkey struts on the roost; the old man struts on the highway; the old woman struts in the house.",
    explanation_non_english="ʻAʻole i kaupalena ʻia nā wahi hōʻike i hoʻokahi wahi",
    explanation_english="Show places are not confined to a single locality."
)

db.list_all_sayings()

print("Predecessor Test")
print(db.predecessor('Ola ka inoa.')) # Output should be 'Kālina ka pona, ‘a‘ohe hua o ka pu‘e, aia ka hua i ka lālā.'
print()
print("Successor Test")
print(db.successor('Kālina ka pona, ‘a‘ohe hua o ka pu‘e, aia ka hua i ka lālā.')) # output should be 'Ola ka inoa.'
print()
print("First Test")
print(db.first()) #output should be 'A‘ea‘e mōhala i luna o ke kukui.'
print()
print("Last Test")
print(db.last()) #output should be 'Ola nā iwi.'
print()
print("MeHua Test")
print(db.MeHua("Ola"))
print()
print("WithWord Test")
print(db.WithWord("family"))
