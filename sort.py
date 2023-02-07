from datetime import datetime


def sort_hw(homework: dict):
    for subject, details in homework.items():
        due_date = datetime.strptime(details["due"], "%Y/%m/%d")
        details["date"] = due_date
    
    sorted_subjects = sorted(homework.keys(), key=lambda x: homework[x]["due"], reverse=False)
    print(sorted_subjects)
    
    sorted_hw = {}
    for subject in sorted_subjects:
        due_date = homework[subject]["due"]
        sorted_hw[subject] = {
            "due_date": due_date,
            "description": homework[subject]["description"],
            "completed": homework[subject]["completed"],
            "id": homework[subject]["id"],
            "show": homework[subject]["show"]
        }
    print(sorted_hw)
    return sorted_hw
