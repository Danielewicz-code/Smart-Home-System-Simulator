# Initialize the UserManager and create a user
user_manager = UserManagement()
user_manager.create_account("Vocablo_Guma","Vocablo_Guma@gmail.com", "mistitaesmia")

# Authenticate and login the user
user = user_manager.authentification("Vocablo_Guma", "mistitaesmia")

# Create a room and add devices
living_room = Room("Living Room")
living_room.add_devices(name="camera")
living_room.add_devices(name="main door")
living_room.add_devices(name="smart mirror")

# List devices in the room
print("\nDevices in the Living Room:")
living_room.get_devices()

# User controls devices
print("\nUser controlling devices:")
user.control_device(living_room, "main door", "on")
user.control_device(living_room, "mirror", "on")

# List devices to verify changes
print("\nDevices in the Living Room after actions:")
living_room.get_devices()

# User logs out
user.logout()
