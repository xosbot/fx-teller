import { useEffect, useRef, useState } from 'react';
import {
  View,
  Text,
  Pressable,
  StyleSheet,
  ScrollView,
  Animated,
  Modal,
  Vibration,
  Platform,
} from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Audio } from 'expo-av';
import { TradeCall, MusicCue, Sentiment } from '@fx-teller/shared-types';
import { getHmsToken, fetchCurrentMusicCue, fetchRecentTradeCalls } from '../src/services/api';
import { longVibrate } from '../src/services/haptics';
import { useAuth } from '../src/auth-context';
import { colors, spacing, radius } from '../src/theme';
import { sse } from '../src/services/sse';

// Pre-bundled music. In production these would be served by the backend /
// pre-loaded on first launch. For v1 demo, we use a stub local cue.
const MUSIC = {
  CALM: null, // real asset would be: require('../../assets/music/calm.m4a')
  ALERT: null,
} as const;

export default function Live() {
  const router = useRouter();
  const { user } = useAuth();
  const [hmsToken, setHmsToken] = useState<string | null>(null);
  const [roomId, setRoomId] = useState<string | null>(null);
  const [joined, setJoined] = useState(false);
  const [cue, setCue] = useState<MusicCue | null>(null);
  const [recentCalls, setRecentCalls] = useState<TradeCall[]>([]);
  const [activeCall, setActiveCall] = useState<TradeCall | null>(null);
  const shakeAnim = useRef(new Animated.Value(0)).current;
  const musicRef = useRef<Audio.Sound | null>(null);

  // On mount: fetch token, room info, music cue, recent trade calls
  useEffect(() => {
    (async () => {
      try {
        const t = await getHmsToken();
        setHmsToken(t.token);
        setRoomId(t.roomId);
      } catch (e) {
        // not authed or backend down — surface in UI
      }
      try {
        setCue(await fetchCurrentMusicCue());
        setRecentCalls(await fetchRecentTradeCalls(5));
      } catch {}
    })();
    // Listen for server-pushed trade calls and music cues via SSE
    // (in production, prefer 100ms data channel for in-room events).
    sse.start({
      onTradeCall: (c: TradeCall) => {
        setRecentCalls((prev) => [c, ...prev].slice(0, 10));
        showTradeCall(c);
      },
      onMusicCue: (c: MusicCue) => {
        setCue(c);
        switchMusic(c.sentiment);
      },
    });
    return () => sse.stop();
  }, []);

  // When we have an HMS token, attempt to join. Real 100ms SDK wiring is
  // sketched below but kept lightweight in this prototype stub.
  useEffect(() => {
    if (!hmsToken) return;
    joinRoom(hmsToken);
  }, [hmsToken]);

  async function joinRoom(token: string) {
    try {
      // Production wiring (kept commented for v1 demo):
      //   import { HMSSDK, HMSConfig, HMSUpdateListenerActions } from '@100mslive/react-native-hms';
      //   const hms = await HMSSDK.build();
      //   await hms.join(new HMSConfig({ authToken: token, username: user?.name || 'Listener' }));
      //   hms.addEventListener(HMSUpdateListenerActions.ON_MESSAGE, e => {
      //     const payload = JSON.parse(e.data);
      //     if (payload.type === 'trade_call') showTradeCall(payload.data);
      //     if (payload.type === 'music_cue') switchMusic(payload.sentiment);
      //   });
      setJoined(true);
    } catch (e) {
      // surface error
    }
  }

  function showTradeCall(call: TradeCall) {
    setActiveCall(call);
    longVibrate(1500);
    Animated.sequence([
      Animated.timing(shakeAnim, { toValue: 12, duration: 60, useNativeDriver: true }),
      Animated.timing(shakeAnim, { toValue: -12, duration: 60, useNativeDriver: true }),
      Animated.timing(shakeAnim, { toValue: 8, duration: 60, useNativeDriver: true }),
      Animated.timing(shakeAnim, { toValue: -8, duration: 60, useNativeDriver: true }),
      Animated.timing(shakeAnim, { toValue: 0, duration: 60, useNativeDriver: true }),
    ]).start();
  }

  async function switchMusic(sentiment: Sentiment) {
    if (musicRef.current) {
      try { await musicRef.current.unloadAsync(); } catch {}
    }
    const asset = MUSIC[sentiment];
    if (!asset) return; // dev stub
    const { sound } = await Audio.Sound.createAsync(asset, { isLooping: true, shouldPlay: true });
    musicRef.current = sound;
  }

  function dismissCall() {
    setActiveCall(null);
  }

  const sentimentColor = cue?.sentiment === 'ALERT' ? colors.danger : colors.success;
  const sentimentEmoji = cue?.sentiment === 'ALERT' ? '⚡' : '🌊';

  return (
    <SafeAreaView style={styles.container} edges={['top']}>
      <ScrollView contentContainerStyle={{ padding: spacing.lg }}>
        <Pressable onPress={() => router.back()} style={{ marginBottom: spacing.lg }}>
          <Text style={{ color: colors.textMuted, fontSize: 14 }}>← Back</Text>
        </Pressable>

        {/* Top status */}
        <View style={styles.statusRow}>
          {joined ? (
            <View style={styles.statusPillLive}>
              <View style={styles.liveDot} />
              <Text style={styles.statusPillText}>LIVE</Text>
            </View>
          ) : (
            <View style={styles.statusPillOff}>
              <Text style={styles.statusPillText}>CONNECTING…</Text>
            </View>
          )}
          <Text style={styles.listenerCount}>· {recentCalls.length} calls</Text>
        </View>

        {/* Host card */}
        <View style={styles.hostCard}>
          <View style={styles.hostAvatar}>
            <Text style={styles.hostAvatarText}>🎙️</Text>
          </View>
          <Text style={styles.hostName}>FX-Teller Live</Text>
          <Text style={styles.hostSub}>Live from Kerala</Text>
        </View>

        {/* Music cue */}
        <View style={[styles.cueCard, { borderColor: sentimentColor }]}>
          <Text style={styles.cueEmoji}>{sentimentEmoji}</Text>
          <View style={{ flex: 1 }}>
            <Text style={styles.cueLabel}>NOW PLAYING</Text>
            <Text style={styles.cueTrack}>{cue?.trackName ?? 'Still Water'}</Text>
            <Text style={styles.cueSentiment}>{cue?.sentiment ?? 'CALM'}</Text>
          </View>
        </View>

        {/* Recent trade calls */}
        <Text style={styles.section}>Recent Calls</Text>
        {recentCalls.length === 0 ? (
          <Text style={styles.muted}>No calls yet. Stay tuned.</Text>
        ) : (
          recentCalls.map((c) => (
            <View key={c.id} style={styles.callRow}>
              <View
                style={[
                  styles.sideBadge,
                  { backgroundColor: c.side === 'BUY' ? colors.success : colors.danger },
                ]}
              >
                <Text style={styles.sideBadgeText}>{c.side}</Text>
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.callInstrument}>{c.instrument}</Text>
                <Text style={styles.callDetails}>
                  Entry {c.entry} · SL {c.sl} · TP {c.tp.join('/')}
                </Text>
              </View>
              <Text style={styles.callTime}>
                {new Date(c.pushedAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </Text>
            </View>
          ))
        )}
      </ScrollView>

      {/* Floating trade call modal (full-screen on iOS, can be replaced
          by a true system overlay on Android in v1.5) */}
      <Modal visible={!!activeCall} animationType="slide" transparent onRequestClose={dismissCall}>
        <View style={styles.modalBackdrop}>
          <Animated.View
            style={[
              styles.modalCard,
              { transform: [{ translateX: shakeAnim }] },
            ]}
          >
            {activeCall && (
              <>
                <View
                  style={[
                    styles.modalSide,
                    { backgroundColor: activeCall.side === 'BUY' ? colors.success : colors.danger },
                  ]}
                >
                  <Text style={styles.modalSideText}>{activeCall.side}</Text>
                </View>
                <Text style={styles.modalInstrument}>{activeCall.instrument}</Text>
                <View style={styles.modalRow}>
                  <View style={styles.modalField}>
                    <Text style={styles.modalLabel}>ENTRY</Text>
                    <Text style={styles.modalValue}>{activeCall.entry}</Text>
                  </View>
                  <View style={styles.modalField}>
                    <Text style={styles.modalLabel}>SL</Text>
                    <Text style={[styles.modalValue, { color: colors.danger }]}>{activeCall.sl}</Text>
                  </View>
                  <View style={styles.modalField}>
                    <Text style={styles.modalLabel}>TP</Text>
                    <Text style={[styles.modalValue, { color: colors.success }]}>
                      {activeCall.tp.join(' / ')}
                    </Text>
                  </View>
                </View>
                <Pressable style={styles.modalDismiss} onPress={dismissCall}>
                  <Text style={styles.modalDismissText}>Dismiss</Text>
                </Pressable>
              </>
            )}
          </Animated.View>
        </View>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.bg },
  statusRow: { flexDirection: 'row', alignItems: 'center', marginBottom: spacing.lg },
  statusPillLive: { flexDirection: 'row', alignItems: 'center', backgroundColor: colors.danger, paddingHorizontal: 10, paddingVertical: 4, borderRadius: 6 },
  statusPillOff: { backgroundColor: colors.bgElev2, paddingHorizontal: 10, paddingVertical: 4, borderRadius: 6 },
  statusPillText: { color: 'white', fontWeight: '800', fontSize: 11, letterSpacing: 1 },
  liveDot: { width: 6, height: 6, borderRadius: 3, backgroundColor: 'white', marginRight: 6 },
  listenerCount: { color: colors.textMuted, fontSize: 13, marginLeft: spacing.sm },
  hostCard: { alignItems: 'center', paddingVertical: spacing.xl, marginBottom: spacing.lg },
  hostAvatar: { width: 90, height: 90, borderRadius: 45, backgroundColor: colors.bgElev, alignItems: 'center', justifyContent: 'center', marginBottom: spacing.md, borderWidth: 2, borderColor: colors.accent },
  hostAvatarText: { fontSize: 36 },
  hostName: { color: colors.text, fontSize: 22, fontWeight: '700' },
  hostSub: { color: colors.textMuted, fontSize: 13, marginTop: 2 },
  cueCard: { flexDirection: 'row', alignItems: 'center', backgroundColor: colors.bgElev, borderRadius: radius.lg, padding: spacing.lg, marginBottom: spacing.xl, borderWidth: 1.5 },
  cueEmoji: { fontSize: 36, marginRight: spacing.lg },
  cueLabel: { color: colors.textMuted, fontSize: 10, letterSpacing: 1, fontWeight: '700' },
  cueTrack: { color: colors.text, fontSize: 17, fontWeight: '700', marginTop: 2 },
  cueSentiment: { color: colors.textMuted, fontSize: 12, marginTop: 2 },
  section: { color: colors.text, fontSize: 18, fontWeight: '700', marginBottom: spacing.md, marginTop: spacing.md },
  muted: { color: colors.textMuted, fontSize: 14 },
  callRow: { flexDirection: 'row', alignItems: 'center', backgroundColor: colors.bgElev, borderRadius: radius.md, padding: spacing.md, marginBottom: spacing.sm, gap: spacing.md },
  sideBadge: { paddingHorizontal: 10, paddingVertical: 6, borderRadius: 6 },
  sideBadgeText: { color: 'white', fontWeight: '800', fontSize: 12 },
  callInstrument: { color: colors.text, fontSize: 16, fontWeight: '700' },
  callDetails: { color: colors.textMuted, fontSize: 12, marginTop: 2 },
  callTime: { color: colors.textMuted, fontSize: 12 },
  modalBackdrop: { flex: 1, backgroundColor: 'rgba(11,18,32,0.85)', alignItems: 'center', justifyContent: 'center', padding: spacing.xl },
  modalCard: { width: '100%', backgroundColor: colors.bgElev, borderRadius: radius.xl, padding: spacing.xl, borderWidth: 2, borderColor: colors.accent },
  modalSide: { alignSelf: 'flex-start', paddingHorizontal: 14, paddingVertical: 6, borderRadius: 8, marginBottom: spacing.md },
  modalSideText: { color: 'white', fontWeight: '800', fontSize: 14, letterSpacing: 1 },
  modalInstrument: { color: colors.text, fontSize: 32, fontWeight: '800', marginBottom: spacing.lg },
  modalRow: { flexDirection: 'row', gap: spacing.md, marginBottom: spacing.xl },
  modalField: { flex: 1, backgroundColor: colors.bgElev2, padding: spacing.md, borderRadius: radius.md },
  modalLabel: { color: colors.textMuted, fontSize: 11, fontWeight: '700', letterSpacing: 1 },
  modalValue: { color: colors.text, fontSize: 18, fontWeight: '700', marginTop: 4 },
  modalDismiss: { backgroundColor: colors.bgElev2, paddingVertical: 12, borderRadius: radius.md, alignItems: 'center' },
  modalDismissText: { color: colors.text, fontWeight: '600' },
});
