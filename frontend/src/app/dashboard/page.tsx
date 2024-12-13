'use client';

import { withAuth } from "../../utils/withAuth";
import { useAuth } from "../../context/AuthContext";

const Dashboard = () => {
  const { logout } = useAuth();

  return (
    <div>
      <h1 className="text-2xl font-bold">Welcome to your Dashboard</h1>
      <button
        onClick={logout}
        className="mt-4 bg-red-500 text-white px-4 py-2 rounded"
      >
        Logout
      </button>
    </div>
  );
};

export default withAuth(Dashboard);
