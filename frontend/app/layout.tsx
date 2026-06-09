import React from 'react';
import './globals.css';

export const metadata = {
  title: 'StartupOS',
  description: 'AI-powered Startup Operating System',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
