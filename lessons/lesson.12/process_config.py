import configparser


def demo_configparser():
    config = configparser.ConfigParser()
    config.read("demo-config.ini")
    print(config)
    print(config.sections())
    print(config["DEFAULT"])
    print("environ:", config["DEFAULT"]["environ"])

    for item in config["DEFAULT"].items():
        print(item)

    print("PG sk:", config["postgresql"]["secret_key"])

    mysql_port = config["mysql"].get("port", "6543")
    print("mysql_port", mysql_port)
    postgresql_port = config["postgresql"].getint("port", 5432)
    print("postgresql_port", postgresql_port)

    config["mysql"]["port"] = mysql_port
    config["postgresql"]["port"] = str(postgresql_port)

    with open("demo-config.ini", "w") as f:
        config.write(f)


def main():
    demo_configparser()


if __name__ == '__main__':
    main()
