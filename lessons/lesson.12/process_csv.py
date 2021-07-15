import csv


def read_csv_cars():
    with open("cars.csv", "r") as f:
        csv_reader = csv.reader(f, delimiter=",")
        # for row in csv_reader:
        #     print(row)

        for line_no, row in enumerate(csv_reader):
            if line_no == 0:
                print("Headers:", ", ".join(row))
            else:
                print("Car by {vendor} {model!r} ({year}, {description}) for ${price}".format(
                    vendor=row[1],
                    model=row[2],
                    year=row[0],
                    description=row[3],
                    price=row[4],
                ))
                # print(row)


def read_csv_cars_dict():
    with open("cars.csv", "r") as f:
        csv_reader = csv.DictReader(f, delimiter=",")

        print("Headers:", ", ".join(csv_reader.fieldnames))

        for row in csv_reader:
            print("Car by {vendor} {model!r} ({year}, {description}) for ${price}".format(
                vendor=row['Make'],
                model=row['Model'],
                year=row['Year'],
                description=row['Description'],
                price=row['Price'],
            ))


def write_csv_dict():
    FIELD_NAME = "name"
    FIELD_DEPARTMENT = "department"
    FIELD_MONTH = "month"

    fieldnames = [
        FIELD_NAME,
        FIELD_DEPARTMENT,
        FIELD_MONTH,
    ]

    with open("employees_birth_months.csv", "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()

        john_data = {
            FIELD_NAME: "John Smith",
            FIELD_DEPARTMENT: "Helpdesk",
            FIELD_MONTH: "May",
        }
        csv_writer.writerow(john_data)

        sam_data = {
            FIELD_NAME: "Sam Brown",
            FIELD_DEPARTMENT: "IT",
            FIELD_MONTH: "November",
        }
        csv_writer.writerow(sam_data)

        # csv_writer.writerows([john_data, sam_data])


def main():
    # read_csv_cars()
    # read_csv_cars_dict()
    write_csv_dict()


if __name__ == '__main__':
    main()
