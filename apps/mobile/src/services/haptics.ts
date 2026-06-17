// Long vibration helper. expo-haptics has limited Android API; for the
// "1.5s long buzz" requirement we use a sequence of impact notifications
// or expo-notifications with a custom pattern on Android (where supported).

import * as Haptics from 'expo-haptics';
import { Platform } from 'react-native';

export async function longVibrate(ms = 1500) {
  try {
    if (Platform.OS === 'ios') {
      // iOS doesn't expose arbitrary-length vibrations; chain impacts
      const count = Math.max(1, Math.floor(ms / 200));
      for (let i = 0; i < count; i++) {
        await Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy);
        await new Promise((r) => setTimeout(r, 180));
      }
    } else {
      // Android: try notification haptic; if API doesn't support arbitrary
      // duration, fall back to a series of impacts.
      try {
        await Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning);
      } catch {
        const count = Math.max(1, Math.floor(ms / 200));
        for (let i = 0; i < count; i++) {
          await Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy);
          await new Promise((r) => setTimeout(r, 180));
        }
      }
    }
  } catch {
    // swallow — haptics is non-essential
  }
}
