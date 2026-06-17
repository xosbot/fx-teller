'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const links = [
  { href: '/', label: 'Home' },
  { href: '/features', label: 'Features' },
  { href: '/app-preview', label: 'App UI' },
  { href: '/roadmap', label: 'Roadmap' },
  { href: '/marketing', label: 'Marketing' },
  { href: '/demo', label: 'Demo' },
];

export default function Header() {
  const pathname = usePathname();
  return (
    <header className="site-header">
      <div className="container site-header-inner">
        <Link href="/" className="brand">
          <span className="dot" />
          FX<b>-Teller</b>
        </Link>
        <nav className="nav">
          {links.map((l) => {
            const active = pathname === l.href;
            return (
              <Link key={l.href} href={l.href} className={active ? 'active' : ''}>
                {l.label}
              </Link>
            );
          })}
          <Link href="/demo" className="btn nav-cta" style={{ marginLeft: 8 }}>
            Try Demo
          </Link>
        </nav>
      </div>
    </header>
  );
}
