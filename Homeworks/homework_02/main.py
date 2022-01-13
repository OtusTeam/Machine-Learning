
import Vehicle
import Plane

#Vehicle
object_vehile = Vehicle.Vehicle(False)
object_vehile.fuel=100
object_vehile.fuel_consumption=10
object_vehile.move(1)
object_vehile.started=False
object_vehile.start()

#Plane

object_plane = Plane.Plane(100)
object_plane.load_cargo(10)
