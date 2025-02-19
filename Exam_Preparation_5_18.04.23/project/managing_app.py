from typing import List
from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE = {
        "PassengerCar": PassengerCar,
        "CargoVan": CargoVan
                     }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def __define_next_route_id(self):
        return len(self.routes) + 1

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        try:
            next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
            return f"{driving_license_number} has already been registered to our platform."
        except StopIteration:
            user = User(first_name, last_name, driving_license_number)
            self.users.append(user)

            return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        try:
            vehicle = self.VALID_VEHICLE[vehicle_type](brand, model, license_plate_number)

        except KeyError:
            return f"Vehicle type {vehicle_type} is inaccessible."

        try:
            next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
            return f"{license_plate_number} belongs to another vehicle."

        except StopIteration:
            self.vehicles.append(vehicle)
            return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        try:
            greater_length_route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length > length][0]
            greater_length_route.is_locked = True
        except IndexError:
            pass

        try:
            route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length == length][0]
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        except IndexError:

            try:
                route = [r for r in self.routes if r.start_point == start_point and r.end_point == end_point and r.length < length][0]
                return f"{start_point}/{end_point} shorter route had already been added to our platform."

            except IndexError:
                r_id = self.__define_next_route_id()
                r = Route(start_point, end_point, length, r_id)
                self.routes.append(r)

                return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(filter(lambda u: u.driving_license_number == driving_license_number, self.users))
        vehicle = next(filter(lambda v: v.license_plate_number == license_plate_number, self.vehicles))
        route = next(filter(lambda r: r.route_id == route_id, self.routes))

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [v for v in self.vehicles if v.is_damaged]
        damaged_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))

        if len(damaged_vehicles) > count:
            damaged_vehicles = damaged_vehicles[:count]

        for v in damaged_vehicles:
            v.is_damaged = False
            v.recharge()

        return f"{len(damaged_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda u: -u.rating)
        result = ["*** E-Drive-Rent ***"]

        for u in sorted_users:
            result.append(str(u))

        return "\n".join(result)