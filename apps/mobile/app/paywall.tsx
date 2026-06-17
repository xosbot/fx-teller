import { useState } from 'react';
import {
  View,
  Text,
  Pressable,
  StyleSheet,
  ScrollView,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import RazorpayCheckout from 'react-native-razorpay';
import { API_URL } from '../src/config';
import { getToken } from '../src/services/auth';
import { useAuth } from '../src/auth-context';
import { colors, spacing, radius } from '../src/theme';

export default function Paywall() {
  const router = useRouter();
  const { refresh } = useAuth();
  const [loading, setLoading] = useState(false);

  async function subscribe() {
    setLoading(true);
    try {
      const token = await getToken();
      const sub = await fetch(`${API_URL}/subscriptions/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
        body: JSON.stringify({ planId: 'plan_monthly' }),
      }).then((r) => r.json());

      const result = await RazorpayCheckout.open({
        key: sub.keyId,
        subscription_id: sub.subscriptionId,
        name: 'FX-Teller Premium',
        description: 'Live podcast trading community',
        prefill: { contact: '+919999999999' },
        theme: { color: '#F5B400' },
      });
      // Verify on server (optional for UX; webhook is source of truth)
      await fetch(`${API_URL}/subscriptions/verify`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(result),
      });
      await refresh();
      Alert.alert('Welcome!', 'Your subscription is active.');
      router.replace('/home');
    } catch (e: any) {
      if (e?.code !== 0) {
        Alert.alert('Payment', e?.description || 'Payment was cancelled or failed');
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <ScrollView contentContainerStyle={{ padding: spacing.lg }}>
        <Pressable onPress={() => router.back()} style={{ marginBottom: spacing.lg }}>
          <Text style={{ color: colors.textMuted, fontSize: 14 }}>← Back</Text>
        </Pressable>

        <Text style={styles.title}>Continue with FX-Teller Premium</Text>
        <Text style={styles.sub}>
          Live podcast trading room. Real-time commentary. Music-based trend signals.
        </Text>

        <View style={styles.card}>
          <Text style={styles.planName}>Premium Monthly</Text>
          <View style={styles.priceRow}>
            <Text style={styles.price}>₹499</Text>
            <Text style={styles.per}>/ month</Text>
          </View>
          <View style={styles.bulletRow}>
            <Text style={styles.bullet}>• Live audio commentary</Text>
            <Text style={styles.bullet}>• Trade call alerts with vibration</Text>
            <Text style={styles.bullet}>• Music-based trend signals</Text>
            <Text style={styles.bullet}>• Background listening</Text>
          </View>
        </View>

        <Pressable style={styles.cta} onPress={subscribe} disabled={loading}>
          {loading ? (
            <ActivityIndicator color="#0B1220" />
          ) : (
            <Text style={styles.ctaText}>Subscribe ₹499 / month</Text>
          )}
        </Pressable>

        <Text style={styles.smallNote}>
          Cancel anytime from your profile. UPI, cards, and netbanking supported.
        </Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.bg },
  title: { color: colors.text, fontSize: 24, fontWeight: '800', marginBottom: spacing.sm },
  sub: { color: colors.textMuted, fontSize: 14, marginBottom: spacing.xl, lineHeight: 20 },
  card: {
    backgroundColor: colors.bgElev,
    borderRadius: radius.lg,
    padding: spacing.lg,
    borderWidth: 1.5,
    borderColor: colors.accent,
    marginBottom: spacing.xl,
  },
  planName: { color: colors.textMuted, fontSize: 12, fontWeight: '700', letterSpacing: 1, textTransform: 'uppercase' },
  priceRow: { flexDirection: 'row', alignItems: 'baseline', marginVertical: spacing.md },
  price: { color: colors.text, fontSize: 44, fontWeight: '800', letterSpacing: -1 },
  per: { color: colors.textMuted, fontSize: 16, marginLeft: 4 },
  bulletRow: { marginTop: spacing.md, gap: spacing.sm },
  bullet: { color: colors.text, fontSize: 14, marginBottom: 4 },
  cta: { backgroundColor: colors.accent, paddingVertical: 16, borderRadius: radius.md, alignItems: 'center', marginBottom: spacing.md },
  ctaText: { color: '#0B1220', fontSize: 17, fontWeight: '800' },
  smallNote: { color: colors.textMuted, fontSize: 12, textAlign: 'center', lineHeight: 18 },
});
