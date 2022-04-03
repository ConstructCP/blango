from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class AnonSustainedThrottle(AnonRateThrottle):
  scope = 'anon_sustained'


class AnonBurstThrottle(AnonRateThrottle):
  scope = 'anon_burst'


class UserSustainedThrottle(AnonRateThrottle):
  scope = 'user_sustained'


class UserBurstThrottle(AnonRateThrottle):
  scope = 'user_burst'
