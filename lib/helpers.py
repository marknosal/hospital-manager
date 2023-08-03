def selected_id_class(selected_class, class_name):
    all_rows = session.query(selected_class).all()
    [print(row) for row in all_rows]

    while True:
        selected_id = input(f'Please enter the ID of the {class_name} you would like to update: ')
        try:
            if int(selected_id) in [row.id for row in all_rows]:
                return selected_id
            else:
                print(f'Please enter a valid ID from the list of {class_name}s')
        except ValueError:
            print('Enter a valid ID. Whole Number.')