from netmiko import ConnectHandler

def send_show_commands(device, commands):
    with ConnectHandler(**device) as conn:
        hostname = device['ip']  
        for command in commands:
            output = conn.send_command(command)
            filename = f"{hostname}_{command.replace(' ', '_')}.txt"
            with open(filename, 'w') as file:
                file.write(output)

def send_config_commands(device, commands):
    with ConnectHandler(**device) as conn:
        output = conn.send_config_set(commands)
        print(output)

def read_commands_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        commands = [line.strip() for line in lines if line.strip() and not line.startswith('!')]
        return commands

def backup_device_config(device_details):
    with ConnectHandler(**device_details) as conn:
        hostname = device_details['ip'] 
        config = conn.send_command("show running-config")
        filename = f"{hostname}_backup_config.txt"
        with open(filename, 'w') as file:
            file.write(config)

def main():
    devices = {
        'router1': {
            'device_type': 'cisco_ios',
            'ip': '192.168.56.101',
            'username': 'cisco',
            'password': 'cisco123!',
            'port': 22,  
        },
        'router2': {
            'device_type': 'cisco_ios',
            'ip': '192.168.56.102',
            'username': 'cisco',
            'password': 'cisco123!',
            'port': 22,  
        },
    }

    show_commands = ["show version", "show ip int brief"]
    config_commands_router1 = ["interface loopback0", "ip address 1.1.1.1 255.255.255.0"]
    config_commands_router2 = ["interface loopback0", "ip address 192.168.1.1 255.255.255.0"]
    
    print(f"config interfaces")
    print(f"---------------------------------------------------")

    for device_name, device_details in devices.items():
        print(f"Connecting to {device_name}")
        if device_name == 'router1':
            send_config_commands(device_details, config_commands_router1)
        elif device_name == 'router2':
            send_config_commands(device_details, config_commands_router2)
        print(f"---------------------------------------------------")

    print(f"Read extrenal conf file and execute")
    for device_name, device_details in devices.items():
        print(f"Connecting to {device_name}")
        print(f"reading external file")
        commands = read_commands_from_file('router_lab_01_template.txt')
        send_config_commands(device_details, commands)
        print(f"---------------------------------------------------")

    print(f"Run show command's and save the output")
    for device_name, device_details in devices.items():
        print(f"Connecting to {device_name}")
        send_show_commands(device_details, show_commands)
        print(f"---------------------------------------------------")

    print(f"Make a backup and save it")
    for device_name, device_details in devices.items():
        print(f"Backing up configuration for {device_name}")
        backup_device_config(device_details)
        print(f"---------------------------------------------------")

if __name__ == "__main__":
    main()
