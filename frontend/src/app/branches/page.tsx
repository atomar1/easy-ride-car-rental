// src/app/branches/page.tsx
"use client";

import { useEffect, useState } from "react";
import { fetchBranches } from "../../services/branches";
import Table from "../../components/Table";

export default function BranchesPage() {
  const [branches, setBranches] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const getBranches = async () => {
      try {
        const data = await fetchBranches();
        setBranches(data);
      } catch (err) {
        setError("Failed to fetch branches.");
      }
    };
    getBranches();
  }, []);

  return (
    <div className="container mx-auto py-6">
      <h1 className="text-2xl font-bold mb-4">Our Branches</h1>
      {error ? (
        <p className="text-red-500">{error}</p>
      ) : (
        <Table data={branches} />
      )}
    </div>
  );
}
