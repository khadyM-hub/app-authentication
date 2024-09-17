"use client"; 

import Link from "next/link";
import { useState } from "react";

export default function Home() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch("/api/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Login successful:", data);
      } else {
        console.error("Login failed");
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <main className="w-full max-w-sm p-8 bg-white shadow-md rounded-lg">
      <h1 className="text-2xl font-bold text-center mb-6 text-black">Login</h1>

        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <input
            type="email"
            name="email"
            placeholder="Please enter your email"
            value={formData.email}
            onChange={handleChange}
            required
            className=" w-full p-3 mb-4 border border-green-500 rounded-lg focus:outline-none focus:border-green-500"
          />
          <input
            type="password"
            name="password"
            placeholder="Please enter password"
            value={formData.password}
            onChange={handleChange}
            required
            className=" w-full p-3 mb-4 border border-green-500 rounded-lg focus:outline-none focus:border-green-500"
          />
          <button
            type="submit"
            className="w-full py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
          >
            Log In
          </button>
        </form>
        <p className="mt-4 text-center text-black" >
          Don’t have an account?{" "}
          <Link href="/sign-up" className="text-blue-500 hover:underline">
            Sign up
          </Link>
        </p>
        <p className="mt-2 text-center">
          <Link href="/forgot-password" className="text-blue-500 hover:underline">
            Forgot Password?
          </Link>
        </p>
      </main>
    </div>
  );
}