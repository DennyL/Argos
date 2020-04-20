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


class Host(Park):
    """The Host model"""
    def __init__(self, park_id, name, gender, race, height, legend="MISSING", back_story="MISSING"):
        self.park_id = park_id
        self.status = "active"
        self.name = name
        self.gender = gender
        self.race = race
        self.height = height
        self.legend = legend
        self.back_story = back_story

        # as the instance of a host is created
        # we add it to the list of hosts in a particular park
        self.park_id.active_hosts.update({self.name: self})
        # and to the general statistic of Delos' hosts
        Park.delos_hosts.update({self.name: id(self)})

    def __str__(self):
        """returns the host's profile"""
        return f'''
Host name: {self.name.upper()}
Current location: {self.park_id.park_name.upper()}
Status: {self.status.upper()}
Gender: {self.gender.upper()}
Race: {self.race.upper()}
Height: {self.height} cm
Legend: {self.legend}
Back Story: {self.back_story}
'''

    def add_back_story(self, file):
        """host's back story upload. Receives a link to the file containing the back story"""
        with open(file) as back_story:
            self.back_story = back_story.read()
        print(f"### {self.name}. Back story successfully uploaded ###")


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


def decommission_host(host):
    """deletes a host record from the park by the host's name
    and places it into the warehouse"""
    del(host.park_id.active_hosts[host.name])
    host.park_id = storage
    host.status = 'decommissioned'
    storage.decommissioned_hosts.update({host.name: host})
    print(f"\n{host.name} ::::: DECOMMISSIONED")


def reactivate_host(host, park):
    """reactivates a host from a storage in the park selected"""
    del(storage.decommissioned_hosts[host.name])
    host.park_id = park
    host.status = 'active'
    park.active_hosts.update({host.name: host})
    print(f"\n{host.name} ::::: RE-ACTIVATED in {park.park_name}")


# place for decommissioned hosts, initialisation
storage = Storage("Storage")

# Delos theme parks initialisation
park_1 = Park("WestWorld")
park_2 = Park("SamuraiWorld")
park_3 = Park("Raj")
park_4 = Park("MedievalWorld")
park_5 = Park("WarWorld")

# creating hosts for the initialised parks
Dolores = Host(park_1, "Dolores Abernathy", "female", "Caucasian American", 174, "Rancher's Daughter")
Bernard = Host(park_1, "Bernard Lowe", "male", "African American", 180, "Head of Programming Division")
Teddy = Host(park_1, "Theodor Flood", "male", "Caucasian American", 176, "Gunslinger")
Maeve = Host(park_1, "Maeve Millay", "female", "Black British", 173, "Brothel Madam in the local Mariposa Saloon")
Musashi = Host(park_2, "Musashi Sanada", "male", "Japanese", 176, "Shogun")


if __name__ == '__main__':
    # print(Bernard)
    # Bernard.add_back_story("Stories/Bernard Lowe.txt")
    print(Dolores)
    # print(Bernard)
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

