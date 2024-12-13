// src/services/cars.ts
import axios from "./api";

export const fetchCars = async () => {
  const response = await axios.get("/cars/");
  return response.data;
};
