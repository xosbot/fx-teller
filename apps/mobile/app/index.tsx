import { Redirect, useRouter } from 'expo-router';
import { useEffect } from 'react';
import { View, Text, ActivityIndicator } from 'react-native';
import { useAuth } from '../src/auth-context';
import { colors } from '../src/theme';

export default function Index() {
  const { user, loading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (loading) return;
    if (user) router.replace('/home');
    else router.replace('/auth');
  }, [user, loading, router]);

  return (
    <View
      style={{
        flex: 1,
        backgroundColor: colors.bg,
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <Text
        style={{
          color: colors.text,
          fontSize: 32,
          fontWeight: '800',
          letterSpacing: -1,
        }}
      >
        FX<Text style={{ color: colors.accent }}>-Teller</Text>
      </Text>
      <ActivityIndicator color={colors.accent} style={{ marginTop: 32 }} />
    </View>
  );
}
