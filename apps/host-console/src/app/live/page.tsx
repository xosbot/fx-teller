import { redirect } from 'next/navigation';
import LiveConsole from './LiveConsole';

export default function LivePage() {
  if (typeof window !== 'undefined') {
    const token = localStorage.getItem('fxteller_token');
    if (!token) redirect('/');
  }
  return <LiveConsole />;
}
