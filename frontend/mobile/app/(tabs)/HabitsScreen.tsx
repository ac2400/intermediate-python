import React, { useEffect, useState } from "react";
import { View, Text, FlatList, useColorScheme } from "react-native";
import { getHabits } from "../../services/api"; // ← use your helper here

type Habit = {
  id: number;
  name: string;
  last_completed: string;
};

const HabitsScreen = () => {
  const [habits, setHabits] = useState<Habit[]>([]);
  const colorScheme = useColorScheme();
  const isDark = colorScheme === "dark";

  useEffect(() => {
    const fetchHabits = async () => {
      try {
        const data = await getHabits(); // ← cleaner!
        setHabits(data);
      } catch (err) {
        console.error("Error fetching habits:", err);
      }
    };

    fetchHabits();
  }, []);

  return (
    <View
      style={{
        flex: 1,
        padding: 16,
        backgroundColor: isDark ? "#121212" : "#ffffff",
      }}
    >
      <Text
        style={{
          fontSize: 20,
          fontWeight: "bold",
          color: isDark ? "#fff" : "#000",
        }}
      >
        Habits:
      </Text>
      <FlatList
        data={habits}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <Text style={{ marginVertical: 8, color: isDark ? "#ddd" : "#222" }}>
            {item.name}
          </Text>
        )}
      />
    </View>
  );
};

export default HabitsScreen;
