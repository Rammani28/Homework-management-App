import json


def delete_hw(user: str, subject: str, hw_id: int | str) -> None:
    
    """deletes  a homework of specified user's specified subject with provided hw_id"""
    
    with open('data.json') as read_file:
        whole_data = json.load(read_file)
        # whole_data.
    pass


# removed_value = test_dict.pop('Mani')