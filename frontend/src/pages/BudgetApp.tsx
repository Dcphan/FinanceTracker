import { useState, useEffect } from "react";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@radix-ui/react-select";
import { Plus, Calendar, Wallet, LogOut } from "lucide-react";
import { Button} from "@/components/ui/button";


interface UserInformation {
    userName: String
}
export function BudgetApp({userName}: UserInformation ){

    const [currentMonth, setCurrentMonth] = useState(
        new Date().toISOString().slice(0, 7)
    );
    
    const generateMonthOptions = () => {
        const options = [];
        const currentDate = new Date();
        for (let i = 0; i < 12; i++) {
        const date = new Date(currentDate.getFullYear(), currentDate.getMonth() - i, 1);
        const value = date.toISOString().slice(0, 7);
        const label = date.toLocaleDateString('en-US', { month: 'long', year: 'numeric' });
        options.push({ value, label });
        }
        return options;
    };

    const monthOptions = generateMonthOptions();

    return (
         <div className="min-h-screen bg-background">
            <div className="border-b">
                <div className="container mx-auto px-4 py-4">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-3">
                    <div className="bg-primary text-primary-foreground p-2 rounded-lg">
                        <Wallet className="h-6 w-6" />
                    </div>
                    <div>
                        <h1>Budget Tracker</h1>
                        <p className="text-sm text-muted-foreground">
                        Manage your personal finances
                        </p>
                    </div>
                    </div>
                    <div className="flex items-center gap-3">
                    <div className="hidden sm:block text-sm text-muted-foreground">
                        {userName}
                    </div>
                    <div className="flex items-center gap-2">
                        <Calendar className="h-4 w-4 text-muted-foreground" />
                        <Select value={currentMonth} onValueChange={setCurrentMonth}>
                        <SelectTrigger className="w-[180px]">
                            <SelectValue />
                        </SelectTrigger>
                        <SelectContent>
                            {monthOptions.map(option => (
                            <SelectItem key={option.value} value={option.value}>
                                {option.label}
                            </SelectItem>
                            ))}
                        </SelectContent>
                        </Select>
                    </div>
                    {/* <Button onClick={() => setDialogOpen(true)}>
                        <Plus className="h-4 w-4 mr-2" />
                        Add Transaction
                    </Button>
                    <Button variant="outline" onClick={onLogout}>
                        <LogOut className="h-4 w-4 mr-2" />
                        Logout
                    </Button> */}
                    </div>
                    
                </div>
                </div>
            </div>
         </div>
    )
}
