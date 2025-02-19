from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    INITIAL_MAX_MILEAGE = 180.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        BaseVehicle.__init__(self, brand, model, license_plate_number, self.INITIAL_MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage = round(mileage / self.max_mileage * 100) + 5
        self.battery_level -= percentage