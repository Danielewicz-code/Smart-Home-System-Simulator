import itertools

class Device:
    count_id = itertools.count(1)

    def __init__(self, name) -> None:
        self.id = next(Device.count_id)
        self.name = name 
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        print(f"\n{self.name} is ON.")
        
    def turn_off(self):
        self.status = "OFF"
        print(f"\n{self.name} is OFF.")

    def see_status(self):
        return self.status
    
class Lights(Device):
    def __init__(self, name, color= "white", brightness= 0) -> None:
        super().__init__(name)
        self.color = color
        self.brightness = brightness

    def set_color(self, color):
        self.color = color
        print(f"{self.name} color has been set to {self.color}.")
    
    def set_brightness(self, brightness):
        self.brightness = brightness
        print(f"{self.name} brightness has been set to {self.brightness}.")

class Thermostat(Device):
    def __init__(self, name, temperature= 0) -> None:
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"{self.name} has been set to {self.temperature} degrees.")

    def get_temperature(self):
        return self.temperature
    
class Door(Device):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.locked = False

    def lock(self):
        self.locked = True
        print(f"{self.name} has been locked.")

    def unlock(self):
        self.locked = False
        print(f"{self.name} has been unlocked.")

    def door_status(self):
        return self.locked

class Room:
    def __init__(self, name) -> None:
        self.room_name = name 
        self.devices_list = []

    def add_devices(self, name):
        device = Device(name)
        self.devices_list.append(device)
        print(f"\nDevice: {name} was added to {self.room_name}")

    def remove_devices(self, key):
        devise_to_remove = None
        for devise in self.devices_list:
            if key == devise.name:
                devise_to_remove = devise
                break
        if devise_to_remove:
            self.devices_list.remove(devise_to_remove)
            print(f"\nDevice: {key} was removed from {self.room_name}.")
        else:
            raise ValueError(f"Key: {key} not found.")

    def get_devices(self):
        for i, device in enumerate(self.devices_list):
            print(f"\nIndex: {i}")
            print(f"Device ID: {device.id}, Name: {device.name}, Status: {device.status}")

    def turn_on(self, name):
        for device in self.devices_list:
            if device.name == name:
                device.turn_on()
                return
        raise ValueError(f"{name} was not found in {self.room_name}.")
            
    def turn_off(self, name):
        for device in self.devices_list:
            if device.name == name:
                device.turn_off()
                return
        raise ValueError(f"{name} was not found in {self.room_name}.")


class User:
    def __init__(self, username, email, password) -> None:
        self.user = username
        self.email = email 
        self.password = password
        self.logged_in = False

    def control_device(self, room, device_name, action):
        if not self.logged_in:
            raise PermissionError("User must be logged in to control devices.")
        elif action.lower() == "on":
            room.turn_on(device_name)
        elif action.lower() == "off":
            room.turn_off(device_name)
        else:
            raise ValueError(f"Unknown Action: {action}.")    

    def login(self, password):
        if self.password == password:
            self.logged_in = True
            print(f"User:{self.user} has logged in.")
        else:
            raise ValueError("Wrong password.")

    def logout(self):
        self.logged_in = False
        print(f"User:{self.user} hass logged out.")


class UserManagement:
    def __init__(self) -> None:
        self.users = {}


    def create_account(self, username, email, password):
        if username in self.users:
            raise ValueError("User already exists.")
        
        self.users[username] = User(username, email, password)
        print(f"Account created for {username}.")

    def authentification(self, username, password):
        if username not in self.users:
            raise ValueError(f"{username} does not exist.")
         
        user = self.users[username]
        user.login(password)
        return user

    #for password reset aproach or accessing user info
    def get_user(self, user_name):
        if user_name not in self.users:
            raise ValueError(f"{user_name} does not exist")
        return self.users[user_name]









