import { View, Text, Pressable, StyleSheet, Alert } from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useAuth } from '../src/auth-context';
import { colors, spacing, radius } from '../src/theme';

export default function Profile() {
  const router = useRouter();
  const { user, signOut } = useAuth();

  async function onSignOut() {
    await signOut();
    router.replace('/auth');
  }

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <View style={{ padding: spacing.lg }}>
        <Pressable onPress={() => router.back()} style={{ marginBottom: spacing.lg }}>
          <Text style={{ color: colors.textMuted, fontSize: 14 }}>← Back</Text>
        </Pressable>

        <View style={styles.avatar}>
          <Text style={styles.avatarText}>{(user?.name || 'U').charAt(0).toUpperCase()}</Text>
        </View>
        <Text style={styles.name}>{user?.name || 'Trader'}</Text>
        <Text style={styles.phone}>{user?.phone || ''}</Text>

        <View style={styles.card}>
          <Text style={styles.cardLabel}>SUBSCRIPTION</Text>
          {user?.subscription === 'active' ? (
            <Text style={[styles.cardValue, { color: colors.success }]}>Active</Text>
          ) : user?.subscription === 'trialing' ? (
            <Text style={[styles.cardValue, { color: colors.accent }]}>
              Free Trial · ends {new Date(user.trialEndsAt!).toLocaleDateString()}
            </Text>
          ) : (
            <Pressable onPress={() => router.push('/paywall')}>
              <Text style={[styles.cardValue, { color: colors.danger }]}>
                Expired — Subscribe →
              </Text>
            </Pressable>
          )}
        </View>

        <View style={styles.card}>
          <Text style={styles.cardLabel}>ABOUT</Text>
          <Text style={styles.aboutText}>
            FX-Teller is a live podcast trading community for forex traders in Kerala.
            Educational commentary only — not financial advice.
          </Text>
        </View>

        <Pressable style={styles.signOutBtn} onPress={onSignOut}>
          <Text style={styles.signOutText}>Sign Out</Text>
        </Pressable>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.bg },
  avatar: { width: 80, height: 80, borderRadius: 40, backgroundColor: colors.accent, alignItems: 'center', justifyContent: 'center', marginBottom: spacing.md },
  avatarText: { color: '#0B1220', fontSize: 32, fontWeight: '800' },
  name: { color: colors.text, fontSize: 22, fontWeight: '700' },
  phone: { color: colors.textMuted, fontSize: 14, marginBottom: spacing.xl },
  card: { backgroundColor: colors.bgElev, borderRadius: radius.md, padding: spacing.lg, marginBottom: spacing.md, borderWidth: 1, borderColor: colors.border },
  cardLabel: { color: colors.textMuted, fontSize: 11, fontWeight: '700', letterSpacing: 1, marginBottom: spacing.sm },
  cardValue: { color: colors.text, fontSize: 16, fontWeight: '600' },
  aboutText: { color: colors.textMuted, fontSize: 14, lineHeight: 20 },
  signOutBtn: { marginTop: spacing.xl, backgroundColor: colors.bgElev, borderRadius: radius.md, paddingVertical: 14, alignItems: 'center', borderWidth: 1, borderColor: colors.border },
  signOutText: { color: colors.danger, fontSize: 15, fontWeight: '600' },
});
