from homeassistant.const import Platform

# API
API_ENDPOINT = "https://api.weather.gov"
USER_AGENT = "Home Assistant"

# Config
CONF_TIMEOUT = "timeout"
CONF_INTERVAL = "interval"
CONF_ZONE_ID = "zone_id"
CONF_GPS_LOC = "gps_loc"
CONF_TRACKER = "tracker"

# Defaults
DEFAULT_ICON = "mdi:alert"
DEFAULT_NAME = "NWS Alerts"
DEFAULT_INTERVAL = 1
DEFAULT_TIMEOUT = 120

# Misc
ZONE_ID = ""
VERSION = "2.7"
ISSUE_URL = "https://github.com/finity69x2/nws_alert"
DOMAIN = "nws_alerts"
PLATFORM = "sensor"
ATTRIBUTION = "Data provided by Weather.gov"
COORDINATOR = "coordinator"
PLATFORMS = [Platform.SENSOR]
CONFIG_VERSION = 2  # Config flow version
