export default function Footer() {
    return (
      <footer className="bg-black text-white py-4">
        <div className="max-w-7xl mx-auto text-center">
          <p className="text-sm">
            © {new Date().getFullYear()} EasyRide. All rights reserved.
          </p>
        </div>
      </footer>
    );
  }
  