import Image from "next/image";
import Link from "next/link";

export default function HomePage() {
  return (
    <div className="bg-gray-50">
      {/* Hero Section */}
      <section className="relative h-[80vh] flex items-center justify-center text-center">
        <div className="max-w-4xl">
          <h1 className="text-4xl font-bold text-gray-900">
            Welcome to EasyRide Car Rentals
          </h1>
          <p className="mt-4 text-lg text-gray-700">
            Affordable, reliable, and luxurious car rentals at your fingertips.
          </p>
          <div className="mt-6">
            <Link 
              href="/bookings" 
              className="bg-black text-white px-6 py-3 rounded-lg shadow hover:bg-gray-800 mr-4"
            >
              Book a Car
            </Link>
            <Link 
              href="/branches" 
              className="bg-white text-black border border-black px-6 py-3 rounded-lg shadow hover:bg-gray-100"
            >
              Find a Branch
            </Link>
          </div>
        </div>
        {/* Background Image */}
        <Image
          src="/hero.jpg" // Place a relevant car rental image in public/ folder
          alt="Luxury car"
          layout="fill"
          objectFit="cover"
          quality={80}
          className="opacity-50"
        />
      </section>

      {/* Featured Section */}
      <section className="py-12">
        <div className="max-w-7xl mx-auto px-4">
          <h2 className="text-3xl font-bold text-center">Why Choose EasyRide?</h2>
          <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center">
              <h3 className="text-xl font-bold">Wide Range of Cars</h3>
              <p className="mt-2 text-gray-600">
                From sedans to SUVs, we have cars for every occasion.
              </p>
            </div>
            <div className="text-center">
              <h3 className="text-xl font-bold">Affordable Prices</h3>
              <p className="mt-2 text-gray-600">
                Competitive daily rates with no hidden fees.
              </p>
            </div>
            <div className="text-center">
              <h3 className="text-xl font-bold">Excellent Support</h3>
              <p className="mt-2 text-gray-600">
                24/7 customer service to assist with your booking.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer CTA */}
      <section className="bg-gray-900 text-white py-12 text-center">
        <h2 className="text-2xl font-bold">Ready to Hit the Road?</h2>
        <p className="mt-4">
          Reserve your car today and start your journey with EasyRide!
        </p>
        <div className="mt-6">
          <Link 
            href="/bookings" 
            className="bg-yellow-400 text-black px-6 py-3 rounded-lg shadow hover:bg-yellow-500"
          >
            Book Now
          </Link>
        </div>
      </section>
    </div>
  );
}
