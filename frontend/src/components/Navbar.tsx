"use client";

import Link from "next/link";
import { useState } from "react";

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <nav className="bg-black text-white sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <div className="flex-shrink-0">
            <Link 
              href="/" 
              className="text-2xl font-bold text-yellow-500"
            >
              EasyRide
            </Link>
          </div>
          <div className="md:hidden">
            <button 
              onClick={toggleMenu}
              className="text-white focus:outline-none"
            >
              {isMenuOpen ? (
                <svg 
                  className="h-6 w-6" 
                  fill="none" 
                  viewBox="0 0 24 24" 
                  stroke="currentColor"
                >
                  <path 
                    strokeLinecap="round" 
                    strokeLinejoin="round" 
                    strokeWidth={2} 
                    d="M6 18L18 6M6 6l12 12" 
                  />
                </svg>
              ) : (
                <svg 
                  className="h-6 w-6" 
                  fill="none" 
                  viewBox="0 0 24 24" 
                  stroke="currentColor"
                >
                  <path 
                    strokeLinecap="round" 
                    strokeLinejoin="round" 
                    strokeWidth={2} 
                    d="M4 6h16M4 12h16M4 18h16" 
                  />
                </svg>
              )}
            </button>
          </div>
          <div className="hidden md:flex md:absolute md:left-1/2 md:transform md:-translate-x-1/2">
            <div className="flex items-center space-x-4">
              <Link 
                href="/branches" 
                className="hover:text-yellow-500"
              >
                Branches
              </Link>
              <Link 
                href="/cars" 
                className="hover:text-yellow-500"
              >
                Cars
              </Link>
              <Link 
                href="/contact" 
                className="hover:text-yellow-500"
              >
                Contact Us
              </Link>
            </div>
          </div>
          <div className="hidden md:block">
          <Link 
                href="/login-signup" 
                className="bg-yellow-500 text-black px-4 py-2 rounded-md font-semibold hover:bg-yellow-600"
              >
                Login/Signup
              </Link>
          </div>
        </div>
        {isMenuOpen && (
          <div className="md:hidden">
            <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-gray-900">
              <Link 
                href="/branches" 
                className="hover:bg-gray-700 block px-3 py-2 rounded-md text-base font-medium"
                onClick={toggleMenu}
              >
                Branches
              </Link>
              <Link 
                href="/cars" 
                className="hover:bg-gray-700 block px-3 py-2 rounded-md text-base font-medium"
                onClick={toggleMenu}
              >
                Cars
              </Link>
              <Link 
                href="/contact" 
                className="hover:bg-gray-700 block px-3 py-2 rounded-md text-base font-medium"
                onClick={toggleMenu}
              >
                Contact Us
              </Link>
              <Link 
                href="/login-signup" 
                className="w-full text-left bg-yellow-500 text-black px-4 py-2 rounded-md font-semibold hover:bg-yellow-600"
                onClick={toggleMenu}
              >
                Login/Signup
              </Link>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}
