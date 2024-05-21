#!/usr/bin/python3


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structure for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes (list, dictionary, string, integer, boolean).

    Returns:
        dict: A dictionary with serializable attributes of the object.
    """
    # Initialize an empty dictionary to store attribute-value pairs
    json_dict = {}

    # Iterate through the object's attributes
    for attr_name in dir(obj):
        # Skip private and special attributes
        if not attr_name.startswith("__"):
            # Get the attribute value
            attr_value = getattr(obj, attr_name)

            # Check if the attribute value is serializable
            if isinstance(attr_value, (list, dict, str, int, bool)):
                # Add the attribute-value pair to the dictionary
                json_dict[attr_name] = attr_value

    return json_dict

