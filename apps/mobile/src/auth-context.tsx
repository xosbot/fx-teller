import { createContext, useContext, useEffect, useState, ReactNode } from 'react';
import { User } from '@fx-teller/shared-types';
import { getToken, getUser, clearAuth } from './services/auth';

interface AuthCtx {
  user: User | null;
  loading: boolean;
  signOut: () => Promise<void>;
  refresh: () => Promise<void>;
}

const Ctx = createContext<AuthCtx | null>(null);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  async function refresh() {
    const token = await getToken();
    if (!token) {
      setUser(null);
      return;
    }
    const u = await getUser();
    setUser(u);
  }

  useEffect(() => {
    refresh().finally(() => setLoading(false));
  }, []);

  async function signOut() {
    await clearAuth();
    setUser(null);
  }

  return (
    <Ctx.Provider value={{ user, loading, signOut, refresh }}>{children}</Ctx.Provider>
  );
}

export function useAuth() {
  const c = useContext(Ctx);
  if (!c) throw new Error('useAuth must be inside AuthProvider');
  return c;
}
