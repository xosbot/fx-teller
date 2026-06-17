import { useEffect, useState } from 'react';
import {
  View,
  Text,
  ScrollView,
  Pressable,
  StyleSheet,
  RefreshControl,
} from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Session } from '@fx-teller/shared-types';
import { useAuth } from '../src/auth-context';
import { fetchCurrentSession, fetchUpcomingSessions } from '../src/services/api';
import { colors, spacing, radius } from '../src/theme';

function trialDaysLeft(trialEndsAt: string | null): number {
  if (!trialEndsAt) return 0;
  const ms = new Date(trialEndsAt).getTime() - Date.now();
  return Math.max(0, Math.ceil(ms / (1000 * 60 * 60 * 24)));
}

export default function Home() {
  const router = useRouter();
  const { user } = useAuth();
  const [current, setCurrent] = useState<Session | null>(null);
  const [upcoming, setUpcoming] = useState<Session[]>([]);
  const [refreshing, setRefreshing] = useState(false);

  async function load() {
    setRefreshing(true);
    try {
      const [c, u] = await Promise.all([
        fetchCurrentSession(),
        fetchUpcomingSessions().catch(() => []),
      ]);
      setCurrent(c);
      setUpcoming(u);
    } finally {
      setRefreshing(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  const days = trialDaysLeft(user?.trialEndsAt ?? null);
  const isActive = user?.subscription === 'active';

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <ScrollView
        contentContainerStyle={{ padding: spacing.lg }}
        refreshControl={<RefreshControl refreshing={refreshing} onRefresh={load} tintColor={colors.accent} />}
      >
        <Text style={styles.brand}>
          FX<Text style={{ color: colors.accent }}>-Teller</Text>
        </Text>
        <Text style={styles.greeting}>
          Welcome{user?.name ? `, ${user.name}` : ''}
        </Text>

        {user && !isActive && days > 0 && (
          <View style={styles.trialBanner}>
            <Text style={styles.trialText}>
              🎁 <Text style={{ fontWeight: '700' }}>{days} day{days === 1 ? '' : 's'}</Text> left in your free trial
            </Text>
          </View>
        )}

        {user && !isActive && days === 0 && (
          <Pressable style={styles.paywallBanner} onPress={() => router.push('/paywall')}>
            <Text style={styles.paywallText}>
              ⏰ Your trial has ended. <Text style={{ fontWeight: '700' }}>Subscribe</Text> to continue.
            </Text>
          </Pressable>
        )}

        {/* Live CTA */}
        {current && current.status === 'LIVE' ? (
          <Pressable
            style={styles.liveCard}
            onPress={() => router.push('/live')}
          >
            <View style={styles.liveRow}>
              <View style={styles.liveDotOuter}>
                <View style={styles.liveDotInner} />
              </View>
              <Text style={styles.liveLabel}>LIVE NOW</Text>
            </View>
            <Text style={styles.liveTitle}>{current.title}</Text>
            <Text style={styles.liveSub}>Hosted by {current.hostName}</Text>
            <View style={styles.tapHint}>
              <Text style={styles.tapHintText}>Tap to join →</Text>
            </View>
          </Pressable>
        ) : (
          <View style={styles.offlineCard}>
            <Text style={styles.offlineTitle}>No live session right now</Text>
            <Text style={styles.offlineSub}>
              Check the schedule below or come back during market hours.
            </Text>
          </View>
        )}

        {/* Schedule */}
        <Text style={styles.section}>Upcoming Sessions</Text>
        {upcoming.length === 0 ? (
          <Text style={styles.muted}>No sessions scheduled yet.</Text>
        ) : (
          upcoming.map((s) => (
            <View key={s.id} style={styles.scheduleItem}>
              <View style={{ flex: 1 }}>
                <Text style={styles.scheduleTitle}>{s.title}</Text>
                <Text style={styles.scheduleMeta}>
                  {new Date(s.startsAt).toLocaleString()} · {s.hostName}
                </Text>
              </View>
              <Text
                style={[
                  styles.statusPill,
                  s.status === 'LIVE' && { backgroundColor: colors.danger },
                ]}
              >
                {s.status}
              </Text>
            </View>
          ))
        )}

        <Pressable style={styles.profileLink} onPress={() => router.push('/profile')}>
          <Text style={styles.profileLinkText}>Profile & Settings →</Text>
        </Pressable>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.bg },
  brand: { color: colors.text, fontSize: 28, fontWeight: '800', letterSpacing: -0.5, marginBottom: spacing.xs },
  greeting: { color: colors.textMuted, fontSize: 16, marginBottom: spacing.lg },
  trialBanner: {
    backgroundColor: colors.bgElev,
    borderColor: colors.accent,
    borderWidth: 1,
    borderRadius: radius.md,
    padding: spacing.md,
    marginBottom: spacing.lg,
  },
  trialText: { color: colors.text, fontSize: 14 },
  paywallBanner: {
    backgroundColor: colors.danger,
    borderRadius: radius.md,
    padding: spacing.md,
    marginBottom: spacing.lg,
  },
  paywallText: { color: 'white', fontSize: 14 },
  liveCard: {
    backgroundColor: colors.bgElev,
    borderColor: colors.danger,
    borderWidth: 1.5,
    borderRadius: radius.lg,
    padding: spacing.lg,
    marginBottom: spacing.xl,
  },
  liveRow: { flexDirection: 'row', alignItems: 'center', marginBottom: spacing.sm },
  liveDotOuter: {
    width: 10, height: 10, borderRadius: 5, backgroundColor: colors.danger,
    marginRight: spacing.sm,
  },
  liveDotInner: {},
  liveLabel: { color: colors.danger, fontWeight: '800', fontSize: 13, letterSpacing: 1 },
  liveTitle: { color: colors.text, fontSize: 22, fontWeight: '700', marginBottom: 4 },
  liveSub: { color: colors.textMuted, fontSize: 14, marginBottom: spacing.md },
  tapHint: { backgroundColor: colors.danger, paddingVertical: 10, borderRadius: radius.md, alignItems: 'center' },
  tapHintText: { color: 'white', fontWeight: '700' },
  offlineCard: {
    backgroundColor: colors.bgElev,
    borderRadius: radius.lg,
    padding: spacing.lg,
    marginBottom: spacing.xl,
    alignItems: 'center',
  },
  offlineTitle: { color: colors.text, fontSize: 16, fontWeight: '600', marginBottom: 4 },
  offlineSub: { color: colors.textMuted, fontSize: 13, textAlign: 'center' },
  section: { color: colors.text, fontSize: 18, fontWeight: '700', marginBottom: spacing.md, marginTop: spacing.md },
  muted: { color: colors.textMuted, fontSize: 14 },
  scheduleItem: {
    flexDirection: 'row',
    backgroundColor: colors.bgElev,
    borderRadius: radius.md,
    padding: spacing.md,
    marginBottom: spacing.sm,
    alignItems: 'center',
  },
  scheduleTitle: { color: colors.text, fontSize: 15, fontWeight: '600', marginBottom: 2 },
  scheduleMeta: { color: colors.textMuted, fontSize: 12 },
  statusPill: {
    color: colors.text,
    fontSize: 10,
    fontWeight: '700',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
    overflow: 'hidden',
    backgroundColor: colors.bgElev2,
  },
  profileLink: {
    marginTop: spacing.xl,
    paddingVertical: spacing.md,
    alignItems: 'center',
  },
  profileLinkText: { color: colors.accent, fontSize: 14, fontWeight: '600' },
});
