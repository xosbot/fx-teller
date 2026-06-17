import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'FX-Teller Host Console',
  description: 'Live podcast control for FX-Teller hosts',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
