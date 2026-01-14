import { useState } from "react";
import { Button } from "../components/ui/button"
import { Input } from "../components/ui/input";
import { Label } from "../components/ui/label";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../components/ui/card";
import { Wallet, Lock, Mail } from "lucide-react";
import {useAuth} from "../hook/useAuth"


interface LoginPageProps {
onLogin: (email: string, password: string) => void;
onSwitchToSignUp: () => void;
}



export function LoginPage({ onSwitchToSignUp }: LoginPageProps) {
    const {login} = useAuth();
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e: React.FormEvent) =>{
        e.preventDefault();
        setError("");

        

        if (!email || !password){
            setError("Please enter both email and password");
            return;
        }

        // Delegate to auth
        const result = await login(email, password);

        if (!result.ok){
            setError(result.message)
        }

    }
    return (
        <div className="min-h-screen bg-gradient-to-br from-primary/10 via-background to-primary/5 flex items-center justify-center p-4">
        <Card className="w-full max-w-md">
            <CardHeader className="space-y-4 text-center">
            <div className="mx-auto bg-primary text-primary-foreground p-3 rounded-xl w-fit">
                <Wallet className="h-8 w-8" />
            </div>
            <div>
                <CardTitle className="text-2xl">Welcome Back</CardTitle>
                <CardDescription>
                Sign in to your Budget Tracker account
                </CardDescription>
            </div>
            </CardHeader>
            <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
                <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <div className="relative">
                    <Mail className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                    <Input
                    id="email"
                    type="email"
                    placeholder="you@example.com"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="pl-10"
                    />
                </div>
                </div>

                <div className="space-y-2">
                <Label htmlFor="password">Password</Label>
                <div className="relative">
                    <Lock className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
                    <Input
                    id="password"
                    type="password"
                    placeholder="Enter your password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="pl-10"
                    />
                </div>
                </div>

                {error && (
                <div className="bg-destructive/10 text-destructive text-sm p-3 rounded-md">
                    {error}
                </div>
                )}

                <Button type="submit" className="w-full">
                Sign In
                </Button>

                <div className="text-sm text-center pt-2">
                <span className="text-muted-foreground">Don't have an account? </span>
                <button
                    type="button"
                    onClick={onSwitchToSignUp}
                    className="text-primary hover:underline"
                >
                    Sign up
                </button>
                </div>
            </form>
            </CardContent>
        </Card>
        </div>
    );
}
