"""Constants for the Bird Buddy integration."""

from datetime import timedelta
import logging

from homeassistant.helpers import config_validation as cv
import voluptuous as vol

DOMAIN = "birdbuddy"
LOGGER = logging.getLogger(__package__)
MANUFACTURER = "Bird Buddy, Inc."

# Default polling interval.
# For best performance, this should be less than the access token expiration
POLLING_INTERVAL = timedelta(minutes=10)

CONF_FEEDER_ID = "feeder_id"
CONF_POSTCARD_ID = "postcard_id"
CONF_SHARE = "share"
TRIGGER_TYPE_POSTCARD = "new_postcard"
EVENT_NEW_POSTCARD = f"{DOMAIN}_new_postcard"

SERVICE_COLLECT_POSTCARD = "collect_postcard"
SERVICE_SCHEMA_COLLECT_POSTCARD = vol.Schema(
    {
        vol.Required(CONF_POSTCARD_ID): cv.string,
        vol.Optional(CONF_FEEDER_ID): cv.string,
        vol.Optional(CONF_SHARE): cv.boolean,
    }
)
