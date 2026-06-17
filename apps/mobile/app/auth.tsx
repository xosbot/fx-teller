import { useState } from 'react';
import {
  View,
  Text,
  TextInput,
  Pressable,
  StyleSheet,
  KeyboardAvoidingView,
  Platform,
  Alert,
} from 'react-native';
import { useRouter } from 'expo-router';
import { SafeAreaView } from 'react-native-safe-area-context';
import { requestOtp, verifyOtp } from '../src/services/auth';
import { useAuth } from '../src/auth-context';
import { colors, spacing, radius } from '../src/theme';

export default function Auth() {
  const router = useRouter();
  const { refresh } = useAuth();
  const [phone, setPhone] = useState('');
  const [code, setCode] = useState('');
  const [stage, setStage] = useState<'phone' | 'code'>('phone');
  const [loading, setLoading] = useState(false);

  async function onRequest() {
    if (phone.length < 10) {
      Alert.alert('Invalid phone', 'Enter a 10-digit Indian mobile number');
      return;
    }
    setLoading(true);
    try {
      const res = await requestOtp(`+91${phone}`);
      if (res.devCode) {
        Alert.alert('Dev mode', `Your code is ${res.devCode}`);
      }
      setStage('code');
    } catch (e: any) {
      Alert.alert('Failed', e.message);
    } finally {
      setLoading(false);
    }
  }

  async function onVerify() {
    if (code.length !== 6) {
      Alert.alert('Invalid code', 'Enter the 6-digit code');
      return;
    }
    setLoading(true);
    try {
      await verifyOtp(`+91${phone}`, code);
      await refresh();
      router.replace('/home');
    } catch (e: any) {
      Alert.alert('Failed', e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <SafeAreaView style={styles.container}>
      <KeyboardAvoidingView
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
        style={{ flex: 1, justifyContent: 'center', padding: spacing.xl }}
      >
        <Text style={styles.brand}>
          FX<Text style={{ color: colors.accent }}>-Teller</Text>
        </Text>
        <Text style={styles.tagline}>Live market commentary, on the go</Text>

        <View style={styles.card}>
          {stage === 'phone' ? (
            <>
              <Text style={styles.label}>Mobile Number</Text>
              <View style={styles.phoneRow}>
                <View style={styles.countryCode}>
                  <Text style={styles.countryCodeText}>+91</Text>
                </View>
                <TextInput
                  style={styles.input}
                  value={phone}
                  onChangeText={(v) => setPhone(v.replace(/\D/g, '').slice(0, 10))}
                  keyboardType="number-pad"
                  placeholder="98765 43210"
                  placeholderTextColor={colors.textMuted}
                  maxLength={10}
                />
              </View>
              <Pressable
                style={[styles.btn, loading && { opacity: 0.6 }]}
                onPress={onRequest}
                disabled={loading}
              >
                <Text style={styles.btnText}>{loading ? 'Sending…' : 'Send Code'}</Text>
              </Pressable>
            </>
          ) : (
            <>
              <Text style={styles.label}>Enter 6-digit code</Text>
              <Text style={styles.smallMuted}>Sent to +91 {phone}</Text>
              <TextInput
                style={[styles.input, { letterSpacing: 8, fontSize: 22, textAlign: 'center' }]}
                value={code}
                onChangeText={(v) => setCode(v.replace(/\D/g, '').slice(0, 6))}
                keyboardType="number-pad"
                placeholder="------"
                placeholderTextColor={colors.textMuted}
                maxLength={6}
              />
              <Pressable
                style={[styles.btn, loading && { opacity: 0.6 }]}
                onPress={onVerify}
                disabled={loading}
              >
                <Text style={styles.btnText}>{loading ? 'Verifying…' : 'Verify & Continue'}</Text>
              </Pressable>
              <Pressable onPress={() => setStage('phone')} style={{ marginTop: spacing.md }}>
                <Text style={{ color: colors.textMuted, textAlign: 'center' }}>
                  Change number
                </Text>
              </Pressable>
            </>
          )}
        </View>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: colors.bg },
  brand: {
    color: colors.text,
    fontSize: 36,
    fontWeight: '800',
    textAlign: 'center',
    letterSpacing: -1,
  },
  tagline: {
    color: colors.textMuted,
    textAlign: 'center',
    marginTop: spacing.sm,
    marginBottom: spacing.xxl,
  },
  card: {
    backgroundColor: colors.bgElev,
    borderRadius: radius.lg,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: colors.border,
  },
  label: {
    color: colors.textMuted,
    fontSize: 12,
    fontWeight: '600',
    letterSpacing: 0.5,
    textTransform: 'uppercase',
    marginBottom: spacing.sm,
  },
  smallMuted: { color: colors.textMuted, fontSize: 13, marginBottom: spacing.md },
  phoneRow: { flexDirection: 'row', gap: spacing.sm, marginBottom: spacing.lg },
  countryCode: {
    backgroundColor: colors.bgElev2,
    borderRadius: radius.md,
    paddingHorizontal: spacing.md,
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: colors.border,
  },
  countryCodeText: { color: colors.text, fontSize: 16, fontWeight: '600' },
  input: {
    flex: 1,
    backgroundColor: colors.bgElev2,
    borderRadius: radius.md,
    paddingHorizontal: spacing.md,
    paddingVertical: 14,
    color: colors.text,
    fontSize: 16,
    borderWidth: 1,
    borderColor: colors.border,
  },
  btn: {
    backgroundColor: colors.accent,
    borderRadius: radius.md,
    paddingVertical: 14,
    alignItems: 'center',
  },
  btnText: { color: '#0B1220', fontSize: 16, fontWeight: '700' },
});
