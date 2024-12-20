from scapy.all import ARP, Ether, srp

def scan(ip):
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc, 'vendor': get_vendor(received.hwsrc)})

    return clients

def get_vendor(mac):
    # Placeholder function to get vendor information from MAC address
    # You can use an API or a local database to get the actual vendor information
    return "Unknown Vendor"

def save_to_file(clients, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ip', 'mac', 'vendor']) 
        writer.writeheader() 
        for client in clients:
            writer.writerow(client)

if __name__ == "__main__":
    ip_range = "192.168.1.1/24"
    clients = scan(ip_range)
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC" + " "*18+"Vendor")
    for client in clients:
        print("{:16}    {:18}    {}".format(client['ip'], client['mac'], client['vendor']))

