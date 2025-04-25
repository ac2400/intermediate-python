const BASE_URL = "http://Aleks-MacBook-Air.local:8000";

export async function getHabits() {
    const res = await fetch(`${BASE_URL}/habits`);
    if (!res.ok) throw new Error("Failed to fetch habits");
  
    const data = await res.json();
    console.log("✅ Successfully fetched habits:", data);
    return data;
  }

export async function applyFreePass(habitId: number) {
    const res = await fetch(`${BASE_URL}/habits/${habitId}/free_pass`, {
        method: "POST",
    });
    if (!res.ok) throw new Error("Failed to apply free pass");
    return res.json();
}