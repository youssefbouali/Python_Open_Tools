import ipaddress
// Vlsm Calculator
def calculate_vlsm(network_address_str, subnet_sizes):
    try:
        network_address = ipaddress.IPv4Network(network_address_str, strict=False)
    except ValueError:
        print("Invalid network address format.")
        return []

    subnet_sizes.sort(reverse=True)
    vlsm_result = []

    for size in subnet_sizes:
        prefix_length = 32 - (size.bit_length() - 1)

        if network_address.num_addresses >= 2 ** (32 - prefix_length):
            vlsm_result.append((network_address.network_address, prefix_length, size))
            network_address = ipaddress.IPv4Network(
                (
                    int(network_address.network_address) + 2 ** (32 - prefix_length),
                    prefix_length,
                ),
                strict=False,
            )
        else:
            print(f"Not enough address space for subnet size {size}!")

    return vlsm_result

# Take user inputs for network address and subnet sizes
network_address_str = input("Enter the network address (e.g., 192.168.0.0/24): ")
subnet_sizes_str = input("Enter subnet sizes separated by commas (e.g., 30,20,15,10): ")

# Convert the subnet sizes input to a list of integers
subnet_sizes = [int(size.strip()) for size in subnet_sizes_str.split(',')]

# Calculate VLSM
vlsm_result = calculate_vlsm(network_address_str, subnet_sizes)

# Display the VLSM result
print("\nVLSM Result:")
for subnet in vlsm_result:
    print(f"Subnet: {subnet[0]}/{subnet[1]}, Size: {subnet[2]}")
