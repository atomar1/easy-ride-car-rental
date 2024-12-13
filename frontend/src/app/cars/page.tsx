// src/app/cars/page.tsx
"use client";

import { useEffect, useState } from "react";
import { fetchCars } from "../../services/cars";
import Table from "../../components/Table";

export default function CarsPage() {
  const [cars, setCars] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const getCars = async () => {
      try {
        const data = await fetchCars();
        setCars(data);
      } catch (err) {
        setError("Failed to fetch cars.");
      }
    };
    getCars();
  }, []);

  return (
    <div className="container mx-auto py-6">
      <h1 className="text-2xl font-bold mb-4">Available Cars</h1>
      {error ? (
        <p className="text-red-500">{error}</p>
      ) : (
        <Table data={cars} />
      )}
    </div>
  );
}
