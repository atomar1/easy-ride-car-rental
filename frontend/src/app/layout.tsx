import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import "../styles/globals.css"; // Ensure global styles are applied

export const metadata = {
  title: "EasyRide - Car Rentals",
  description: "Rent your dream car with EasyRide",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="bg-gray-100 text-gray-900">
        <Navbar />
        <main className="min-h-screen">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
