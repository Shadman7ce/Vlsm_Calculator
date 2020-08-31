from math import pow


def get_number_of_hosts(cidr):
    return pow(2, (32 - cidr)) - 2


def get_ip(ip):
    return [int(x) for x in ip.split('.')]


def get_broadcast(wildcard, network_address):
    broadcast = [0, 0, 0, 0]
    for i in range(0, 4):
        broadcast[i] = wildcard[i] | network_address[i]

    return broadcast


def get_mask(cidr):
    mask = [0, 0, 0, 0]

    if cidr < 8:
        mask[0] = 256 - int(pow(2, (8 - cidr)))

    elif cidr < 16:
        mask[0] = 255
        mask[1] = 256 - int(pow(2, (16 - cidr)))

    elif cidr < 24:
        mask[0] = 255
        mask[1] = 255
        mask[2] = 256 - int(pow(2, (24 - cidr)))
    else:
        mask[0] = 255
        mask[1] = 255
        mask[2] = 255
        mask[3] = 256 - int(pow(2, (32 - cidr)))

    return mask


def get_network_address(ip, mask):
    net_addr = []
    for i in range(4):
        net_addr.append(ip[i] & mask[i])
    return net_addr


def get_wild_card(mask):
    wild_card_address = [0, 0, 0, 0]
    for i in range(4):
        wild_card_address[i] = 255 - mask[i]
    return wild_card_address


def get_slash(number_of_hosts):
    for i in range(2, 33):
        if (number_of_hosts <= pow(2, i) - 2):
            return 32 - i


network_address = str(input(
    "Enter IP Address and CIDR in this format (192.168.1.0/16): "))

required_hosts = int(input("Required Hosts: "))

cidr = int(network_address.split('/')[1])
ip = get_ip(network_address.split('/')[0])

available_hosts = get_number_of_hosts(cidr)
prev_mask = get_mask(cidr)
prev_network_address = get_network_address(ip, prev_mask)
prev_wildcard = get_wild_card(prev_mask)

# inside the loop

slash = get_slash(required_hosts)  # j
mask = get_mask(slash)  # u
network_address = get_network_address(prev_network_address, mask)  # e
wild_card = get_wild_card(mask)  # l
broadcast = get_broadcast(wild_card, network_address)  # b

available_hosts = int(get_number_of_hosts(slash))

start_address = [network_address[0], network_address[1],
                 network_address[2], network_address[3]+1]
end_address = [broadcast[0], broadcast[1],
               broadcast[2], broadcast[3]-1]

print()
print("Required Hosts: ", required_hosts)
print("Available Hosts: ", available_hosts)
print("Unused Hosts: ", available_hosts-required_hosts)
print("Address Range: ", start_address, end_address)
print("Slash: /", slash)
print("Broadcast Address: ", broadcast)
print("Wildcard Address: ", wild_card)
