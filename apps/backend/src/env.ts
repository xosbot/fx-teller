// Centralized env access. Reads from process.env with sensible defaults for dev.
// In production, secrets should be injected as env vars by the host.
export const env = {
  port: parseInt(process.env.PORT || '3000', 10),
  nodeEnv: process.env.NODE_ENV || 'development',
  databaseUrl:
    process.env.DATABASE_URL ||
    'postgres://fxteller:fxteller@localhost:5432/fxteller',
  jwtSecret: process.env.JWT_SECRET || 'dev-only-change-me-in-prod',
  jwtExpiresIn: process.env.JWT_EXPIRES_IN || '30d',
  hmsAppAccessKey: process.env.HMS_APP_ACCESS_KEY || 'dev-access-key',
  hmsAppSecret: process.env.HMS_APP_SECRET || 'dev-secret',
  hmsTemplateId: process.env.HMS_TEMPLATE_ID || 'dev-template',
  hmsRoleListener: process.env.HMS_ROLE_LISTENER || 'listener',
  hmsRoleHost: process.env.HMS_ROLE_HOST || 'host',
  rzpKeyId: process.env.RZP_KEY_ID || 'rzp_test_xxx',
  rzpKeySecret: process.env.RZP_KEY_SECRET || 'rzp_test_xxx',
  rzpWebhookSecret: process.env.RZP_WEBHOOK_SECRET || 'dev-webhook-secret',
  rzpPlanMonthly: process.env.RZP_PLAN_MONTHLY || 'plan_dev_monthly',
  trialDays: parseInt(process.env.TRIAL_DAYS || '3', 10),
};
