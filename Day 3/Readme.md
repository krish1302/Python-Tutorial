# Built-in Datatypes

1. List - [] - list() - it will accept iterable 
    1. `List is a collection which is ordered and changeable. Allows duplicate members`
    2. index - position
    3. slicing - [start:end]
    4. index, slicing with change
    5. append - add to last
    6. insert - add to position
    7. remove - remove value, mulitple items means remove first occurance
    8. pop - remove with position or last item4
    9. clear - empty the list
    10. sort - asc / desc
    11. copy
    12. extend - update two list together
    13. count
    14. reverse
    15. in
    16. del
2. Tuple - () - tuple() - it will accept iterable 
    1. index
    2. slicing
    3. + - tuple + tuple
    4. count
    5. in
    6. del
3. Set - {}
    1. in
    2. add
    3. update / union - like extend in list
    4. remove / discard
    5. del
    add()	Adds an element to the set
    clear()	Removes all the elements from the set
    copy()	Returns a copy of the set
    difference()	Returns a set containing the difference between two or more sets
    difference_update()	Removes the items in this set that are also included in another, specified set
    discard()	Remove the specified item
    intersection()	Returns a set, that is the intersection of two other sets
    intersection_update()	Removes the items in this set that are not present in other, specified set(s)
    isdisjoint()	Returns whether two sets have a intersection or not
    issubset()	Returns whether another set contains this set or not
    issuperset()	Returns whether this set contains another set or not
    pop()	Removes an element from the set
    remove()	Removes the specified element
    symmetric_difference()	Returns a set with the symmetric differences of two sets
    symmetric_difference_update()	inserts the symmetric differences from this set and another
    union()	Return a set containing the union of sets
    update()	Update the set with the union of this set and others
4. Dict - {key: value}
    clear()	Removes all the elements from the dictionary
    copy()	Returns a copy of the dictionary
    fromkeys()	Returns a dictionary with the specified keys and value
    get()	Returns the value of the specified key
    items()	Returns a list containing a tuple for each key value pair
    keys()	Returns a list containing the dictionary's keys
    pop()	Removes the element with the specified key
    popitem()	Removes the last inserted key-value pair
    setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
    update()	Updates the dictionary with the specified key-value pairs
    values()	Returns a list of all the values in the dictionary

1. Mutable - it can be change, it will modify on same object - list, set, dict
2. Immutable - it can't be change, it will create a new object - int, str, tuple



