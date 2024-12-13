// src/components/Table.tsx
interface TableProps {
  data: { [key: string]: any }[];
}

export default function Table({ data }: TableProps) {
  if (!data || data.length === 0) {
    return <p>No data available.</p>;
  }

  const headers = Object.keys(data[0]);

  return (
    <table className="min-w-full border-collapse border border-gray-200">
      <thead className="bg-gray-100">
        <tr>
          {headers.map((header) => (
            <th key={header} className="border px-4 py-2 text-left">
              {header}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.map((row, index) => (
          <tr key={index} className="odd:bg-white even:bg-gray-50">
            {headers.map((header) => (
              <td key={header} className="border px-4 py-2">
                {row[header]}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}
