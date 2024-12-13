// src/services/branches.ts
import axios from "./api";

export const fetchBranches = async () => {
  const response = await axios.get("/branches/");
  return response.data;
};
