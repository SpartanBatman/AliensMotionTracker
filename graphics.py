from PIL import Image, ImageDraw
import math

ScrWidth = 290
ScrHeight = 320

class ContactsArray:
    def __init__(self, contacts):
        self.contacts = contacts

    def getClosestContactDistance(self):
        if not self.contacts:
            return float('inf')
        return min(math.hypot(x - 160, y - 120) for x, y, age in self.contacts)

class TrackerGraphics:
    def __init__(self, scope, resources, calibration):
        self.scope = scope
        self.resources = resources
        self.contacts = []
        self.device = scope.device  # Get the luma.lcd device

    def getClosestContactDistance(self):
        if not self.contacts:
            return float('inf')
        return min(math.hypot(x - 160, y - 120) for x, y, age in self.contacts)

    def update(self, wave_size, addcontact, calibration):
        # Start with black canvas matching device dimensions
        base = Image.new("RGBA", (320, 240), "black")
        
        # Create a centered box for the HUDs
        box = Image.new("RGBA", (ScrWidth, 240), (0, 0, 0, 0))  # Transparent box
        box_w, box_h = box.size
        offset = ((320 - box_w) // 2, 0)  # Center horizontally
        base.paste(box, offset, box)  # Paste transparent box to create centering area

        # Draw HUD elements
        if hasattr(self.resources, "hud"):
            hud = self.resources.hud.convert("RGBA")
            hud = hud.resize((ScrWidth, ScrHeight), Image.Resampling.LANCZOS)  # Resize to full height
            hud_w, hud_h = hud.size
            base_w, base_h = base.size
            
            # Rotate HUD based on compass reading
            #hud = hud.rotate(-calibration.getHeading())  # Negative to rotate clockwise
            
            # Position behind bottom HUD with additional offset
            offset = ((base_w - hud_w) // 2, base_h - hud_h + 100)  # Move down 20 pixels from bottom
            base.paste(hud, offset, hud.split()[3])  # Use alpha channel as mask

        if hasattr(self.resources, "info"):
            hud_bottom = self.resources.info.convert("RGBA")
            hud_bottom = hud_bottom.resize((ScrWidth, 50), Image.Resampling.LANCZOS)  # Resize to 50px height
            hud_bottom_w, hud_bottom_h = hud_bottom.size
            base_w, base_h = base.size
            offset = ((base_w - hud_bottom_w) // 2, base_h - hud_bottom_h)  # Position at bottom
            base.paste(hud_bottom, offset, hud_bottom.split()[3])  # Use alpha channel as mask

        draw = ImageDraw.Draw(base)

        # Add new contact if requested
        if addcontact:
            self.contacts.append((calibration.cx, calibration.cy, 1))

        # Update existing contacts
        updated_contacts = []
        for contact in self.contacts:
            x, y, age = contact
            if age < 30:
                updated_contacts.append((x, y, age + 1))
        self.contacts = updated_contacts

        # Draw contacts
        for contact in self.contacts:
            x, y, age = contact
            size = max(1, 6 - age // 5)
            draw.ellipse((x - size, y - size, x + size, y + size), outline="green")

        # Draw pulse wave on top of HUD
        if hasattr(self.resources, "waves") and wave_size < len(self.resources.waves):
            pulse = self.resources.waves[wave_size].convert("RGBA")
            pulse = pulse.resize((ScrWidth, 240), Image.Resampling.LANCZOS)
            
            # Center the pulse wave
            pulse_w, pulse_h = pulse.size
            base_w, base_h = base.size
            offset = ((base_w - pulse_w) // 2, (base_h - pulse_h) // 2)
            base.paste(pulse, offset, pulse.split()[3])  # Use alpha channel as mask

        # Convert to RGB and display
        self.device.display(base.convert("RGB"))

        return ContactsArray(self.contacts)
