import type { Metadata } from 'next';
import './globals.css';
import Header from './components/Header';
import Footer from './components/Footer';

export const metadata: Metadata = {
  title: 'FX-Teller — Live podcast trading community for Kerala',
  description:
    'FX-Teller is a live podcast trading community for forex traders in Kerala. Real-time audio commentary, push trade calls with vibration, and sentiment-driven music cues — all in your phone.',
  keywords: [
    'forex trading',
    'Kerala traders',
    'live podcast',
    'trade calls',
    'FX-Teller',
    'forex community India',
  ],
  openGraph: {
    title: 'FX-Teller — Live podcast trading community',
    description:
      'Live forex commentary, push trade calls, and a community built for Kerala traders.',
    type: 'website',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Header />
        <main>{children}</main>
        <Footer />
      </body>
    </html>
  );
}
