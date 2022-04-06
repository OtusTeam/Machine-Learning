import csv


def read_csv_cars():
    with open("cars.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for line_number, row in enumerate(csv_reader):
            if line_number == 0:
                print(" | ".join(row))
            else:
                print("Car by {vendor}, model: {model!r} for {price}".format(
                    vendor=row[1],
                    model=row[2],
                    price=row[4],
                ))


def read_csv_cars_as_dict():
    with open("cars.csv") as f:
        csv_reader = csv.DictReader(f, delimiter=",")
        print("Columns:", " | ".join(csv_reader.fieldnames))
        for row in csv_reader:
            # print(row)
            print("Car by {vendor}, model: {model!r} for {price}".format(
                vendor=row["Make"],
                model=row["Model"],
                price=row["Price"],
            ))


class FieldNames:
    NAME = "name"
    DEPARTMENT = "department"
    MONTH = "month"


def write_csv_dict():
    fieldnames = [
        FieldNames.NAME,
        FieldNames.DEPARTMENT,
        FieldNames.MONTH,
    ]
    with open("employees_bd_months.csv", "w") as f:
        csv_writer = csv.DictWriter(f, fieldnames)
        csv_writer.writeheader()

        row = {
            FieldNames.NAME: "John",
            FieldNames.DEPARTMENT: "HelpDesk",
            FieldNames.MONTH: "February",
        }
        csv_writer.writerow(row)

        row2 = {
            FieldNames.NAME: "Jack",
            FieldNames.DEPARTMENT: "IT",
            FieldNames.MONTH: "March",
        }
        row3 = {
            FieldNames.NAME: "Ann",
            FieldNames.DEPARTMENT: "Accounting",
            FieldNames.MONTH: "May",
        }
        csv_writer.writerows([row2, row3])


def main():
    # my_str = "foobar"
    # print(my_str)
    # print(repr(my_str))
    # print(f"my str: {my_str}")
    # print(f"my str: {my_str!r}")

    # read_csv_cars()
    # read_csv_cars_as_dict()
    write_csv_dict()


if __name__ == "__main__":
    main()
