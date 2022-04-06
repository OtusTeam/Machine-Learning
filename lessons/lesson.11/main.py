import json
from pprint import pprint


def main():
    json_string = "{\n\t\"foo\": \"bar\",\n\t\"fizz\": \"buzz\"\n}"
    print(json_string)
    print(repr(json_string))
    print(json_string[3:10])

    json_data = json.loads(json_string)
    print(json_data)
    print(repr(json_data))
    print(json_data["foo"])
    print(json_data["fizz"])

    json_string2 = "[\n\t{\n\t\t\"foo\": \"bar\",\n\t\t\"fizz\": \"buzz\"\n\t},\n\t{\n\t\t\"spam\": \"eggs\",\n\t\t\"nested\": {\n\t\t\t\"key\": \"value\",\n\t\t\t\"inner\": {\n\t\t\t\t\"some_array\": [\n\t\t\t\t\t1,\n\t\t\t\t\tnull,\n\t\t\t\t\ttrue,\n\t\t\t\t\tfalse,\n\t\t\t\t\t1234\n\t\t\t\t]\n\t\t\t}\n\t\t}\n\t}\n]"
    print(json_string2)
    json_data2 = json.loads(json_string2)
    print(json_data2)
    obj2 = json_data2[1]
    print(obj2)
    print(obj2["nested"])
    print(obj2["nested"]["inner"])

    my_data = {}
    my_data["foo"] = "bar"
    my_data["foo"] = "baz"
    print(my_data)

    another_json_string = "[\n\t{\n\t\t\"foo\": \"bar\",\n\t\t\"fizz\": \"buzz\",\n\t\t\"foo\": \"baz\"\n\t},\n\t{\n\t\t\"spam\": \"eggs\",\n\t\t\"foo\": \"second\",\n\t\t\"nested\": {\n\t\t\t\"foo\": \"nested\",\n\t\t\t\"key\": \"value\",\n\t\t\t\"inner\": {\n\t\t\t\t\"some_array\": [\n\t\t\t\t\t1,\n\t\t\t\t\tnull,\n\t\t\t\t\ttrue,\n\t\t\t\t\tfalse,\n\t\t\t\t\t1234\n\t\t\t\t]\n\t\t\t}\n\t\t}\n\t}\n]"

    another_json_data = json.loads(another_json_string)
    pprint(another_json_data)
    d = {
        "foo": "bar",
        "foo": "baz",
    }
    print(d)

    dumped_json = json.dumps(
        another_json_data * 10,
        indent=2,
    )
    print(dumped_json)


if __name__ == "__main__":
    main()
