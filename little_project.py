# Property of Delos Inc. :)


class Park:
    """A Delos Theme Park model"""
    def __init__(self, park_name):
        self.park_name = park_name
        # below a container of hosts instances in a particular Delos park
        self.active_hosts = {}
    # delos_hosts is a container of all delos's hosts from all parks and from the storage
    delos_hosts = {}

    @classmethod
    def delos_hosts_stats(cls):
        """returns statistics of all instantiated delos' hosts in all parks and the storage"""
        print(f"\nDelos' property\nAll Hosts number: '{len(cls.delos_hosts)}'")
        for name, identity in cls.delos_hosts.items():
            print(f"\t{name} ::::: control unit #{identity}")
        return "Listing complete"

    def active_hosts_number(self):
        """hosts number in a particular Delos park"""
        return f"{self.park_name}: '{len(self.active_hosts)}' hosts"

    def active_hosts_stats(self):
        print(f"\n'{self.park_name.upper()}' theme park\nActive Hosts number: '{len(self.active_hosts)}'")
        for name, identity in self.active_hosts.items():
            print(f"\t{name} ::::: control unit #{id(identity)}")
        return "Listing complete"

    def get_description(self):
        try:
            with open(f"Parks Descriptions/{self.park_name.lower()}.txt") as file:
                text = file.read()
        except FileNotFoundError:
            return f"\n'{self.park_name}' description file not found"
        if len(text) > 1:
            return f"\n'{self.park_name.upper()}'\n{text}"
        else:
            return f"\n'{self.park_name.upper()}'\nDescription missing"

    def __str__(self):
        return self.park_name


class Host:
    """The Host model"""
    def __init__(self, park, name, gender, race, height, legend="MISSING", back_story="MISSING"):
        self.name = name
        self.status = "active"
        self.park = park
        self.gender = gender
        self.race = race
        self.height = height
        self.legend = legend
        self.back_story = back_story

        # as the instance of a host is created
        # we add it to the list of hosts in a particular park
        self.park.active_hosts.update({self.name: self})
        # and to the general statistic of Delos' hosts
        Park.delos_hosts.update({self.name: id(self)})

    def add_back_story(self, file):
        """host's back story upload. Receives a link to the file containing the back story"""
        with open(file) as back_story:
            self.back_story = back_story.read()
        print(f"\n### {self.name}. Back story successfully uploaded ###")

    def __str__(self):
        profile = []
        for k, v in self.__dict__.items():
            profile.append(f"\n{k.upper()}: {str(v)}")
        return "".join(profile)


class Storage:
    """A storage for decommissioned hosts"""
    def __init__(self, park_name):
        self.park_name = park_name
        # below a container of hosts instances in a particular Delos park
        self.decommissioned_hosts = {}

    def decommissioned_hosts_number(self):
        """hosts number in a particular Delos park"""
        return f"{self.park_name}: '{len(self.decommissioned_hosts)}' hosts"

    def decommissioned_hosts_stats(self):
        print(f"\n'{self.park_name.upper()}'. \nHosts number: '{len(self.decommissioned_hosts)}'")
        for name, identity in self.decommissioned_hosts.items():
            print(f"\t{name} ::::: control unit #{id(identity)}")
        return "Listing complete"

    def __str__(self):
        return self.park_name


def decommission_host(host):
    """deletes a host record from the park by the host's name
    and places it into the warehouse"""
    del(host.park.active_hosts[host.name])
    host.park = storage
    host.status = 'decommissioned'
    storage.decommissioned_hosts.update({host.name: host})
    print(f"\n{host.name} ::::: DECOMMISSIONED")


def reactivate_host(host, park):
    """reactivates a host from a storage in the park selected"""
    del(storage.decommissioned_hosts[host.name])
    host.park = park
    host.status = 'active'
    park.active_hosts.update({host.name: host})
    print(f"\n{host.name} ::::: RE-ACTIVATED in {park.park_name}")


def terminate_host(host):
    """deletes a host from:
       1. the park/storage of his location records;
       2. the general delos_hosts records;
       3. finally deletes the host instance object entirely from the global namespace
       where it was created
    """
    # erasing a host from his park records
    del(host.park.active_hosts[host.name])
    # erasing a host from delos_hosts records
    del(Park.delos_hosts[host.name])
    # localising the host object in global namespace and terminating it by its key
    global_names_assigned_with_host = [key for key, value in globals().items() if value == host]
    for obj in global_names_assigned_with_host:
        del(globals()[obj])
    print(f"\n{host.name} ::::: TERMINATED")


# place for decommissioned hosts, initialisation
storage = Storage("Storage")

# Delos theme parks initialisation
park_1 = Park("Westworld")
park_2 = Park("Shogunworld")
park_3 = Park("Raj")
park_4 = Park("Medieval world")
park_5 = Park("WarWorld")

# creating hosts for the initialised parks
Dolores = Host(park_1, "Dolores Abernathy", "female", "Caucasian American", 174, "Rancher's Daughter")
Bernard = Host(park_1, "Bernard Lowe", "male", "African American", 180, "Head of Programming Division")
Teddy = Host(park_1, "Theodor Flood", "male", "Caucasian American", 176, "Gunslinger")
Maeve = Host(park_1, "Maeve Millay", "female", "Black British", 173, "Brothel Madam in the local Mariposa Saloon")
Musashi = Host(park_2, "Musashi Sanada", "male", "Japanese", 176, "Shogun")


if __name__ == '__main__':
    print(Bernard)
    Bernard.add_back_story("Stories/Bernard Lowe.txt")
    print(Dolores)
    print(Bernard)
    print(park_1.active_hosts_stats())
    decommission_host(Dolores)
    print(storage.decommissioned_hosts_stats())
    print(park_1.active_hosts_stats())
    print(Dolores)
    reactivate_host(Dolores, park_3)
    print(storage.decommissioned_hosts_stats())
    print(park_1.active_hosts_stats())
    print(park_3.active_hosts_stats())
    print(Dolores)
    print(Park.delos_hosts_stats())

    print(park_2.get_description())
