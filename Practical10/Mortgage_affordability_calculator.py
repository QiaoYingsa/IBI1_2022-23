def can_buy_house(x, y):
    """
    Determines whether an individual can buy a specific house based on the total value of the house
    and the purchaser's annual salary.

    Args:
        x (float): The total value of the house.
        y (float): The purchaser's annual salary.

    Returns:
        str: 'Yes' if the individual can buy the house, 'No' otherwise.
    """
    max_house_value = y * 5
    if x <= max_house_value:
        return 'Yes'
    else:
        return 'No'
# Example 1
x1 = 180000
y1 = 35000
result1 = can_buy_house(x1, y1)
print(result1)  # Output: 'Yes'

# Example 2
x2 = 500000
y2 = 80000
result2 = can_buy_house(x2, y2)
print(result2)  # Output: 'No'

