"use client"; // Make this a client component

import { useState } from "react";

export default function ForgotPassword() {
  const [email, setEmail] = useState("");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEmail(e.target.value);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/api/forgot-password", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email }),
      });

      if (response.ok) {
        console.log("Password reset email sent");
      } else {
        console.error("Failed to send password reset email");
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <main className="w-full max-w-sm p-8 bg-white shadow-md rounded-lg">
        <h1 className="text-2xl font-bold text-center mb-6 text-red">Forgot Password</h1>
        <form onSubmit={handleSubmit} className="flex flex-col gap-4">
          <input
            type="email"
            name="email"
            placeholder="Enter your email"
            value={email}
            onChange={handleChange}
            required
            className="border border-gray-300 rounded-lg p-2 text-red-500 focus:outline-none focus:border-red-500"
          />
          <button
            type="submit"
            className="w-full py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors"
          >
            Send Reset Link
          </button>
        </form>
      </main>
    </div>
  );
}

