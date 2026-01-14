import { createContext, useCallback ,useContext, useState, useEffect, useMemo } from 'react';

type User = {
  id: number;
  email: string;
  name: string;
};

type AuthContextValue = {
    // state
    //user: User;
    //accessToken: string | null;

    // action
    login: (email: string, password: string) => Promise<LoginResult>;

};

type LoginResult = {ok: true} | {ok: false; message: string}

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children, baseUrl = "http://localhost:8000" }: { children: React.ReactNode, baseUrl?: string; }) {
  const [accessToken, setAccessToken] = useState<string | null>(null);
  const [user, setUser] = useState<User | null>(null);

  // Action
  const login = useCallback(
    async (email: string, password: string): Promise<LoginResult> => {
        try{
            const res = await fetch(`${baseUrl}/auth/login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                credentials: "include", // REQUIRED so backend can set refresh cookie
                body: JSON.stringify({ email, password }),
            });

            if (!res.ok) {
                // Try to read backend error
                let msg = "Invalid Credentials"
                try{
                    const err = await res.json()
                    msg = err?.detail ?? msg;
                } catch {
                    // ignore
                }
                return {ok: false, message: msg};                
            }
            const data = await res.json()
            console.log(data)
            return {ok: true}
        }
        catch{
            return {ok: false, message: 'Network Error'}
        }
    }, [baseUrl]
  );

    const value = useMemo<AuthContextValue>(
        () => ({
            login,
        }),
        [login]
    );
    return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
  
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within <AuthProvider>");
  return ctx;
}