import { requireNativeModule, EventEmitter } from 'expo-modules-core';

type Side = 'BUY' | 'SELL';

export interface TradeCallPayload {
  title?: string;
  body?: string;
  instrument?: string;
  side?: Side;
  entry?: string | number;
  sl?: string | number;
  tp?: string | number;
  durationMs?: number;
}

type Events = {
  onOverlayTap: (event: { nativeEvent: Record<string, never> }) => void;
  onOverlayDismiss: (event: { nativeEvent: Record<string, never> }) => void;
};

declare class FloatingOverlayModule extends EventEmitter<Events> {
  hasOverlayPermission(): Promise<boolean>;
  requestOverlayPermission(): Promise<boolean>;
  showOverlay(payload: TradeCallPayload, autoDismissMs?: number): Promise<void>;
  hideOverlay(): Promise<void>;
}

const Overlay = requireNativeModule<FloatingOverlayModule>('FloatingOverlay');

export default Overlay;
