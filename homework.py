"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    return first == second;


print('for 1 and 1 values is_two_object_has_same_value function result is:')
print(str(is_two_object_has_same_value(1,1)))
print('for 1 and 2 values is_two_object_has_same_value function result is:')
print(str(is_two_object_has_same_value(1,2)))


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return type(first) == type(second);


print('for asd and dfsg the result of is_two_objects_has_same_type is:')
print(str(is_two_objects_has_same_type('asd','dfsg')))
print('for asd and 13 the result of is_two_objects_has_same_type is:')
print(str(is_two_objects_has_same_type('asd',13)))


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    return first is second;


print('for asd and dfsg the result of is_two_objects_is_the_same_objects is:')
print(str(is_two_objects_is_the_same_objects('asd','dfsg')))
print('for 13 and 13 the result of is_two_objects_is_the_same_objects is:')
print(str(is_two_objects_is_the_same_objects(13, 13)))


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if isinstance(first_value, int) and isinstance(second_value, int):
        return first_value*second_value
    else:
        raise Exception('ValueError')


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """

    try:
        int(first_value)
        int(second_value)
        return first_value*second_value

    except OurAwesomeException:
        print('not convertible input data')


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    pass


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    a = []
    for i in range(13):
        if i != 6 and i != 7:
            a.append(i)
        else:
            pass
    return a


print(some_loop_exercise())


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    pass


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    pass

def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    pass
