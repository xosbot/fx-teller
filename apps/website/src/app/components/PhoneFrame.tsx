import type { ReactNode } from 'react';

type PhoneFrameProps = {
  children: ReactNode;
  statusTime?: string;
};

export default function PhoneFrame({ children, statusTime = '9:41' }: PhoneFrameProps) {
  return (
    <div className="phone-frame">
      <div className="phone-notch" />
      <div className="phone-screen">
        <div className="phone-statusbar">
          <span>{statusTime}</span>
          <div className="right">
            <span>•••</span>
            <span>◐</span>
            <span>▮▮</span>
          </div>
        </div>
        <div className="phone-content">{children}</div>
      </div>
    </div>
  );
}
