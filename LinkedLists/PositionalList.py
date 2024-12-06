# Assuming PositionalList is defined as provided
from PositionalList import PositionalList


def insertion_sort(pos_list, ascending=True):
    """Sort PositionalList using insertion sort."""
    if len(pos_list) > 1:  # More than one element
        marker = pos_list.first()  # Last sorted position
        while marker != pos_list.last():  # Continue until the end
            pivot = pos_list.after(marker)  # Next position to be sorted
            value = pivot.element()
            if (ascending and value >= marker.element()) or (not ascending and value <= marker.element()):
                marker = pivot  # Pivot is already sorted
            else:
                # Remove pivot and find new position
                pos_list.delete(pivot)
                walk = marker
                while walk != pos_list.first() and (
                        (ascending and value < pos_list.before(walk).element()) or
                        (not ascending and value > pos_list.before(walk).element())
                ):
                    walk = pos_list.before(walk)
                if (ascending and value < walk.element()) or (not ascending and value > walk.element()):
                    walk = pos_list.before(walk)
                pos_list.add_after(walk, value)
                marker = pos_list.after(marker) if marker != pos_list.last() else pos_list.last()


# Main program
if __name__ == "__main__":
    # Initialize the PositionalList
    pos_list = PositionalList()

    # Input numbers
    numbers = [1, 72, 81, 25, 65, 91, 11]

    # Add numbers to the positional list
    for number in numbers:
        pos_list.add_last(number)

    # Sort in ascending order
    insertion_sort(pos_list, ascending=True)
    print("Ascending order:", list(pos_list))

    # Reinsert numbers (since the list is already sorted)
    pos_list = PositionalList()
    for number in numbers:
        pos_list.add_last(number)

    # Sort in descending order
    insertion_sort(pos_list, ascending=False)
    print("Descending order:", list(pos_list))
