"use client";

import { useState } from 'react';
import axios from 'axios';
import { useRouter } from 'next/navigation';

const LoginSignupPage = () => {
    const [isLogin, setIsLogin] = useState(true);
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [phone, setPhone] = useState('');
    const [address, setAddress] = useState('');
    const [zipCode, setZipCode] = useState('');
    const [city, setCity] = useState('');
    const [state, setState] = useState('');
    const [role, setRole] = useState('customer');
    const [errorMessage, setErrorMessage] = useState('');
    const router = useRouter();

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        try {
            const response = await axios.post('http://127.0.0.1:8000/auth/login', { username: email, password });
            localStorage.setItem('access_token', response.data.token);
            router.push('/dashboard');
        } catch (error) {
            setErrorMessage('Invalid credentials. Please try again!');
        }
    };

    const handleSignup = async (e: React.FormEvent) => {
        e.preventDefault();
        const signupData = {
            email,
            password,
            first_name: firstName,
            last_name: lastName,
            phone,
            address,
            zip_code: zipCode,
            city,
            state,
            role
        };

        try {
            const response = await axios.post('http://127.0.0.1:8000/auth/signup', signupData);
            localStorage.setItem('access_token', response.data.token);
            router.push('/dashboard');
        } catch (error) {
            setErrorMessage('Signup failed. Please try again!');
        }
    };

    return (
        <div className="max-w-lg mx-auto mt-12">
            <h1 className="text-3xl font-bold text-center">{isLogin ? 'Login' : 'Sign Up'}</h1>
            <form onSubmit={isLogin ? handleLogin : handleSignup} className="mt-8 space-y-6">
                <div>
                    <label htmlFor="email" className="block text-gray-700">Email</label>
                    <input
                        type="email"
                        id="email"
                        name="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                        className="w-full p-3 border border-gray-300 rounded mt-2"
                    />
                </div>

                <div>
                    <label htmlFor="password" className="block text-gray-700">Password</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                        className="w-full p-3 border border-gray-300 rounded mt-2"
                    />
                </div>

                {!isLogin && (
                    <>
                        <div>
                            <label htmlFor="firstName" className="block text-gray-700">First Name</label>
                            <input
                                type="text"
                                id="firstName"
                                name="firstName"
                                value={firstName}
                                onChange={(e) => setFirstName(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            />
                        </div>

                        <div>
                            <label htmlFor="lastName" className="block text-gray-700">Last Name</label>
                            <input
                                type="text"
                                id="lastName"
                                name="lastName"
                                value={lastName}
                                onChange={(e) => setLastName(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            />
                        </div>

                        <div>
                            <label htmlFor="phone" className="block text-gray-700">Phone</label>
                            <input
                                type="text"
                                id="phone"
                                name="phone"
                                value={phone}
                                onChange={(e) => setPhone(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            />
                        </div>

                        <div>
                            <label htmlFor="address" className="block text-gray-700">Address</label>
                            <input
                                type="text"
                                id="address"
                                name="address"
                                value={address}
                                onChange={(e) => setAddress(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            />
                        </div>

                        <div>
                            <label htmlFor="city" className="block text-gray-700">City</label>
                            <input
                                type="text"
                                id="city"
                                name="city"
                                value={city}
                                onChange={(e) => setCity(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            />
                        </div>

                        <div>
                            <label htmlFor="state" className="block text-gray-700">State</label>
                            <input
                                type="text"
                                id="state"
                                name="state"
                                value={state}
                                onChange={(e) => setState(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            />
                        </div>

                        <div>
                            <label htmlFor="zipCode" className="block text-gray-700">Zip Code</label>
                            <input
                                type="text"
                                id="zipCode"
                                name="zipCode"
                                value={zipCode}
                                onChange={(e) => setZipCode(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            />
                        </div>

                        <div>
                            <label htmlFor="role" className="block text-gray-700">Role</label>
                            <select
                                id="role"
                                value={role}
                                onChange={(e) => setRole(e.target.value)}
                                required
                                className="w-full p-3 border border-gray-300 rounded mt-2"
                            >
                                <option value="customer">Customer</option>
                                <option value="employee">Employee</option>
                            </select>
                        </div>
                    </>
                )}

                {errorMessage && <p className="text-red-500">{errorMessage}</p>}

                <div className="mt-4">
                    <button
                        type="submit"
                        className="w-full py-3 px-4 bg-blue-600 text-white font-semibold rounded"
                    >
                        {isLogin ? 'Login' : 'Sign Up'}
                    </button>
                </div>
            </form>

            <div className="mt-4 text-center">
                {isLogin ? (
                    <p>
                        Don't have an account?{' '}
                        <span
                            onClick={() => setIsLogin(false)}
                            className="text-blue-600 cursor-pointer"
                        >
                            Sign Up
                        </span>
                    </p>
                ) : (
                    <p>
                        Already have an account?{' '}
                        <span
                            onClick={() => setIsLogin(true)}
                            className="text-blue-600 cursor-pointer"
                        >
                            Login
                        </span>
                    </p>
                )}
            </div>
        </div>
    );
};

export default LoginSignupPage;
