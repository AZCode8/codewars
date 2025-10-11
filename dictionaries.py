'''
Practicing directories and funtions
'''


def main():
    id_card = {"name": "Charles Magna"}
    id_card.update({"subject": "Math", "grade": "A"})
    print(id_card)
    print(create_report(id_card))


def create_report(id_card):
    return f"""
    =========== REPORT ===========

    Name: {id_card.get("name", "user not found")}
    Subject: {id_card.get("subject", "no subject found")}
    Grade: {id_card.get("grade", "no grade assigned")}

    ==============================
    """


main()
