import math

# object description ...
class CelestialObject:
    def __init__(self, name, mean_orbit, mass, position, velocity, diameter, color=(255,255,255), shape=2):
        self.name = name
        self.mean_orbit = mean_orbit # AU
        self.mass = mass # kg
        self.position = position # AU
        self.velocity = velocity # km/s
        self.diameter = diameter # km
        self.color = color
        self.trayectory = [] # list of tuples # AU
        self.shape = shape # shape for render in window, this shoudnt be implemented here
    
    def __str__(self) -> str:
        return f"{self.name}"

# object description ...
class SYSTM:
    G = 6.67430e-11  # Constante gravitatoria (m^3/kg/s^2)
    AU = 149600000 # km
    def __init__(self, name='SYSTM', diameter=5):
        self.name = name
        self.diameter = diameter
        self.objects = []
    
    def __str__(self) -> str:
        return f"{self.name}"
        
    def simulate_movement(self, time=20000):
        for object in self.objects:
            for other_object in self.objects:
                if other_object == object:
                    pass
                else:
                    # Calculate the new distance
                    dx = (object.position[0] - other_object.position[0])
                    dy = (object.position[1] - other_object.position[1])
                    distance = math.sqrt(dx**2 + dy**2) * self.AU
                    # Calculate the new gravitational force
                    gravitational_force = (self.G * object.mass * other_object.mass) / (distance**2)
                    # Calculate the new acceleration in km/s^2
                    new_acceleration = [
                        gravitational_force / object.mass * (other_object.position[0] - object.position[0]) / distance,
                        gravitational_force / object.mass * (other_object.position[1] - object.position[1]) / distance
                    ]
                    # Update the velocity
                    object.velocity[0] += new_acceleration[0] * time
                    object.velocity[1] += new_acceleration[1] * time
                    # Update the position
                    object.position[0] += object.velocity[0] * time / self.AU
                    object.position[1] += object.velocity[1] * time / self.AU
                    # Update trayectory
                    object.trayectory.append((object.position[0], object.position[1]))

class SLR_SYSTM(SYSTM):
    def __init__(self, name='SLR_SYSTM', diameter=70):
        super().__init__(name, diameter)
        self.objects.append(CelestialObject(name='Sun', mean_orbit=0, mass=1.989e30, position=[0, 0], velocity=[0, 0], diameter=0, shape=2))
        self.objects.append(CelestialObject(name='Mercury', mean_orbit=0.39, mass=3.3011e23, position=[0.39, 0], velocity=[0, 48], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Venus', mean_orbit=0.72, mass=4.8675e24, position=[0.72, 0], velocity=[0, 35.4], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1, 0], velocity=[0, 29], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Mars', mean_orbit=1.52, mass=6.4171e23, position=[1.52, 0], velocity=[0, 24.3], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Jupiter', mean_orbit=5.20, mass=1.898e27, position=[5.20, 0], velocity=[0, 13.2], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Saturn', mean_orbit=9.58, mass=5.683e26, position=[9.58, 0], velocity=[0, 9.7], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Uranus', mean_orbit=19.22, mass=8.681e25, position=[19.22, 0], velocity=[0, 6.8], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Neptune', mean_orbit=30.05, mass=1.024e26, position=[30.05, 0], velocity=[0, 5.5], diameter=0, shape=1))

class RTH_SYSTM(SYSTM):
    def __init__(self, name='RTH_SYSTM', diameter=1):
        super().__init__(name, diameter)
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[0,0], velocity=[0,0], diameter=0))

class TIERRA_PRUEBA_01_SYSTM(SYSTM):
    def __init__(self, name='TIERRA_PRUEBA_01_SYSTM', diameter=5):
        super().__init__(name, diameter)
        self.objects.append(CelestialObject(name='Sun', mean_orbit=0, mass=1.989e30, position=[0,0], velocity=[0,0], diameter=0))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,55], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,50], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,45], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,40], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,35], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,30], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,25], diameter=0, shape=1))
        self.objects.append(CelestialObject(name='Earth', mean_orbit=1, mass=5.972e24, position=[1,0], velocity=[0,20], diameter=0, shape=1))

class SOL_PRUEBA_01_SYSTM(SYSTM):
    def __init__(self, name='SOL_PRUEBA_01_SYSTM', diameter=5):
        super().__init__(name, diameter)
        self.objects.append(CelestialObject(name='Sun', mean_orbit=0, mass=1.989e30, position=[-1,0], velocity=[0,-30], diameter=0))
        self.objects.append(CelestialObject(name='Sun', mean_orbit=0, mass=1.989e30, position=[1,0], velocity=[0,30], diameter=0))





























import PyQt5
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QWidget
class WDW(QWidget):
    def __init__(WDW) -> None:
        super().__init__()
        # Instanciate all simulations
        WDW.simulations = []
        WDW.simulations.append(SLR_SYSTM())
        WDW.simulations.append(RTH_SYSTM())
        WDW.simulations.append(TIERRA_PRUEBA_01_SYSTM())
        WDW.simulations.append(SOL_PRUEBA_01_SYSTM())
        SOL_PRUEBA_01_SYSTM
        WDW.active_simulation = WDW.simulations[0]
        WDW.scale = WDW.calculate_scale(WDW.active_simulation.diameter)
        WDW.animation_started = False
        # Instanciate and configurate timer
        WDW.Timer = PyQt5.QtCore.QTimer(WDW)
        WDW.Timer.timeout.connect(WDW.animate)
        WDW.init_ui()
        
    def init_ui(WDW):
        # Configurates window 
        WDW.draggable = False
        WDW.offset = None
        WDW._size = (1000, 1000)
        WDW.setFixedSize(*WDW._size)
        WDW.center_window()
        WDW.setWindowFlags(Qt.FramelessWindowHint)
        WDW.setContextMenuPolicy(Qt.CustomContextMenu)
        WDW.setStyleSheet("background-color: black;")
        # Create a QLabel to display the simulation name
        WDW.simulation_name = PyQt5.QtWidgets.QLabel(f"{WDW.active_simulation.name}", WDW)
        WDW.simulation_name.setGeometry(0, 970, 250, 30)  # (x, y, b, h)
        WDW.simulation_name.setStyleSheet("color: white;  padding: 10px;")
        
    def __str__(self) -> str:
        return f"WDW, size: {self._size}"

    def save_simulation(WDW):
        import os
        import csv
        # Create a directory to store simulation data if it doesn't exist
        simulation_dir = os.path.join(os.getcwd(), 'simulation_data')
        if not os.path.exists(simulation_dir):
            os.makedirs(simulation_dir)

        # Create a unique directory for the active simulation
        active_simulation_dir = os.path.join(simulation_dir, WDW.active_simulation.name)
        if not os.path.exists(active_simulation_dir):
            os.makedirs(active_simulation_dir)

        # Create CSV files for positions and trajectories
        positions_file = os.path.join(active_simulation_dir, 'positions.csv')
        trajectories_file = os.path.join(active_simulation_dir, 'trajectories.csv')

        # Prepare data to be saved
        positions_data = [['Name', 'X Position (AU)', 'Y Position (AU)', 'X Velocity (km/s)', 'Y Velocity (km/s)']]
        trajectories_data = [['Name', 'X Position (AU)', 'Y Position (AU)']]

        for obj in WDW.active_simulation.objects:
            positions_data.append([obj.name, obj.position[0], obj.position[1], obj.velocity[0], obj.velocity[1]])
            trajectories_data.append([obj.name] + [point for point in obj.trayectory])

        # Save data to CSV files
        with open(positions_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(positions_data)

        with open(trajectories_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(trajectories_data)

        print(f'Simulation data for {WDW.active_simulation.name} saved in CSV format in {active_simulation_dir}')

    def render_objects_position(WDW):
        # Instanciate and configurate painter object
        from PyQt5.QtGui import QPainter
        object_painter = QPainter(WDW)
        object_painter.setRenderHint(QPainter.Antialiasing)
        object_painter.setBrush(Qt.NoBrush)
        # Render objects position
        for object in WDW.active_simulation.objects:
            # Instanciate and configurate pen object
            pen = PyQt5.QtGui.QPen(PyQt5.QtGui.QColor(*object.color))
            pen.setWidth(1) 
            object_painter.setPen(pen)
            object_position = WDW.get_window_position(object.position)
            object_painter.drawEllipse(object_position[0]-object.shape, object_position[1]-object.shape, object.shape * 2, object.shape * 2)

    def render_objects_trayectory(WDW):
        # Instanciate and configurate painter object
        from PyQt5.QtGui import QPainter
        object_painter = QPainter(WDW)
        object_painter.setRenderHint(QPainter.Antialiasing)
        # Render objects trayectory
        for object in WDW.active_simulation.objects:
            trayectory = object.trayectory
            if len(trayectory) > 1:
                path = PyQt5.QtGui.QPainterPath()
                path.moveTo(*WDW.get_window_position(trayectory[0]))
                for position in trayectory[0:]:
                    path.lineTo(*WDW.get_window_position(position))
                pen = PyQt5.QtGui.QPen(PyQt5.QtGui.QColor(75,75,75))
                pen.setWidth(1)
                object_painter.setPen(pen)
                object_painter.drawPath(path)
        
    def paintEvent(WDW, event):
        WDW.simulation_name.setText(f"{WDW.active_simulation.name}")
        WDW.render_objects_trayectory()
        WDW.render_objects_position()

    def next_simulation(WDW):
        active_simulation_index = WDW.simulations.index(WDW.active_simulation)
        next_simulation_index = (active_simulation_index + 1) % len(WDW.simulations)
        WDW.active_simulation = WDW.simulations[next_simulation_index]
        # Actualiza la vista para mostrar la nueva simulación activa
        WDW.scale = WDW.calculate_scale(WDW.active_simulation.diameter)
        WDW.update()

    def previous_simulation(WDW):
        active_simulation_index = WDW.simulations.index(WDW.active_simulation)
        previous_simulation_index = (active_simulation_index - 1) % len(WDW.simulations)
        WDW.active_simulation = WDW.simulations[previous_simulation_index]
        # Actualiza la vista para mostrar la nueva simulación activa
        WDW.scale = WDW.calculate_scale(WDW.active_simulation.diameter)
        WDW.update()

    def calculate_scale(self, simulation_diameter):
            scale = 1000 / simulation_diameter
            return scale

    # REVISAR
    def animate(WDW):
        if WDW.animation_started:
            WDW.active_simulation.simulate_movement()
            WDW.update()
    
    # 
    def export_image(WDW):
        from PyQt5.QtGui import QPixmap, QPainter
        # Create a QPixmap with the same size as the widget
        pixmap = QPixmap(WDW.size())
        # Create a QPainter to render the widget onto the pixmap
        painter = QPainter(pixmap)
        WDW.render(painter)
        # Save the pixmap as an image file (e.g., PNG format)
        file_path = "002.png"
        pixmap.save(file_path)
        # Clean up the QPainter and pixmap
        painter.end()
        # Print a message to confirm the save
        print(f"Saved the image as {file_path}")

    # 
    def start_simulation(WDW):
        # Iniciar o detener la animación al presionar la barra espaciadora
        WDW.animation_started = not WDW.animation_started
        if WDW.animation_started:
            WDW.Timer.start(500)  # Iniciar el temporizador
        else:
            WDW.Timer.stop()  # Detener el temporizador

    # This functions takes the position of the objects and returns the position in the window considering scale and
    def get_window_position(self, object_position):
        x = object_position[0] * self.scale + 500
        y = object_position[1] * self.scale + 500
        return (int(round(x)), int(round(y)))

    def center_window(self):
        from PyQt5.QtWidgets import QDesktopWidget
        frame_geometry = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def minimize_window(self):
        self.showMinimized()

    def keyPressEvent(self, event):
        key = event.key()
        key_actions = {
            Qt.Key_Space: self.start_simulation,
            Qt.Key_Left: self.previous_simulation,
            Qt.Key_Right: self.next_simulation,
            #Qt.Key_Up: self.flecha_arriba,  
            #Qt.Key_Down: self.flecha_abajo,  
            Qt.Key_Return: self.save_simulation,  
            #Qt.Key_Escape: self.escape
        }
        action = key_actions.get(key)
        if action:
            action()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = True
            self.offset = event.pos()
        elif event.button() == Qt.MiddleButton:
            if self.isMinimized():
                self.showNormal()
            else:
                self.minimize_window()
    
    def mouseMoveEvent(self, event):
        if self.draggable and event.buttons() & Qt.LeftButton:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False
            self.offset = None